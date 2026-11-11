# Ejemplos de descripciones

Ejemplos completos de entrada→salida para los tres tipos de propiedad, distintos segmentos de tono y los tres idiomas (español, catalán, inglés), más casos con datos incompletos. Sirven como referencia rápida de calibración — si el texto generado se aleja mucho de este registro, revisar `tono-por-tipo-propiedad.md` antes de tocar la lógica del `SKILL.md`.

Regla común a todos los ejemplos: cada afirmación de la salida se apoya en un dato de la entrada. Cuando la entrada no aporta datos del entorno (servicios, ambiente, afluencia), el párrafo de ubicación se mantiene breve en lugar de rellenarse con suposiciones.

---

## Piso — segmento familiar/estándar

**Entrada:** Piso, 85m², 3 hab, 2 baños, 4ª planta con ascensor, Sant Feliu de Llobregat (cerca FGC), 245.000€, cert. energético C, reformado en 2022, terraza 8m².

**Salida:**

> **Piso reformado de 3 habitaciones con terraza cerca de los FGC en Sant Feliu**
>
> Situado en Sant Feliu de Llobregat, cerca de la estación de FGC, este piso permite moverse en transporte público en el día a día sin depender del coche.
>
> La vivienda dispone de 85m² construidos distribuidos en 3 habitaciones y 2 baños, en una 4ª planta con ascensor. Fue reformada en 2022, por lo que está lista para entrar a vivir. Cuenta además con una terraza de 8m², un espacio exterior propio para aprovechar a diario.
>
> La reforma reciente, la terraza y el ascensor la convierten en una opción cómoda para instalarse sin necesidad de obras.
>
> Precio: 245.000€ · Certificado energético: C
> Concierta tu visita y descubre tu próximo hogar.

*Nota: no se mencionan distancias concretas, luminosidad, calidad de acabados ni servicios del barrio porque no constan en la entrada. La superficie se indica como "construidos" por defecto al no especificarse.*

---

## Piso — segmento inversión

**Entrada:** Mismo piso anterior, pero indicando que está actualmente alquilado con contrato en vigor y que el usuario pide enfoque de inversión.

**Salida:**

> **Piso de 3 habitaciones alquilado con contrato en vigor en Sant Feliu de Llobregat**
>
> Ubicado en Sant Feliu de Llobregat, cerca de la estación de FGC.
>
> 85m² construidos, 3 habitaciones y 2 baños, 4ª planta con ascensor y terraza de 8m². Reformado en 2022. La vivienda se encuentra actualmente arrendada con contrato en vigor, por lo que se adquiere con inquilino y un contrato de alquiler ya en curso.
>
> Al estar reformado recientemente y alquilado, es una opción para el inversor que busca un inmueble ya en explotación.
>
> Precio: 245.000€ · Certificado energético: C
> Solicita más información sobre las condiciones del contrato actual.

*Nota: no se indica cifra de rentabilidad, demanda de la zona ni se "garantizan" ingresos — solo se menciona el contrato porque el usuario confirmó que está alquilado. Las condiciones concretas (renta, duración) se remiten al contacto.*

---

## Casa — segmento lujo

**Entrada:** Villa independiente, 350m² construidos, parcela 1.200m², 5 hab, 4 baños, 2 plantas, piscina infinity, vistas al mar, Sitges, 1.850.000€, cert. energético B, acabados de diseño (cocina Bulthaup, suelos de mármol).

**Salida:**

> **Villa independiente con piscina infinity y vistas al mar en Sitges**
>
> En Sitges, esta villa independiente se asienta sobre una parcela de 1.200m² con vistas al mar Mediterráneo.
>
> Con 350m² construidos repartidos en 2 plantas, la vivienda ofrece 5 habitaciones y 4 baños. Los acabados definen el nivel de la propiedad: cocina Bulthaup y suelos de mármol. En el exterior, la piscina infinity completa una parcela de amplias dimensiones.
>
> Una propiedad que reúne vistas al mar, piscina infinity y acabados de firma reconocida sobre más de mil metros de parcela.
>
> Precio: 1.850.000€ · Certificado energético: B
> Concierte una visita privada para conocer la propiedad.

*Nota: el registro de lujo se transmite con precisión (marcas, materiales, superficies), no con superlativos. Se evitan "zona más exclusiva", "privacidad absoluta" u "oportunidad excepcional" porque no hay datos que los respalden.*

---

## Local comercial — segmento estándar

**Entrada:** Local en alquiler, 90m², diáfano, planta calle, esquina, uso permitido comercial/hostelería, escaparate 12ml, Sant Feliu de Llobregat (calle comercial principal), 1.200€/mes, cert. energético E, con salida de humos.

**Salida:**

> **Local diáfano en esquina con salida de humos en la calle comercial principal de Sant Feliu**
>
> Situado en planta calle y en esquina sobre la calle comercial principal de Sant Feliu de Llobregat. Su licencia permite tanto uso comercial como de hostelería.
>
> Cuenta con 90m² construidos, diáfanos, y 12 metros lineales de escaparate. Uso permitido: comercial/hostelería. Dispone de salida de humos ya instalada, lo que evita esa obra a negocios de restauración y agiliza su puesta en marcha.
>
> La combinación de esquina, uso hostelero permitido y salida de humos instalada lo hace especialmente adecuado para restauración.
>
> Renta: 1.200€/mes · Certificado energético: E
> Solicita más información sobre condiciones y disponibilidad.

