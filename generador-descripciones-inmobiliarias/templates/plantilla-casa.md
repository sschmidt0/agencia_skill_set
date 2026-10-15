# Plantilla: Casa

Estructura de referencia para generar descripciones de casas (unifamiliares, adosadas, pareadas, chalets). Comparte la lógica base de `plantilla-piso.md` pero incorpora los elementos propios de una vivienda con parcela/exterior.

## Diferencias clave respecto a la plantilla de piso

- El exterior (jardín, parcela, piscina) suele ser el elemento más vendible → se le da más peso en el párrafo de características, no se trata como "extra" menor
- No aplica ascensor/planta — en su lugar interesa el número de plantas de la propia vivienda
- La orientación y el terreno (llano, con desnivel) son más relevantes que en un piso
- Si es adosada o pareada, aclarar cuántas medianeras tiene (afecta a luz y privacidad, dato que el comprador suele preguntar)

## Estructura

1. **Titular** (una línea, gancho comercial)
   - Debe incluir: tipo de vivienda + rasgo más vendible (parcela, piscina, vistas) + zona
   - Ejemplo: "Chalet independiente con piscina y jardín de 400m² en Sant Feliu"

2. **Párrafo de ubicación y entorno** (2-3 frases)
   - Igual que en piso, pero para casas conviene mencionar si es zona residencial/urbanización, acceso en coche, distancia al núcleo urbano
   - Específico si hay datos: "urbanización cerrada con acceso controlado", "a 10 min en coche del centro"

3. **Características de la propiedad** (lista o párrafo)
   - Obligatorias: m² construidos, m² de parcela, habitaciones, baños, número de plantas de la vivienda
   - Opcionales si hay dato: piscina, jardín, garaje/plazas de parking, orientación, año de construcción, estado, tipo de vivienda (independiente/adosada/pareada), medianeras (si aplica), calefacción/aire acondicionado, trastero/bodega

4. **Elemento diferenciador** (1 frase)
   - Vistas, tipo de parcela, piscina propia, reforma reciente, ubicación singular
   - Si no hay dato diferenciador claro, omitir esta sección — no inventar

5. **Cierre con llamada a la acción**
   - Ejemplo: "Ven a conocerla en persona, agenda tu visita" / "Pocas oportunidades así en la zona — contacta para más información"

## Variables a rellenar

| Campo | Obligatorio | Notas |
|---|---|---|
| tipo_vivienda | Sí | independiente, adosada, pareada, chalet... |
| m2_construidos | Sí | — |
| m2_parcela | Sí | diferenciar de m² construidos |
| habitaciones | Sí | — |
| baños | Sí | — |
| plantas_vivienda | Sí | número de plantas de la casa (no confundir con planta de un piso) |
| ubicación | Sí | zona/urbanización + ciudad |
| precio | Sí | — |
| certificado_energético | Sí | letra + consumo (ver normativa-anuncios.md) |
| piscina | No | propia o comunitaria |
| jardín | No | — |
| garaje | No | plazas si se conoce |
| medianeras | No | solo si es adosada/pareada |
| segmento | No | familiar, inversión, lujo → ver reference/tono-por-tipo-propiedad.md |

## Ejemplo completo

**Datos de entrada:**
Chalet independiente, 220m² construidos, parcela 500m², 4 hab, 3 baños, 2 plantas, piscina propia, garaje 2 coches, Sant Cugat del Vallès, 690.000€, cert. energético D, jardín con zona de barbacoa.

**Salida esperada:**

> **Chalet independiente de 4 habitaciones con piscina y jardín en Sant Cugat del Vallès**
>
> Ubicado en una tranquila zona residencial de Sant Cugat, este chalet ofrece la privacidad de una vivienda independiente sin renunciar a la cercanía con el centro y sus servicios.
>
> La casa cuenta con 220m² construidos en 2 plantas, distribuidos en 4 habitaciones y 3 baños, sobre una parcela de 500m². Dispone de piscina propia, jardín con zona de barbacoa y garaje para 2 vehículos.
>
> La combinación de parcela amplia, piscina privada y ubicación residencial la convierte en una opción ideal para quienes buscan espacio y tranquilidad sin alejarse de la ciudad.
>
> Precio: 690.000€ · Certificado energético: D
> Ven a conocerla en persona, agenda tu visita.

## Notas de estilo
- Longitud objetivo: 80-150 palabras (salvo indicación contraria), igual que en piso
- Priorizar en el texto los elementos exteriores (parcela, piscina, jardín) frente a detalles interiores menores — es lo que más pesa en la decisión de compra en este tipo de propiedad
- Certificado energético y precio siempre explícitos, nunca se omiten (ver reference/normativa-anuncios.md)
- Si la parcela es especialmente grande o singular (huerto, arbolado maduro, vistas despejadas), tratarlo como elemento diferenciador propio, no como una característica más de la lista
