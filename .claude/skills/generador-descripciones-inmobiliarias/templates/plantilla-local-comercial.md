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
   - Obligatorias: superficie (m² construidos o útiles, siempre indicando cuál — ver normativa-anuncios.md), diáfano o compartimentado, uso permitido/licencia de actividad, planta (calle, sótano, entresuelo)
   - Opcionales si hay dato: metros lineales de escaparate, altura libre, acceso para carga/descarga, aseos, instalación eléctrica/climatización existente, salida de humos (relevante para hostelería), traspaso o local vacío

4. **Elemento diferenciador** (1 frase)
   - Esquina, doble fachada, escaparate amplio, licencia de actividad ya concedida para un uso específico (ahorra trámites al inquilino), traspaso con clientela activa
   - Un solo rasgo y el beneficio concreto que aporta. No repetir la lista de características del párrafo anterior
   - Describir lo que tiene el local, sin compararlo con otros de la zona salvo que el usuario aporte ese dato
   - Si no hay dato diferenciador claro, omitir esta sección — no inventar

5. **Cierre con llamada a la acción**
   - Ejemplo: "Solicita más información sobre condiciones y disponibilidad" / "Contacta para concertar una visita técnica"
   - No afirmar disponibilidad, plazos ni escasez que el usuario no haya indicado

## Variables a rellenar

| Campo | Obligatorio | Notas |
|---|---|---|
| tipo_operación | Sí | venta, alquiler o traspaso |
| superficie | Sí | m² construidos o útiles (o ambos); si no se especifica, tratar como construidos y avisar al usuario |
| diáfano_o_compartimentado | Sí | — |
| uso_permitido | Sí | según licencia de actividad — no asumir que cualquier uso está permitido |
| planta | Sí | calle, sótano, entresuelo, primera planta... |
| ubicación | Sí | calle/zona + ciudad (la calle puede aparecer; el número no) |
| precio | Sí | venta: precio total · alquiler: renta mensual · traspaso: importe del traspaso; renta mensual recomendada si se conoce (ver normativa-anuncios.md) |
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
> Situado en planta calle y en esquina sobre la calle comercial principal de Sant Feliu de Llobregat.
>
> Cuenta con 90m² construidos, diáfanos, con 12 metros lineales de escaparate que dan visibilidad al negocio desde la calle. Uso permitido: comercial y hostelería.
>
> La salida de humos ya instalada evita esa obra a un negocio de restauración y agiliza su apertura.
>
> Renta: 1.200€/mes · Certificado energético: E
> Solicita más información sobre condiciones y disponibilidad.

## Notas de estilo
- Longitud objetivo: 80-150 palabras, igual que en las otras plantillas
- Evitar lenguaje aspiracional/emocional ("tu negocio soñado") — priorizar datos objetivos que ayuden a evaluar viabilidad
- Ningún rasgo aparece más de dos veces en el texto, titular incluido
- El uso permitido/licencia de actividad nunca se omite ni se asume — si no se proporciona, preguntar antes de generar el anuncio
- Certificado energético y precio (o renta/traspaso) siempre explícitos (ver reference/normativa-anuncios.md)
- Si hay traspaso con clientela o facturación conocida, tratarlo como elemento diferenciador propio — es uno de los datos que más interesa a un comprador de negocio
