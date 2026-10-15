---
name: generador-descripciones-inmobiliarias
description: Genera descripciones comerciales de propiedades inmobiliarias (pisos, casas, locales comerciales) a partir de datos estructurados. Úsalo cuando el usuario pida redactar, mejorar o traducir un anuncio inmobiliario. Soporta español, catalán e inglés.
version: 1.0.0
---

## Cuándo usar este skill
Actívalo cuando el usuario proporcione datos de una propiedad (aunque sea en bruto o desordenados) y pida generar, mejorar o traducir un anuncio de venta, alquiler o traspaso.

## Flujo de trabajo

1. **Extraer datos obligatorios**: tipo de propiedad, tipo de operación (venta/alquiler/traspaso), superficie, ubicación, precio, certificado energético, y los campos específicos del tipo de propiedad (ver paso 2).
   Verificar contra el checklist de `reference/normativa-anuncios.md`. Si falta algún dato obligatorio, **preguntarlo explícitamente antes de generar el texto** — nunca rellenar huecos con suposiciones.

2. **Elegir plantilla según tipo de propiedad**:
   - Piso, ático, dúplex, estudio → `templates/plantilla-piso.md`
   - Casa independiente, adosada, pareada, chalet → `templates/plantilla-casa.md`
   - Local comercial (venta, alquiler o traspaso) → `templates/plantilla-local-comercial.md`

3. **Determinar el segmento/tono**: si el usuario lo especifica, o se deduce con claridad de los datos (ver criterios en `reference/tono-por-tipo-propiedad.md`), cargar ese archivo y aplicar el registro correspondiente (familiar, lujo, inversión, alquiler estudiantes). Si no hay segmento claro, usar el tono familiar/estándar por defecto sin cargar el archivo.

4. **Redactar** siguiendo la estructura de la plantilla elegida: titular → párrafo de ubicación/entorno → características → elemento diferenciador (si lo hay) → cierre con llamada a la acción.

5. **Si se pide traducción o generación directa en catalán/inglés**, cargar `reference/vocabulario-inmobiliario-es-ca-en.md` y usar la terminología técnica correcta — no traducir literalmente términos como "ático", "trastero" o "zona de mercado tenso".

6. **Antes de entregar el resultado**, contrastar el texto con `examples/descripciones-ejemplo.md` como referencia de calibración de longitud y tono. Si el caso es muy distinto a los ejemplos disponibles, priorizar las reglas explícitas de la plantilla sobre la imitación literal del ejemplo.

## Restricciones importantes

- Nunca inventar datos que no se han proporcionado (superficie, precio, certificado energético, uso permitido en locales, etc.)
- El certificado energético y el precio (o renta/traspaso) son siempre obligatorios y siempre explícitos en el texto final — ver `reference/normativa-anuncios.md`
- En locales comerciales, el uso permitido/licencia de actividad es tan obligatorio como el certificado energético — no asumir que cualquier uso está permitido
- Mantener el texto entre 80-150 palabras salvo que el usuario pida otra longitud
- El segmento/tono ajusta el registro y el énfasis, nunca elimina un campo obligatorio ni cambia la estructura base de la plantilla

## Estructura de archivos del skill

```
generador-descripciones-inmobiliarias/
├── SKILL.md
├── reference/
│   ├── tono-por-tipo-propiedad.md
│   ├── vocabulario-inmobiliario-es-ca-en.md
│   └── normativa-anuncios.md
├── templates/
│   ├── plantilla-piso.md
│   ├── plantilla-casa.md
│   └── plantilla-local-comercial.md
└── examples/
    └── descripciones-ejemplo.md
```
