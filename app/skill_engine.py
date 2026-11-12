"""Ejecuta el skill generador-descripciones-inmobiliarias a través de la API de Claude.

El contenido del skill (SKILL.md, referencias, plantillas y ejemplos) se lee
directamente de .claude/skills/, así que la app siempre usa la versión actual
del skill sin duplicar sus reglas.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

import anthropic

SKILL_DIR = (
    Path(__file__).resolve().parent.parent
    / ".claude"
    / "skills"
    / "generador-descripciones-inmobiliarias"
)
MODEL = "claude-opus-5-5"

APP_INSTRUCTIONS = """\
Eres el asistente de redacción de anuncios de una agencia inmobiliaria, integrado en una aplicación web.
Sigue el skill `generador-descripciones-inmobiliarias`. Su contenido completo se incluye abajo: cada
archivo va dentro de una etiqueta <archivo ruta="...">. Ya tienes todos los archivos, no hace falta cargarlos.

Los datos llegan desde un formulario (un campo que no aparece significa que el usuario no lo ha indicado) o
como notas libres del agente: apuntes de una visita o una ficha copiada del CRM, a menudo desordenados y con
abreviaturas. En las notas, extrae solo lo que está escrito; lo que no conste se trata como no indicado.

Responde siempre con el formato JSON pedido:
- status "needs_info": falta algún dato obligatorio según el skill. Escribe en `questions` una pregunta
  por cada dato que falta, clara y breve. Deja `listing` vacío.
- status "listing": `listing` contiene solo el texto del anuncio en Markdown, con la estructura de la
  plantilla (titular en negrita, párrafos, línea de precio y certificado energético, llamada a la acción).
  Sin el prefijo de cita ">" de los ejemplos. Deja `questions` vacío.
- `notes`: avisos para el agente que no forman parte del anuncio (supuestos como la superficie tomada
  como construida, datos recomendados que faltan, advertencias de regulación). Una idea por elemento,
  breves. Lista vacía si no hay nada que avisar.
- `datos`: los datos obligatorios del skill tal como constan en toda la conversación hasta ahora, en texto
  breve (p.ej. "venta", "245.000€", "85m² construidos", "E (120 kWh/m² año)", "Gràcia, Barcelona").
  Cadena vacía si el dato no se ha indicado. `uso_permitido` solo aplica a locales comerciales: déjalo
  vacío en el resto. `tipo_propiedad` es informativo (piso, casa adosada, local comercial…).

Las preguntas y las notas van siempre en español, aunque el anuncio esté en catalán o en inglés.
Si el usuario pide cambios sobre un anuncio ya generado, devuelve el anuncio completo actualizado,
respetando igualmente todas las reglas del skill.
"""

# Datos obligatorios de reference/normativa-anuncios.md (más el tipo de propiedad, que decide si aplica el uso
# permitido). Mantener en sincronía con ese archivo.
CAMPOS_DATOS = (
    "tipo_propiedad",
    "operacion",
    "ubicacion",
    "precio",
    "superficie",
    "certificado_energetico",
    "uso_permitido",
)

RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "status": {"type": "string", "enum": ["listing", "needs_info"]},
        "questions": {"type": "array", "items": {"type": "string"}},
        "listing": {"type": "string"},
        "notes": {"type": "array", "items": {"type": "string"}},
        "datos": {
            "type": "object",
            "properties": {campo: {"type": "string"} for campo in CAMPOS_DATOS},
            "required": list(CAMPOS_DATOS),
            "additionalProperties": False,
        },
    },
    "required": ["status", "questions", "listing", "notes", "datos"],
    "additionalProperties": False,
}


class SkillError(Exception):
    """Error que se puede mostrar tal cual al usuario de la app."""


@dataclass
class SkillReply:
    status: str
    listing: str = ""
    questions: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    datos: dict[str, str] = field(default_factory=dict)

    @property
    def needs_info(self) -> bool:
        return self.status == "needs_info"


def build_system_prompt() -> str:
    # SKILL.md primero y el resto en orden fijo, para que el prompt sea estable y se aproveche la caché.
    files = sorted(
        (p for p in SKILL_DIR.rglob("*.md")),
        key=lambda p: (p.name != "SKILL.md", str(p.relative_to(SKILL_DIR))),
    )
    if not files:
        raise SkillError(f"No se encuentra el skill en {SKILL_DIR}")
    parts = [APP_INSTRUCTIONS]
    for path in files:
        rel = path.relative_to(SKILL_DIR).as_posix()
        parts.append(f'<archivo ruta="{rel}">\n{path.read_text(encoding="utf-8")}\n</archivo>')
    return "\n\n".join(parts)


class ListingSession:
    """Una conversación con el skill: el primer mensaje con los datos y las respuestas o ajustes posteriores.

    El historial solo crece (nunca se editan turnos anteriores) y el prompt de sistema se fija al crear
    la sesión, como exige el modelo para conservar el razonamiento entre turnos.
    """

    def __init__(self, client: anthropic.Anthropic):
        self.client = client
        self.system = build_system_prompt()
        self.messages: list[dict] = []

    def send(self, text: str) -> SkillReply:
        self.messages.append({"role": "user", "content": text})
        try:
            response = self.client.beta.messages.create(
                model=MODEL,
                max_tokens=16000,
                betas=["server-side-fallback-2026-07-01"],
                fallbacks="default",
                thinking={"type": "adaptive"},
                output_config={
                    "effort": "medium",
                    "format": {"type": "json_schema", "schema": RESPONSE_SCHEMA},
                },
                system=[
                    {"type": "text", "text": self.system, "cache_control": {"type": "ephemeral"}}
                ],
                messages=self.messages,
            )
        except Exception:
            # El mensaje no obtuvo respuesta: se retira para poder reintentar.
            self.messages.pop()
            raise

        if response.stop_reason == "refusal":
            self.messages.pop()
            raise SkillError("El modelo no ha podido procesar esta petición. Revisa los datos e inténtalo de nuevo.")
        if response.stop_reason == "max_tokens":
            self.messages.pop()
            raise SkillError("La respuesta se ha cortado antes de terminar. Inténtalo de nuevo.")

        self.messages.append({"role": "assistant", "content": response.content})
        text = next((b.text for b in response.content if b.type == "text"), "")
        try:
            data = json.loads(text)
        except json.JSONDecodeError as exc:
            raise SkillError("No se ha podido leer la respuesta del modelo. Inténtalo de nuevo.") from exc
        return SkillReply(
            status=data["status"],
            listing=data["listing"].strip(),
            questions=data["questions"],
            notes=data["notes"],
            datos={k: v.strip() for k, v in data.get("datos", {}).items()},
        )
