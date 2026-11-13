# App de anuncios inmobiliarios

Interfaz web (Streamlit) para que los agentes generen, mejoren o traduzcan anuncios con el skill
`generador-descripciones-inmobiliarias`, sin usar Claude Code.

La app lee el skill directamente de `.claude/skills/generador-descripciones-inmobiliarias/`, así que cualquier
cambio en sus reglas, plantillas o ejemplos se aplica en la app sin tocar el código.

## Puesta en marcha

Requiere Python 3.10 o superior y una clave de la API de Anthropic.

```bash
cd app
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
cp .env.example .env        # y escribe la clave en ANTHROPIC_API_KEY=
.venv/bin/streamlit run app.py
```

La app carga `app/.env` al arrancar (ignorado por git; `.env.example` es la plantilla). Una variable
`ANTHROPIC_API_KEY` ya definida en el entorno tiene prioridad sobre el archivo. Si no hay ninguna clave
configurada, se puede introducir en la barra lateral de la app.

## Cómo funciona

- **Desde notas** (pestaña principal): se pegan las notas de la visita o la ficha del CRM tal cual. El asistente
  extrae los datos obligatorios y los muestra como lista de comprobación; si falta alguno, aparece un formulario
  solo con esos campos ("Completar y generar").
- **Mejorar o traducir**: se pega un anuncio existente y se mejora o se traduce al idioma elegido.
- Si falta algún dato, el asistente pregunta antes de redactar. Las respuestas y los ajustes posteriores
  ("más corto", "otro titular") se escriben en el cuadro de chat bajo el resultado.
- Debajo del anuncio hay botones para traducirlo a los otros dos idiomas. Las traducciones se guardan: volver a una
  versión ya hecha no hace otra llamada. Un ajuste por chat se aplica a la versión que se está viendo y descarta
  las demás.
- Idioma (de la primera versión), segmento/tono y longitud se eligen en la barra lateral. Las fuentes y colores
  están en `.streamlit/config.toml`.

Modelo: `claude-opus-5-5` (en `skill_engine.py`), con respuesta estructurada en JSON para separar el anuncio,
las preguntas, las notas y los datos obligatorios detectados, y caché del prompt de sistema para abaratar las peticiones repetidas.