*Nota: no se afirma nivel de afluencia, tránsito de público ni doble escaparate — la entrada solo indica que es la calle comercial principal y que está en esquina. Los 90m² se indican como "construidos" por defecto al no especificarse.*

---

## Piso — en catalán (segmento familiar/estándar)

**Entrada:** Mismos datos que el piso familiar/estándar, pidiendo el anuncio en catalán.

**Salida:**

> **Pis reformat de 3 habitacions amb terrassa a prop dels FGC a Sant Feliu**
>
> Situat a Sant Feliu de Llobregat, a prop de l'estació dels FGC, aquest pis permet moure's en transport públic en el dia a dia sense dependre del cotxe.
>
> L'habitatge disposa de 85m² construïts distribuïts en 3 habitacions i 2 banys, en una 4a planta amb ascensor. Es va reformar el 2022, de manera que està llest per entrar-hi a viure. Compta a més amb una terrassa de 8m², un espai exterior propi per aprofitar cada dia.
>
> La reforma recent, la terrassa i l'ascensor el converteixen en una opció còmoda per instal·lar-s'hi sense necessitat d'obres.
>
> Preu: 245.000€ · Certificat energètic: C
> Concerta la teva visita i descobreix la teva propera llar.

*Nota: se usan los términos de `vocabulario-inmobiliario-es-ca-en.md` ("pis", "metres construïts", "certificat energètic"). No es una traducción palabra por palabra: la redacción se adapta al catalán manteniendo exactamente los mismos datos.*

---

## Casa — en inglés (segmento lujo)

**Entrada:** Mismos datos que la villa de Sitges (segmento lujo), pidiendo el anuncio en inglés.

**Salida:**

> **Detached villa with infinity pool and sea views in Sitges**
>
> In Sitges, this detached villa stands on a 1,200m² plot with views of the Mediterranean Sea.
>
> With 350m² of built area over 2 floors, the house offers 5 bedrooms and 4 bathrooms. The finishes set the standard of the property: a Bulthaup kitchen and marble floors. Outside, the infinity pool completes a generously sized plot.
>
> A property that brings together sea views, an infinity pool and finishes from renowned brands on more than a thousand square metres of land.
>
> Price: €1,850,000 · Energy performance certificate (EPC): B
> Arrange a private viewing to discover the property.

*Nota: términos técnicos según el vocabulario ("detached", "built area", "plot", "EPC"). Las cifras siguen el formato inglés (€1,850,000; 1,200m²). El nombre de la localidad no se traduce.*

---

## Ejemplos de casos con datos incompletos (comportamiento esperado)

Estos casos sirven para verificar que el skill respeta `normativa-anuncios.md` y no rellena huecos con suposiciones. En todos ellos el skill no genera el anuncio: pregunta por el dato que falta (y solo por ese) y espera la respuesta.

### Falta el certificado energético

**Entrada:** Piso, 70m², 2 hab, 1 baño, Sant Feliu de Llobregat, 190.000€.

**Comportamiento esperado del skill:** No generar el anuncio. Preguntar explícitamente: "Para generar el anuncio necesito el certificado de eficiencia energética (letra, y consumo si lo tienes) — es un dato obligatorio por normativa. ¿Me lo puedes facilitar?"

### Falta el precio

**Entrada:** Casa adosada, 180m² construidos, parcela 150m², 4 hab, 2 baños, 3 plantas, Sant Cugat del Vallès, cert. energético D.

**Comportamiento esperado del skill:** No generar el anuncio ni proponer un precio orientativo. Preguntar: "Para generar el anuncio necesito el precio de venta — es un dato obligatorio que debe aparecer en el texto. ¿Cuál es?"

### Falta el uso permitido de un local

**Entrada:** Local en alquiler, 120m² construidos, compartimentado, planta calle, zona centro de Sant Feliu de Llobregat, 1.500€/mes, cert. energético F. Antes era un bar.

**Comportamiento esperado del skill:** No generar el anuncio ni deducir que la licencia permite hostelería porque antes hubiera un bar. Preguntar: "Para generar el anuncio necesito saber qué usos permite la licencia de actividad del local (comercial, hostelería, oficinas…). Que antes fuera un bar no garantiza que la licencia siga vigente para ese uso. ¿Me lo confirmas?"

### Contraejemplo: datos no obligatorios que faltan (sí se genera)

**Entrada:** Traspaso de local, 60m² útiles, diáfano, planta calle, uso permitido comercial, Sant Feliu de Llobregat (zona Mercat), traspaso 25.000€, cert. energético E. No se indica la renta mensual.

**Comportamiento esperado del skill:** Generar el anuncio con el importe del traspaso. La renta mensual es recomendada, no obligatoria: no se pregunta por ella ni se bloquea el anuncio. Como mucho, al entregar el texto se puede sugerir al usuario añadirla si la conoce.
