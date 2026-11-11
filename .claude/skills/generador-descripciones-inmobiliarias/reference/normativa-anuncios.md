# Normativa y campos obligatorios en anuncios inmobiliarios (España)

Este archivo se carga cuando el skill necesita verificar qué información es legalmente obligatoria antes de publicar una descripción. No generar el anuncio final sin estos datos.

## Campos obligatorios en toda publicación

1. **Certificado de eficiencia energética (CEE)**
   - Obligatorio por RD 390/2021. Debe incluir la letra (A-G) y, si está disponible, el consumo en kWh/m² año.
   - Si el usuario no lo proporciona, preguntar explícitamente antes de generar el anuncio. No asumir ni inventar una letra.
   - Excepción: propiedades exentas (obra nueva sin cédula aún, edificios protegidos) — en ese caso indicar "certificado en trámite" en vez de omitirlo.

2. **Precio**
   - Debe indicarse el importe correspondiente al tipo de operación:
     - Venta → precio total
     - Alquiler → renta mensual
     - Traspaso → importe del traspaso. Se recomienda indicar también la renta mensual del local si se conoce (el adquirente asume el contrato de arrendamiento y es un dato clave para evaluar la operación), pero no es obligatorio — no preguntar por ella ni bloquear el anuncio si falta.
   - Si hay gastos adicionales relevantes conocidos (comunidad, IBI) se pueden mencionar, pero no son obligatorios en el anuncio.

3. **Superficie**
   - Es obligatoria una superficie, en m² construidos **o** en m² útiles. Cualquiera de las dos es válida; si el usuario da ambas, incluir las dos en el texto.
   - El texto del anuncio siempre indica de qué tipo es la cifra ("85m² construidos", "70m² útiles") — nunca un número de m² sin calificar.
   - Si el usuario da un número sin especificar el tipo: no bloquear el anuncio por ello. Tratarlo como m² construidos, escribirlo así en el anuncio y avisar al usuario fuera del texto del anuncio (p.ej. "He tomado los 85m² como construidos; si son útiles, dímelo y lo corrijo").
   - Nunca calcular ni estimar una superficie a partir de la otra (p.ej. deducir útiles aplicando un porcentaje a los construidos).
   - En casas, la superficie de parcela es un dato aparte y no sustituye a la superficie de la vivienda.

4. **Identificación del tipo de operación**
   - El anuncio debe dejar claro si es venta, alquiler o traspaso. No debe quedar ambiguo.

5. **Ubicación**
   - No es obligatorio dar la dirección exacta (de hecho, muchas agencias prefieren solo zona/barrio por seguridad y para evitar que el cliente contacte directamente al propietario), pero sí la localidad y zona aproximada.

## Campos obligatorios adicionales en locales comerciales

6. **Uso permitido / licencia de actividad**
   - Indicar qué usos permite la licencia del local (p.ej. comercial, hostelería, oficinas). Es un requisito de este skill, al mismo nivel que el certificado energético: sin este dato el anuncio puede inducir a error al inquilino o comprador sobre la viabilidad de su negocio.
   - Si el usuario no lo proporciona, preguntar explícitamente antes de generar el anuncio. No asumir que cualquier uso está permitido ni deducirlo del uso anterior del local.
   - Si la licencia está en trámite o hay que solicitarla, indicarlo así en el texto en vez de omitirlo.

## Buenas prácticas (no obligatorias legalmente, pero recomendadas)

- **Ley de Propiedad Horizontal / comunidad**: si hay derramas pendientes conocidas y la agencia quiere mencionarlo, incluirlo — mejora la confianza del comprador aunque no sea obligatorio revelarlo en el anuncio.
- **Accesibilidad**: mencionar si el edificio tiene ascensor o es accesible, especialmente relevante en plantas altas.
- **No discriminación**: evitar cualquier lenguaje que pueda interpretarse como discriminatorio respecto a quién puede alquilar/comprar (esto aplica sobre todo a anuncios de alquiler, donde hay más sensibilidad legal en España sobre este punto).

## Variación por comunidad autónoma

Algunas comunidades autónomas (Cataluña, Comunidad Valenciana, entre otras) tienen requisitos adicionales o matices en la regulación de alquileres (p.ej. zonas de mercado tenso, límites de precio de referencia). Este skill no calcula límites de precio ni verifica zonas tensionadas — si la agencia opera en una zona con regulación de precios de alquiler, ese dato debe aportarlo el usuario; el skill no debe asumir que un precio es legal por defecto.

## Checklist antes de generar el anuncio

- [ ] Certificado energético (letra + consumo si está disponible)
- [ ] Precio según operación (venta: precio total · alquiler: renta mensual · traspaso: importe del traspaso; renta mensual recomendada)
- [ ] Superficie (con indicación construidos/útiles)
- [ ] Tipo de operación (venta/alquiler/traspaso) claro
- [ ] Ubicación (zona/barrio, no necesariamente dirección exacta)
- [ ] Solo locales comerciales: uso permitido / licencia de actividad

Si falta alguno de estos puntos, el skill debe preguntar antes de redactar el texto final, no generar el anuncio con huecos o suposiciones.
