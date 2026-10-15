# Plantilla: Local Comercial

Estructura de referencia para generar descripciones de locales comerciales (venta o alquiler). Comparte la lógica base de las plantillas de piso y casa, pero el enfoque cambia: el comprador/inquilino no busca "vivir", busca que el espacio sea rentable para su negocio.

## Diferencias clave respecto a piso/casa

- El tono es más funcional y orientado a negocio, no emocional/aspiracional — se valoran datos objetivos (afluencia, visibilidad, uso permitido) por encima de adjetivos
- El uso permitido/licencia de actividad es un dato tan crítico como el certificado energético — sin él, el anuncio puede inducir a error
- La ubicación pesa más que en vivienda: afluencia de paso, visibilidad del escaparate, tipo de calle (comercial/residencial) son factores centrales, no complementarios
- No aplican habitaciones/baños en el mismo sentido — en su lugar interesan: diáfano o compartimentado, altura libre, escaparate (metros lineales), acceso para carga/descarga

## Estructura

1. **Titular** (una línea, gancho comercial)
   - Debe incluir: tipo de local + rasgo más relevante para negocio (afluencia, escaparate, esquina) + zona
   - Ejemplo: "Local en esquina con amplio escaparate en zona comercial de Sant Feliu"

2. **Párrafo de ubicación y entorno** (2-3 frases)
   - Enfocado en negocio: tipo de calle, afluencia peatonal/vehicular, comercios vecinos, transporte público si es relevante para clientes o empleados
   - Específico si hay datos: "en calle peatonal con alta afluencia de paso", "junto a parada de metro con más de X mil viajeros/día" (solo si el dato está confirmado, no estimar)

3. **Características del local** (lista o párrafo)
   - Obligatorias: m² totales, diáfano o compartimentado, uso permitido/licencia de actividad, planta (calle, sótano, entresuelo)
   - Opcionales si hay dato: metros lineales de escaparate, altura libre, acceso para carga/descarga, aseos, instalación eléctrica/climatización existente, salida de humos (relevante para hostelería), traspaso o local vacío

4. **Elemento diferenciador** (1 frase)
   - Esquina, doble fachada, escaparate amplio, licencia de actividad ya concedida para un uso específico (ahorra trámites al inquilino), traspaso con clientela activa
   - Si no hay dato diferenciador claro, omitir esta sección — no inventar

5. **Cierre con llamada a la acción**
   - Ejemplo: "Solicita más información sobre condiciones y disponibilidad" / "Contacta para concertar una visita técnica"

## Variables a rellenar

| Campo | Obligatorio | Notas |
|---|---|---|
| tipo_operación | Sí | venta, alquiler o traspaso |
| m2_totales | Sí | — |
| diáfano_o_compartimentado | Sí | — |
| uso_permitido | Sí | según licencia de actividad — no asumir que cualquier uso está permitido |
| planta | Sí | calle, sótano, entresuelo, primera planta... |
| ubicación | Sí | calle/zona + ciudad |
| precio | Sí | venta, renta mensual, o precio de traspaso según tipo_operación |
| certificado_energético | Sí | letra + consumo (ver normativa-anuncios.md) — obligatorio también en locales |
| escaparate_ml | No | metros lineales de escaparate |
| altura_libre | No | relevante para negocios que necesiten almacenaje o instalaciones |
| salida_humos | No | crítico mencionarlo si aplica a hostelería |
| traspaso | No | si aplica, indicar si incluye clientela/facturación conocida |

## Ejemplo completo

**Datos de entrada:**
Local en alquiler, 90m², diáfano, planta calle, esquina, uso permitido: comercial/hostelería, escaparate 12ml, Sant Feliu de Llobregat (calle comercial principal), 1.200€/mes, cert. energético E, con salida de humos instalada.

**Salida esperada:**

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

## Notas de estilo
- Longitud objetivo: 80-150 palabras, igual que en las otras plantillas
- Evitar lenguaje aspiracional/emocional ("tu negocio soñado") — priorizar datos objetivos que ayuden a evaluar viabilidad
- El uso permitido/licencia de actividad nunca se omite ni se asume — si no se proporciona, preguntar antes de generar el anuncio
- Certificado energético y precio (o renta/traspaso) siempre explícitos (ver reference/normativa-anuncios.md)
- Si hay traspaso con clientela o facturación conocida, tratarlo como elemento diferenciador propio — es uno de los datos que más interesa a un comprador de negocio
