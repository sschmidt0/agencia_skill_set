# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

This is a Claude Code **skill set** for a real estate agency. It contains prompt-driven skills (no executable code) that Claude Code loads to handle specific tasks. Currently one skill is implemented.

## Skill: `generador-descripciones-inmobiliarias`

Generates commercial property listings (pisos, casas, locales comerciales) from structured input data. Supports Spanish, Catalan, and English.

### When to activate
When a user provides property data and asks to generate, improve, or translate a listing for sale, rental, or transfer (`traspaso`).

### Mandatory fields before generating (never guess or fill in)
- Certificado de eficiencia energética (CEE) — letter A–G, and kWh/m²/year if available
- Total price (or rent/traspaso amount)
- Surface area — distinguish `m² construidos` vs `m² útiles`; if unspecified, default to `construidos` and say so explicitly
- Operation type: venta / alquiler / traspaso
- Location (zone/neighborhood, exact address not required)

For **locales comerciales**, `uso permitido / licencia de actividad` is equally mandatory.

If any mandatory field is missing: ask explicitly before drafting — never generate with gaps.

### Workflow
1. Extract and validate mandatory fields against `reference/normativa-anuncios.md`
2. Select template by property type:
   - Piso, ático, dúplex, estudio → `templates/plantilla-piso.md`
   - Casa independiente, adosada, pareada, chalet → `templates/plantilla-casa.md`
   - Local comercial → `templates/plantilla-local-comercial.md`
3. Determine tone/segment (see `reference/tono-por-tipo-propiedad.md`):
   - Familiar/estándar (default), Lujo, Inversión, Alquiler estudiantes
   - Load the tone file only when the segment is explicit or clearly deducible
4. Draft following the template structure: titular → ubicación/entorno → características → diferenciador → cierre con CTA
5. For Catalan or English output: load `reference/vocabulario-inmobiliario-es-ca-en.md` and use the correct technical terms (do not translate literally)
6. Calibrate length and tone against `examples/descripciones-ejemplo.md` — target 80–150 words unless the user specifies otherwise

### Key constraints
- Never invent data (price, surface, CEE, permitted use, etc.)
- CEE and price must always appear explicitly in the final text
- Segment/tone adjusts register and emphasis only — it never removes a mandatory field or changes the base template structure
- Avoid superlatives without supporting data; no caps for emphasis; no excessive exclamations
