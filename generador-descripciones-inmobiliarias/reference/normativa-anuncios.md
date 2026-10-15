# Normativa y campos obligatorios en anuncios inmobiliarios (España)

Este archivo se carga cuando el skill necesita verificar qué información es legalmente obligatoria antes de publicar una descripción. No generar el anuncio final sin estos datos.

## Campos obligatorios en toda publicación

1. **Certificado de eficiencia energética (CEE)**
   - Obligatorio por RD 390/2021. Debe incluir la letra (A-G) y, si está disponible, el consumo en kWh/m² año.
   - Si el usuario no lo proporciona, preguntar explícitamente antes de generar el anuncio. No asumir ni inventar una letra.
   - Excepción: propiedades exentas (obra nueva sin cédula aún, edificios protegidos) — en ese caso indicar "certificado en trámite" en vez de omitirlo.

2. **Precio**
   - Debe indicarse el precio total. Si hay gastos adicionales relevantes conocidos (comunidad, IBI) se pueden mencionar, pero no son obligatorios en el anuncio.

3. **Superficie**
   - Diferenciar si el dato es m² construidos o m² útiles. Si el usuario solo da un número sin especificar, preguntar o indicar "construidos" como valor por defecto y dejarlo explícito en el texto interno (no inventar la distinción).

4. **Identificación del tipo de operación**
   - El anuncio debe dejar claro si es venta o alquiler. No debe quedar ambiguo.

5. **Ubicación**
   - No es obligatorio dar la dirección exacta (de hecho, muchas agencias prefieren solo zona/barrio por seguridad y para evitar que el cliente contacte directamente al propietario), pero sí la localidad y zona aproximada.

## Buenas prácticas (no obligatorias legalmente, pero recomendadas)

- **Ley de Propiedad Horizontal / comunidad**: si hay derramas pendientes conocidas y la agencia quiere mencionarlo, incluirlo — mejora la confianza del comprador aunque no sea obligatorio revelarlo en el anuncio.
- **Accesibilidad**: mencionar si el edificio tiene ascensor o es accesible, especialmente relevante en plantas altas.
- **No discriminación**: evitar cualquier lenguaje que pueda interpretarse como discriminatorio respecto a quién puede alquilar/comprar (esto aplica sobre todo a anuncios de alquiler, donde hay más sensibilidad legal en España sobre este punto).

## Variación por comunidad autónoma

Algunas comunidades autónomas (Cataluña, Comunidad Valenciana, entre otras) tienen requisitos adicionales o matices en la regulación de alquileres (p.ej. zonas de mercado tenso, límites de precio de referencia). Este skill no calcula límites de precio ni verifica zonas tensionadas — si la agencia opera en una zona con regulación de precios de alquiler, ese dato debe aportarlo el usuario; el skill no debe asumir que un precio es legal por defecto.

## Checklist antes de generar el anuncio

- [ ] Certificado energético (letra + consumo si está disponible)
- [ ] Precio total
- [ ] Superficie (con indicación construidos/útiles)
- [ ] Tipo de operación (venta/alquiler) claro
- [ ] Ubicación (zona/barrio, no necesariamente dirección exacta)

Si falta alguno de estos puntos, el skill debe preguntar antes de redactar el texto final, no generar el anuncio con huecos o suposiciones.
