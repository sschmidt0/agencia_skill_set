# Ejemplos de descripciones

Ejemplos completos de entrada→salida para los tres tipos de propiedad y distintos segmentos de tono. Sirven como referencia rápida de calibración — si el texto generado se aleja mucho de este registro, revisar `tono-por-tipo-propiedad.md` antes de tocar la lógica del `SKILL.md`.

---

## Piso — segmento familiar/estándar

**Entrada:** Piso, 85m², 3 hab, 2 baños, 4ª planta con ascensor, Sant Feliu de Llobregat (cerca FGC), 245.000€, cert. energético C, reformado en 2022, terraza 8m².

**Salida:**

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

---

## Piso — segmento inversión

**Entrada:** Mismo piso anterior, pero indicando que está actualmente alquilado con contrato en vigor y que el usuario pide enfoque de inversión.

**Salida:**

> **Piso de 3 habitaciones alquilado en zona demandada de Sant Feliu**
>
> Ubicado a 5 minutos a pie de la estación de FGC, en una zona residencial con alta demanda de alquiler por su cercanía al transporte y a servicios básicos.
>
> 85m² distribuidos en 3 habitaciones y 2 baños, 4ª planta con ascensor, reformado en 2022. La propiedad se encuentra actualmente arrendada con contrato en vigor, lo que garantiza ingresos desde el momento de la compra.
>
> Su ubicación junto al transporte público y el estado de conservación reciente la convierten en una opción de bajo mantenimiento para el inversor.
>
> Precio: 245.000€ · Certificado energético: C
> Solicita más información sobre condiciones y rentabilidad actual.

*Nota: obsérvese que no se inventa una cifra de rentabilidad — solo se menciona porque el usuario confirmó que está alquilada.*

---

## Casa — segmento lujo

**Entrada:** Villa independiente, 350m² construidos, parcela 1.200m², 5 hab, 4 baños, 2 plantas, piscina infinity, vistas al mar, Sitges, 1.850.000€, cert. energético B, acabados de diseño (cocina Bulthaup, suelos de mármol).

**Salida:**

> **Villa de diseño con piscina infinity y vistas al mar en Sitges**
>
> Emplazada en una de las zonas más exclusivas de Sitges, esta villa ofrece privacidad absoluta junto a vistas despejadas al mar Mediterráneo, en un entorno donde la naturaleza y el diseño arquitectónico se funden.
>
> Con 350m² construidos sobre una parcela de 1.200m², la vivienda se distribuye en 2 plantas con 5 habitaciones y 4 baños. Los acabados de alta gama — cocina Bulthaup, suelos de mármol — reflejan un cuidado exquisito por el detalle en cada estancia. La piscina infinity corona un exterior pensado para disfrutar del paisaje en cualquier momento del día.
>
> Una propiedad singular donde la calidad de los materiales y la privacidad del entorno la convierten en una oportunidad excepcional.
>
> Precio: 1.850.000€ · Certificado energético: B
> Concierte una visita privada para descubrir esta propiedad exclusiva.

---

## Local comercial — segmento estándar

**Entrada:** Local en alquiler, 90m², diáfano, planta calle, esquina, uso permitido comercial/hostelería, escaparate 12ml, Sant Feliu de Llobregat (calle comercial principal), 1.200€/mes, cert. energético E, con salida de humos.

**Salida:**

> **Local diáfano en esquina con salida de humos en la calle comercial principal de Sant Feliu**
>
> Situado en planta calle sobre una de las vías comerciales de más afluencia de Sant Feliu de Llobregat, este local combina visibilidad y tránsito constante de público, ideal tanto para comercio como para hostelería.
>
> Cuenta con 90m² diáfanos, ubicación en esquina con 12 metros lineales de escaparate y uso permitido comercial/hostelería. Dispone de salida de humos ya instalada, lo que agiliza la puesta en marcha de negocios de restauración.
>
> Su posición en esquina y la doble visibilidad de escaparate lo convierten en un emplazamiento especialmente competitivo para captar clientela de paso.
>
> Renta: 1.200€/mes · Certificado energético: E
> Solicita más información sobre condiciones y disponibilidad.

---

## Ejemplo de caso con datos incompletos (comportamiento esperado)

**Entrada:** Piso, 70m², 2 hab, 1 baño, Sant Feliu de Llobregat, 190.000€. (Falta certificado energético.)

**Comportamiento esperado del skill:** No generar el anuncio. Preguntar explícitamente: "Para generar el anuncio necesito el certificado de eficiencia energética (letra, y consumo si lo tienes) — es un dato obligatorio por normativa. ¿Me lo puedes facilitar?"

*Este caso es clave para verificar que el skill respeta `normativa-anuncios.md` y no rellena huecos con suposiciones.*
