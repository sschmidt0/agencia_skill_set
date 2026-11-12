"""Interfaz web para generar anuncios inmobiliarios con el skill generador-descripciones-inmobiliarias."""

from __future__ import annotations

import os
import re
from pathlib import Path

import anthropic
import streamlit as st
from dotenv import load_dotenv

from skill_engine import ListingSession, SkillError, SkillReply

# Carga app/.env (ANTHROPIC_API_KEY). Una variable ya definida en el entorno tiene prioridad.
load_dotenv(Path(__file__).resolve().parent / ".env")

st.set_page_config(page_title="Anuncios inmobiliarios", page_icon=":material/home_work:", layout="wide")

st.markdown(
    """
    <style>
    .block-container { padding-top: 2.2rem; max-width: 1280px; }
    .app-subtitle { color: #5f6b67; margin-top: -0.6rem; margin-bottom: 1.6rem; font-size: 1.02rem; }
    .section-label { font-size: 0.78rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase;
                     color: #2f5d50; margin: 1.2rem 0 0.3rem; }
    .st-key-listing_card { background: #ffffff; border: 1px solid #e4dfd5; border-radius: 14px;
                           padding: 1.6rem 1.8rem;
                           box-shadow: 0 1px 2px rgba(31, 42, 40, 0.04), 0 8px 24px rgba(31, 42, 40, 0.05); }
    .st-key-listing_card p { line-height: 1.65; color: #1f2a28; }
    .st-key-listing_card p:first-child strong { font-family: 'DM Serif Display', serif; font-weight: 400;
                                                font-size: 1.35rem; line-height: 1.3; }
    .empty-state { border: 1px dashed #d6d0c4; border-radius: 14px; padding: 2.2rem 1.8rem; color: #5f6b67;
                   text-align: center; }
    .empty-state h3 { color: #1f2a28; margin-bottom: 0.4rem; }
    .meta { color: #5f6b67; font-size: 0.85rem; margin: 0.5rem 0 0.8rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

LETRAS_CEE = ["A", "B", "C", "D", "E", "F", "G", "En trámite"]
LONGITUDES = {
    "Corta": "unas 60-80 palabras",
    "Estándar": "entre 80 y 150 palabras",
    "Extensa": "unas 150-220 palabras",
}
IDIOMAS = {"Español": "español", "Català": "catalán", "English": "inglés"}
SEGMENTOS = ["Automático", "Familiar / estándar", "Lujo", "Inversión", "Alquiler estudiantes"]
# Etiquetas de los datos obligatorios que devuelve el skill (CAMPOS_DATOS en skill_engine.py).
ETIQUETAS_DATOS = {
    "operacion": "Operación",
    "ubicacion": "Ubicación",
    "precio": "Precio",
    "superficie": "Superficie",
    "certificado_energetico": "Certificado energético",
    "uso_permitido": "Uso permitido / licencia",
}


# ---------- Utilidades ----------


def texto_plano(markdown: str) -> str:
    return re.sub(r"\*\*(.+?)\*\*", r"\1", markdown)


def contar_palabras(markdown: str) -> int:
    return len(re.findall(r"[\wÀ-ÿ·'’€.,]+", texto_plano(markdown)))


@st.cache_resource(show_spinner=False)
def get_client(api_key: str | None) -> anthropic.Anthropic:
    return anthropic.Anthropic(api_key=api_key) if api_key else anthropic.Anthropic()


def configured_api_key() -> str | None:
    try:
        if "ANTHROPIC_API_KEY" in st.secrets:
            return st.secrets["ANTHROPIC_API_KEY"]
    except Exception:  # no hay secrets.toml
        pass
    return os.environ.get("ANTHROPIC_API_KEY", "").strip() or None


def preferencias(idioma: str, segmento: str, longitud: str) -> list[str]:
    lines = [f"- Idioma del anuncio: {IDIOMAS[idioma]}"]
    if segmento == "Automático":
        lines.append("- Segmento: no indicado (determínalo según el skill)")
    else:
        lines.append(f"- Segmento: {segmento.lower()}")
    lines.append(f"- Longitud: {LONGITUDES[longitud]}")
    return lines


def sobre_version_actual(text: str) -> str:
    """Si se está viendo una versión distinta de la última que redactó el modelo, se la recuerda."""
    actual = st.session_state.get("idioma_actual")
    if actual and actual != st.session_state.get("idioma_modelo"):
        anuncio = st.session_state.versiones[actual]
        return f"Trabaja sobre la versión en {IDIOMAS[actual]}:\n<anuncio>\n{anuncio}\n</anuncio>\n\n{text}"
    return text


def campos_aplicables(datos: dict[str, str]) -> list[str]:
    es_local = "local" in datos.get("tipo_propiedad", "").lower()
    return [c for c in ETIQUETAS_DATOS if c != "uso_permitido" or es_local]


def etiqueta_precio_para(operacion: str) -> str:
    op = operacion.lower()
    if "alquiler" in op:
        return "Renta mensual (€)"
    if "traspaso" in op:
        return "Importe del traspaso (€)"
    return "Precio (€)" if "venta" in op else "Precio o renta (€)"


def mostrar_checklist(datos: dict[str, str]) -> None:
    for campo in campos_aplicables(datos):
        valor = datos.get(campo, "")
        if valor:
            st.markdown(f":green[:material/check_circle:] **{ETIQUETAS_DATOS[campo]}:** {valor}")
        else:
            st.markdown(f":orange[:material/radio_button_unchecked:] **{ETIQUETAS_DATOS[campo]}:** :orange[pendiente]")


def formulario_pendientes(datos: dict[str, str], pendientes: list[str]) -> None:
    """Pide solo los datos obligatorios que faltan y los envía a la misma conversación."""
    with st.form("completar_datos", clear_on_submit=True, border=False):
        valores: dict[str, str | None] = {}
        for campo in pendientes:
            etiqueta = ETIQUETAS_DATOS[campo]
            if campo == "operacion":
                es_local = "local" in datos.get("tipo_propiedad", "").lower()
                opciones = ["Venta", "Alquiler", "Traspaso"] if es_local else ["Venta", "Alquiler"]
                valores[campo] = st.segmented_control(etiqueta, opciones, default=None)
            elif campo == "certificado_energetico":
                valores[campo] = st.segmented_control(etiqueta, LETRAS_CEE, default=None)
            elif campo == "precio":
                valores[campo] = st.text_input(etiqueta_precio_para(datos.get("operacion", "")), placeholder="245000")
            elif campo == "superficie":
                valores[campo] = st.text_input(etiqueta, placeholder="85 m² construidos")
            elif campo == "ubicacion":
                valores[campo] = st.text_input(etiqueta, placeholder="Municipio y zona o barrio")
            else:
                valores[campo] = st.text_input(etiqueta, placeholder="Comercial y hostelería")
        if st.form_submit_button("Completar y generar", type="primary", width="stretch",
                                 icon=":material/edit_note:"):
            rellenos = [f"- {ETIQUETAS_DATOS[c]}: {v.strip()}" for c, v in valores.items() if v and v.strip()]
            if not rellenos:
                st.session_state.error = "Indica al menos uno de los datos pendientes."
            else:
                run("Datos que faltaban:\n" + "\n".join(rellenos), new_session=False)
            st.rerun()


def run(text: str, *, new_session: bool, idioma: str | None = None, traduccion: bool = False) -> None:
    """Envía un mensaje al skill. `idioma` es el idioma en que quedará el anuncio (por defecto, el actual).

    Cada anuncio generado o ajustado reinicia las versiones; una traducción se añade a las existentes.
    """
    client = st.session_state.get("client")
    if client is None:
        st.session_state.error = "Configura la clave de la API en la barra lateral para empezar."
        return
    try:
        if new_session or st.session_state.get("session") is None:
            st.session_state.session = ListingSession(client)
        with st.spinner("Redactando…"):
            reply = st.session_state.session.send(text)
        st.session_state.reply = reply
        st.session_state.error = None
        if not reply.needs_info:
            idioma = idioma or st.session_state.get("idioma_actual") or "Español"
            versiones = st.session_state.get("versiones", {}) if traduccion else {}
            st.session_state.versiones = versiones | {idioma: reply.listing}
            st.session_state.idioma_actual = st.session_state.idioma_modelo = idioma
    except SkillError as exc:
        st.session_state.error = str(exc)
    except anthropic.AuthenticationError:
        st.session_state.error = "La clave de la API no es válida. Revísala en la barra lateral."
    except anthropic.RateLimitError:
        st.session_state.error = "Se ha alcanzado el límite de peticiones. Espera un momento y vuelve a intentarlo."
    except anthropic.APIConnectionError:
        st.session_state.error = "No se ha podido conectar con el servicio. Revisa la conexión a internet."
    except anthropic.APIStatusError as exc:
        st.session_state.error = f"El servicio ha devuelto un error ({exc.status_code}). Inténtalo de nuevo."


# ---------- Barra lateral ----------

with st.sidebar:
    st.markdown("### Preferencias")
    idioma = st.segmented_control("Idioma del anuncio", list(IDIOMAS), default="Español", required=True)
    segmento = st.selectbox(
        "Segmento y tono",
        SEGMENTOS,
        help="En automático, el tono se deduce de los datos. Si no hay un segmento claro, se usa el familiar.",
    )
    longitud = st.segmented_control("Longitud", list(LONGITUDES), default="Estándar", required=True)

    st.divider()
    api_key = configured_api_key()
    if not api_key:
        api_key = st.text_input(
            "Clave de la API de Anthropic",
            type="password",
            help="También se puede configurar en el archivo app/.env (ANTHROPIC_API_KEY).",
        ) or None
    try:
        st.session_state.client = get_client(api_key)
    except anthropic.AnthropicError:
        st.session_state.client = None
    st.caption("Los anuncios siguen las reglas del skill de la agencia: nunca se inventan datos y el precio y el "
               "certificado energético siempre aparecen en el texto.")


# ---------- Cabecera ----------

st.title("Anuncios inmobiliarios")
st.markdown(
    '<p class="app-subtitle">Pega tus notas de la propiedad y obtén un anuncio listo para publicar, '
    "en español, catalán o inglés.</p>",
    unsafe_allow_html=True,
)

col_form, col_result = st.columns([1.15, 1], gap="large")

# ---------- Formulario ----------

with col_form:
    tab_notas, tab_mejorar = st.tabs(["Desde notas", "Mejorar o traducir"])

    with tab_notas:
        st.markdown('<p class="section-label">Lo que tengas de la propiedad</p>', unsafe_allow_html=True)
        notas = st.text_area(
            "Notas, ficha del CRM o apuntes de la visita",
            placeholder="Piso 3 hab 2 baños, 85m2 const., Gràcia (cerca Fontana). Venta 345.000€. "
                        "CEE E 120 kWh. 4ª con ascensor, reformado 2021, balcón a calle, mucha luz…",
            height=260,
        )
        st.caption("Pega el texto tal cual. Se comprueban los datos obligatorios y, si falta alguno, "
                   "solo tendrás que completar ese.")
        if st.button("Generar anuncio", type="primary", width="stretch", icon=":material/edit_note:",
                     key="generar_notas"):
            if not notas.strip():
                st.session_state.error = "Pega las notas o la ficha de la propiedad."
            else:
                lines = ["Genera un anuncio inmobiliario a partir de estas notas del agente:", "",
                         "<notas>", notas.strip(), "</notas>", "", "Preferencias:"]
                run("\n".join(lines + preferencias(idioma, segmento, longitud)), new_session=True, idioma=idioma)

    with tab_mejorar:
        st.markdown('<p class="section-label">Anuncio existente</p>', unsafe_allow_html=True)
        accion = st.segmented_control("¿Qué quieres hacer?", ["Mejorar", "Traducir"], default="Mejorar", required=True)
        original = st.text_area("Pega aquí el anuncio", height=240)
        datos_extra = st.text_area(
            "Datos que no aparecen en el texto (opcional)",
            placeholder="Por ejemplo: certificado energético D, 85m² construidos…",
            height=90,
        )
        st.caption("El idioma de destino, el segmento y la longitud se toman de las preferencias de la barra lateral.")
        if st.button("Procesar anuncio", type="primary", width="stretch", icon=":material/auto_fix_high:"):
            if not original.strip():
                st.session_state.error = "Pega el texto del anuncio que quieres procesar."
            else:
                verbo = "Mejora" if accion == "Mejorar" else f"Traduce al {IDIOMAS[idioma]}"
                lines = [f"{verbo} este anuncio inmobiliario siguiendo el skill. No añadas datos que no estén en el "
                         "texto o en los datos adicionales.", "", "<anuncio>", original.strip(), "</anuncio>"]
                if datos_extra.strip():
                    lines += ["", f"Datos adicionales: {datos_extra.strip()}"]
                lines += ["", "Preferencias:"] + preferencias(idioma, segmento, longitud)
                run("\n".join(lines), new_session=True, idioma=idioma)

# ---------- Resultado ----------

with col_result:
    result_area = st.container()
    reply: SkillReply | None = st.session_state.get("reply")

    if reply is not None:
        placeholder = "Responde a las preguntas…" if reply.needs_info else "Pide un ajuste: más corto, otro titular…"
        follow_up = st.chat_input(placeholder)
        if follow_up:
            run(sobre_version_actual(follow_up), new_session=False)
            reply = st.session_state.get("reply")

    with result_area:
        if st.session_state.get("error"):
            st.error(st.session_state.error, icon=":material/error:")

        if reply is None:
            st.markdown(
                '<div class="empty-state"><h3>Tu anuncio aparecerá aquí</h3>'
                "<p>Pega las notas de la propiedad y pulsa <b>Generar anuncio</b>. "
                "Si falta algún dato obligatorio, el asistente te lo preguntará antes de redactar.</p></div>",
                unsafe_allow_html=True,
            )
        elif reply.needs_info:
            st.markdown("### Faltan algunos datos")
            pendientes = [c for c in campos_aplicables(reply.datos) if not reply.datos.get(c)]
            with st.container(border=True):
                mostrar_checklist(reply.datos)
            if pendientes:
                st.markdown("Completa lo que falta para redactar el anuncio sin inventar nada:")
                formulario_pendientes(reply.datos, pendientes)
                st.caption("También puedes responder en el cuadro de abajo.")
            else:
                st.markdown("Para redactar el anuncio sin inventar nada, necesito que me indiques:")
                for question in reply.questions:
                    st.markdown(f"- {question}")
                st.caption("Escribe la respuesta en el cuadro de abajo.")
        else:
            actual = st.session_state.get("idioma_actual", "Español")
            versiones = st.session_state.get("versiones", {actual: reply.listing})
            listing = versiones[actual]
            st.markdown(f"### Anuncio · {actual}")
            with st.container(key="listing_card"):
                # Un salto de línea simple (p.ej. entre la línea de precio y la llamada a la acción) se respeta.
                st.markdown(re.sub(r"(?<!\n)\n(?!\n)", "  \n", listing))
            st.markdown(f'<p class="meta">{contar_palabras(listing)} palabras</p>', unsafe_allow_html=True)
            with st.container(horizontal=True):
                for otro in (i for i in IDIOMAS if i != actual):
                    ya_hecha = otro in versiones
                    if st.button(otro if ya_hecha else f"Traducir: {otro}", key=f"version_{otro}",
                                 icon=":material/translate:" if not ya_hecha else ":material/visibility:"):
                        if ya_hecha:
                            st.session_state.idioma_actual = otro
                        else:
                            run(sobre_version_actual(
                                f"Traduce el anuncio al {IDIOMAS[otro]}. Mantén los mismos datos y la misma "
                                "estructura: no añadas ni quites información."), new_session=False,
                                idioma=otro, traduccion=True)
                        st.rerun()
            plano = texto_plano(listing)
            st.download_button("Descargar .txt", plano, file_name=f"anuncio-{IDIOMAS[actual]}.txt", width="stretch",
                               icon=":material/download:")
            with st.expander("Copiar texto"):
                st.code(plano, language=None, wrap_lines=True)
            if reply.datos:
                with st.expander("Datos obligatorios usados", icon=":material/checklist:"):
                    mostrar_checklist(reply.datos)

        if reply is not None and reply.notes:
            st.markdown('<p class="section-label">Notas del asistente</p>', unsafe_allow_html=True)
            for note in reply.notes:
                st.info(note, icon=":material/info:")

        if reply is not None:
            if st.button("Empezar de nuevo", width="stretch", icon=":material/restart_alt:"):
                for key in ("reply", "session", "error", "versiones", "idioma_actual", "idioma_modelo"):
                    st.session_state.pop(key, None)
                st.rerun()
