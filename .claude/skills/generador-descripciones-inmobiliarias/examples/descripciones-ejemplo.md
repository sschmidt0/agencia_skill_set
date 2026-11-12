# Ejemplos de descripciones

Ejemplos completos de entrada→salida para los tres tipos de propiedad, distintos segmentos de tono y los tres idiomas (español, catalán, inglés), más casos con datos incompletos. Sirven como referencia rápida de calibración — si el texto generado se aleja mucho de este registro, revisar `tono-por-tipo-propiedad.md` antes de tocar la lógica del `SKILL.md`.

Regla común a todos los ejemplos: cada afirmación de la salida se apoya en un dato de la entrada. Ningún rasgo se repite más de dos veces (titular incluido): el diferenciador desarrolla un solo rasgo en lugar de volver a enumerar las características. Cuando la entrada no aporta datos del entorno (servicios, ambiente, afluencia), el párrafo de ubicación se mantiene breve en lugar de rellenarse con suposiciones.

---

## Piso — segmento familiar/estándar

**Entrada:** Piso, 85m², 3 hab, 2 baños, 4ª planta con ascensor, Sant Feliu de Llobregat (cerca FGC), 245.000€, cert. energético C, reformado en 2022, terraza 8m².

**Salida:**

> **Piso reformado de 3 habitaciones con terraza cerca de los FGC en Sant Feliu**
>
> Situado en Sant Feliu de Llobregat, cerca de la estación de FGC, este piso permite moverse en transporte público en el día a día sin depender del coche.
>
> La vivienda dispone de 85m² construidos distribuidos en 3 habitaciones y 2 baños, en una 4ª planta con ascensor. Fue reformada en 2022, por lo que está lista para entrar a vivir sin hacer obras.
>
> Su terraza de 8m² añade un espacio exterior propio para aprovechar a diario.
>
> Precio: 245.000€ · Certificado energético: C
> Llámanos o escríbenos para concertar una visita al piso.

*Nota: no se mencionan distancias concretas, luminosidad, calidad de acabados ni servicios del barrio porque no constan en la entrada. La superficie se indica como "construidos" por defecto al no especificarse.*

---

## Piso — segmento inversión

**Entrada:** Mismo piso anterior, pero indicando que está actualmente alquilado con contrato en vigor y que el usuario pide enfoque de inversión.

**Salida:**

> **Piso de 3 habitaciones alquilado con contrato en vigor en Sant Feliu de Llobregat**
>
> Ubicado en Sant Feliu de Llobregat, cerca de la estación de FGC.
>
> 85m² construidos, 3 habitaciones y 2 baños, 4ª planta con ascensor y terraza de 8m². Reformado en 2022.
>
> Se adquiere con inquilino y contrato en vigor, por lo que el inversor incorpora un inmueble que ya está en explotación desde el primer día.
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
> En Sitges, esta villa independiente se asienta sobre una parcela de 1.200m².
>
> Con 350m² construidos repartidos en 2 plantas, la vivienda ofrece 5 habitaciones y 4 baños. Los acabados definen el nivel de la propiedad: cocina Bulthaup y suelos de mármol.
>
> En el exterior, la piscina infinity y las vistas al mar Mediterráneo dan a la parcela su carácter.
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
> Situado en planta calle y en esquina sobre la calle comercial principal de Sant Feliu de Llobregat.
>
> Cuenta con 90m² construidos, diáfanos, con 12 metros lineales de escaparate que dan visibilidad al negocio desde la calle. Uso permitido: comercial y hostelería.
>
> La salida de humos ya instalada evita esa obra a un negocio de restauración y agiliza su apertura.
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
> L'habitatge disposa de 85m² construïts distribuïts en 3 habitacions i 2 banys, en una 4a planta amb ascensor. Es va reformar el 2022, de manera que està llest per entrar-hi a viure sense fer obres.
>
> La seva terrassa de 8m² afegeix un espai exterior propi per aprofitar cada dia.
>
> Preu: 245.000€ · Certificat energètic: C
> Truca'ns o escriu-nos per concertar una visita al pis.

*Nota: se usan los términos de `vocabulario-inmobiliario-es-ca-en.md` ("pis", "metres construïts", "certificat energètic"). No es una traducción palabra por palabra: la redacción se adapta al catalán manteniendo exactamente los mismos datos.*

---

## Casa — en inglés (segmento lujo)

**Entrada:** Mismos datos que la villa de Sitges (segmento lujo), pidiendo el anuncio en inglés.

**Salida:**

> **Detached villa with infinity pool and sea views in Sitges**
>
> In Sitges, this detached villa stands on a 1,200m² plot.
>
> With 350m² of built area over 2 floors, the house offers 5 bedrooms and 4 bathrooms. The finishes set the standard of the property: a Bulthaup kitchen and marble floors.
>
> Outside, the infinity pool and views of the Mediterranean Sea give the plot its character.
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
