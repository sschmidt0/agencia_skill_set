# Plantilla: Piso

Estructura de referencia para generar descripciones de pisos. Sigue este orden y usa los ejemplos como guía de tono, no para copiar literalmente.

## Estructura

1. **Titular** (una línea, gancho comercial)
   - Debe incluir: tipo de propiedad + rasgo más vendible + zona
   - Ejemplo: "Luminoso piso de 3 habitaciones a un paso del centro de Sant Feliu"

2. **Párrafo de ubicación y entorno** (2-3 frases)
   - Contextualiza el barrio/zona: transporte, servicios cercanos, ambiente
   - Evitar clichés vacíos ("zona muy bien comunicada" sin más). Ser específico si hay datos: "a 5 min a pie de la estación de FGC"

3. **Características de la propiedad** (lista o párrafo, según estilo de la agencia)
   - Obligatorias: m² construidos, habitaciones, baños, planta, ascensor (sí/no)
   - Opcionales si hay dato: orientación, año de construcción, estado (reformado/a reformar/obra nueva), terraza/balcón, trastero, parking, calefacción/aire acondicionado, comunidad (cuota si se conoce)

4. **Elemento diferenciador** (1 frase)
   - Lo que distingue esta propiedad de otras similares en la zona: vistas, luz natural, reforma reciente, edificio con encanto, etc.
   - Si no hay dato diferenciador claro, omitir esta sección — no inventar

5. **Cierre con llamada a la acción**
   - Ejemplo: "Concierta tu visita y descubre tu próximo hogar" / "Disponible para visitas esta semana"

## Variables a rellenar

| Campo | Obligatorio | Notas |
|---|---|---|
| tipo_propiedad | Sí | piso, ático, dúplex, estudio... |
| m2_construidos | Sí | — |
| habitaciones | Sí | — |
| baños | Sí | — |
| planta | Sí | incluir si hay ascensor |
| ubicación | Sí | barrio + ciudad |
| precio | Sí | — |
| certificado_energético | Sí | letra + consumo (ver normativa-anuncios.md) |
| estado_conservación | No | — |
| extras | No | terraza, parking, trastero, piscina comunitaria... |
| segmento | No | familiar, inversión, lujo, estudiantes → afecta al tono, ver reference/tono-por-tipo-propiedad.md |

## Ejemplo completo

**Datos de entrada:**
Piso, 85m², 3 hab, 2 baños, 4ª planta con ascensor, Sant Feliu de Llobregat (cerca FGC), 245.000€, cert. energético C, reformado en 2022, terraza 8m².

**Salida esperada:**

> **Piso reformado de 3 habitaciones con terraza cerca de la FGC en Sant Feliu**
>
> Situado a solo 5 minutos a pie de la estación de FGC, este piso combina la tranquilidad de un barrio residencial con la comodidad de tener el centro de Barcelona a un trayecto corto. La zona cuenta con comercios, colegios y zonas verdes a poca distancia.
>
> La vivienda dispone de 85m² distribuidos en 3 habitaciones y 2 baños, en 4ª planta con ascensor. Reformado en 2022, mantiene un estado impecable con acabados modernos. Cuenta además con una terraza de 8m², ideal para disfrutar del exterior sin salir de casa.
>
> Su luminosidad y la reforma reciente lo convierten en una opción lista para entrar a vivir sin pendientes de obra.
>
> Precio: 245.000€ · Certificado energético: C
> Concierta tu visita y descubre tu próximo hogar.

## Notas de estilo
- Longitud objetivo: 80-150 palabras (salvo indicación contraria)
- Evitar superlativos sin respaldo ("el mejor piso de la zona") — preferir datos concretos
- No usar mayúsculas para enfatizar, ni exceso de exclamaciones
- El certificado energético y el precio siempre van explícitos, nunca se omiten
