---
name: cv-product-designer
description: Crea, audita, evalúa contra ofertas y adapta CVs de Product Designer / UX / UI / Diseño de Producto, en español o inglés, y genera el documento maquetado en HTML listo para exportar a PDF. Úsala siempre que aparezca un CV, currículum, currículo, resumé o resume en contexto de diseño, producto o UX — tanto si piden escribirlo desde cero, como revisarlo, "darle una vuelta", "hacerlo más fuerte", quitarle paja, traducirlo al inglés, ajustarlo a una oferta concreta, pasar de portfolio a CV, o preparar la candidatura a una vacante de diseño. Actívala también cuando alguien pegue una oferta de empleo de diseño y pregunte si encaja, si cumple los requisitos, si merece la pena aplicar o qué le falta para esa vacante, cuando comparta un PDF o DOCX de su CV para que lo mires, o cuando diga que no le llaman a entrevistas. No hace falta que digan "CV efectivo" ni pidan la skill por su nombre.
---

# CVs de Product Designer

## La idea que ordena todo lo demás

Un CV de diseño no es un documento de identidad ni un resumen de vida laboral: **es un tráiler cuyo único trabajo es conseguir que alguien abra el portfolio.** El portfolio demuestra el criterio; el CV solo tiene que ganarse el clic.

Esto tiene tres consecuencias que gobiernan cada decisión de esta skill:

1. **Se lee en 7 segundos y luego lo parsea una máquina.** Nadie lee un CV: se escanea. Y antes de que lo escanee una persona, un ATS lo convierte a texto plano. Todo lo que no sobreviva a esos dos filtros, sobra.
2. **Los procesos no diferencian; los resultados sí.** Todo diseñador hace research, wireframes y prototipos en Figma. Un CV que enumera eso describe la profesión, no a la persona.
3. **El propio CV es una muestra de trabajo.** A un diseñador se le juzga la tipografía, el ritmo y la jerarquía del documento como no se le juzga a nadie más. Un CV feo de un diseñador es una contradicción visible.

## Elige el modo antes de empezar

| Situación | Modo | Sigue |
|---|---|---|
| No hay CV, o el que hay no sirve | **Crear** | Entrevista → bullets → documento |
| Hay un CV y quieren mejorarlo | **Auditar** | `references/auditoria.md` → reescritura |
| Hay CV + una oferta, y la duda es si aplicar | **Evaluar encaje** | `references/evaluar-encaje.md` |
| Hay CV + una oferta, y ya se ha decidido aplicar | **Adaptar** | `references/adaptar-oferta.md` |

Si no está claro cuál piden, pregunta con una sola frase. Y si te dan un CV existente, **audita antes de reescribir**: entender por qué falla evita cambiar lo que ya funcionaba.

---

## Modo Crear

### 1. Extrae material antes de escribir nada

No redactes con lo que te den de primeras. Nadie describe bien su propio trabajo sin que le pregunten: la gente cuenta lo que *hizo* y se salta lo que *cambió*.

Lee `references/entrevista.md` — trae el guion de preguntas por nivel de seniority y las preguntas de rescate para cuando alguien dice "es que yo no tengo métricas".

Reglas de la entrevista:
- **Por tandas de 3-4 preguntas, no de golpe.** Un cuestionario de 20 preguntas se abandona.
- **Persigue el resultado, no el proceso.** Cuando alguien diga "rediseñé el checkout", la siguiente pregunta siempre es *¿y qué pasó después?*
- **Acepta que a veces no hay número.** Es normal y tiene solución honesta. Lo que nunca se hace es inventarlo (§ Métricas).

### 2. Escribe los bullets

Es el 80% del valor del CV. Lee `references/bullets.md` antes de redactar el primero: trae la escalera tarea → verbo → impacto, el banco de verbos de diseño ES/EN, y la lista de lo que hay que borrar.

El resumen operativo: **cada bullet es una decisión que tomaste y lo que cambió por haberla tomado.** Si el bullet sobreviviría igual en el CV de cualquier otro diseñador de la empresa, no es un bullet, es una descripción del puesto.

### 3. Monta el documento

Estructura por defecto (§ Estructura). Usa `assets/cv-template.html`, genera el PDF con `scripts/html_to_pdf.py` y comprueba que el texto sea seleccionable.

### 4. Valida contra la lista de salida

Antes de entregar, pásale al resultado la checklist de `references/auditoria.md`. Es la misma vara con la que auditas los CVs ajenos: si el tuyo no la pasa, no está terminado.

---

## Estructura del documento

Orden por defecto, de arriba abajo:

```
1. Cabecera        Nombre · Rol · Ciudad, País · Email · Teléfono · PORTFOLIO · LinkedIn
2. Summary         2-3 líneas. Qué eres, en qué contexto, con qué evidencia.
3. Experiencia     Lo más reciente primero. 3-5 bullets por puesto reciente, 1-2 por los antiguos.
4. Proyectos       Opcional. Solo si añade algo que la experiencia no cuenta.
5. Habilidades     Agrupadas y honestas. Sin barritas de nivel.
6. Formación       Al final, salvo junior o cambio de carrera.
7. Idiomas / Extra Solo si es relevante para el puesto.
```

**La URL del portfolio va en la cabecera, siempre, y en texto plano visible** (`tunombre.design`, no un "aquí" hipervinculado). Es la línea más importante del documento: si el ATS se come el enlace o alguien imprime el CV, tiene que seguir siendo legible. Es también el único caso en que repetirla al final está justificado.

**Education va al final** en cuanto hay un año de experiencia real. Solo sube arriba si la persona es junior, viene de un cambio de carrera, o el máster/bootcamp es la credencial más fuerte que tiene ahora mismo.

**Nada de fotos, edad, DNI, estado civil ni dirección postal** por defecto. Ciudad y país bastan. En España la foto es práctica extendida y puede incluirse si la persona lo pide, pero en US, UK, Canadá o Irlanda descalifica por normativa antidiscriminación — ver `references/mercados.md`.

### El summary

Tres líneas como máximo, y va sobre lo que aportas, no sobre lo que buscas. Un "Objective" del tipo *"Busco una posición estable en una empresa consolidada que me permita crecer"* habla del candidato y no dice nada; es un patrón muerto.

La fórmula que funciona: **[rol y años] + [dominio o tipo de producto] + [la evidencia más fuerte que tengas] + [gancho al portfolio si cabe]**.

> Product Designer con 7 años en SaaS B2B, especializada en flujos de datos densos para usuarios expertos. Lideré el design system de una plataforma con 40.000 usuarios activos, adoptado hoy por cinco equipos de producto.

Si el CV se va a adaptar a una oferta concreta, el summary es la primera pieza que se reescribe.

---

## Métricas: qué hacer cuando no las hay

Este es el punto donde más CVs de diseño se rompen, y donde es más fácil hacer daño. Mucha gente honestamente no tiene números: la empresa no medía, los datos son confidenciales, o el impacto se vio dos años después de que se fueran.

**Nunca inventes, estimes ni redondees hacia arriba una métrica.** Un número inventado en un CV se cae en la primera entrevista, y cuando se cae, cae con él todo lo demás. Además pone a la persona en una posición que no eligió.

Cuando no haya números de negocio, hay cuatro alternativas verificables, en orden de fuerza:

**Escala** — el tamaño de lo que tocaste.
> Diseñé la app de reservas usada por 300 hoteles en 8 mercados.

**Alcance y propiedad** — qué eras la única persona en sostener.
> Única diseñadora de un equipo de 12; responsable de discovery, UI y handoff de tres productos en paralelo.

**Adopción** — la prueba de que tu trabajo lo usa alguien más.
> Construí la librería de componentes que hoy usan los 5 equipos de producto de la compañía.

**Decisión y consecuencia** — el resultado no siempre es un KPI; a veces es lo que dejó de pasar.
> Detecté en research que la funcionalidad más pedida no resolvía el problema real; el equipo la descartó y ahorró un trimestre de desarrollo.

Este último tipo es el que mejor señala seniority y casi nadie lo usa. Si alguien "no tiene métricas", pregúntale qué se dejó de hacer gracias a él.

Y si la métrica existe pero es confidencial, se puede expresar en relativo sin romper el NDA: *"reduje a la mitad el tiempo de alta"* en vez del dato absoluto.

---

## ATS: lo que importa de verdad

Hay mucha mitología. Lo que se sostiene hoy:

- **PDF está bien.** El consejo de "usa siempre DOCX" viene de parsers de 2010; desde 2018 los ATS leen PDF sin problema **siempre que el texto sea seleccionable**. Un PDF que es una imagen exportada de Figma es texto invisible: es el error más caro y más frecuente en CVs de diseñadores.
- **Una sola columna.** Un layout a dos columnas hace que el parser lea en horizontal cruzando ambas y produzca texto mezclado e ilegible. Esta es la restricción real, y es la razón de que la plantilla sea de columna única.
- **Cargo y empresa en el mismo nodo de texto.** Si van en líneas separadas, algunos documentos extraen todos los pares cargo+fecha primero y todas las empresas después, y deja de poder saberse qué cargo fue en qué empresa. Ver `references/craft-visual.md`.
- **Sin tablas, cajas de texto ni gráficos** para contenido. Nada de barritas de nivel en habilidades: no dicen nada ("Figma ▓▓▓▓░ 80%" ¿sobre qué escala?) y se parsean como ruido.
- **Contacto en el cuerpo del documento, no en el header/footer** del PDF. Muchos parsers descartan headers.
- **Encabezados de sección estándar**: *Experiencia / Experience*, *Formación / Education*, *Habilidades / Skills*. "Mi trayectoria" o "Lo que sé hacer" quedan bonitos y confunden al parser.
- **Fuentes normales.** Cualquier sans o serif de texto parsea bien. Las display y las script pueden fallar.
- **Nunca keywords ocultas** en blanco sobre blanco: los ATS actuales las revelan al extraer el texto y varios auto-rechazan por ello.

Comprobación honesta antes de entregar: abre el PDF, selecciona todo, copia y pega en un editor de texto plano. Lo que veas es lo que ve el ATS. Si sale desordenado o faltan cosas, el CV no está listo por bonito que se vea.

---

## Modo Auditar

Lee `references/auditoria.md`. Trae la rúbrica completa y el orden en que revisar.

Al dar feedback, sé concreto y reescribe: *"este bullet es débil"* no ayuda a nadie. Muestra el bullet original, la versión mejorada y en una línea por qué cambia. Y reconoce lo que ya está bien — un CV auditado que vuelve todo en rojo desmoraliza y hace que se ignore lo importante.

## Modo Evaluar encaje

Lee `references/evaluar-encaje.md`. Devuelve un **informe por escrito** — veredicto en la primera línea, cobertura requisito a requisito, y qué hacer con cada hueco — y solo al final ofrece tocar el CV. No lo modifica por su cuenta: si reescribes antes de que la persona lea el veredicto, das por hecho que aplicar es buena idea.

Lo que sostiene este modo es la distinción entre **requisito eliminatorio y negociable**. Un nivel de idioma por debajo del pedido, un visado que no se tiene o una diferencia de seis años de experiencia no se compensan con nada del CV; un "deseable" o una herramienta concreta dentro de una categoría que ya se domina, sí.

Contempla también el caso de la oferta que no describe el puesto que anuncia —título de diseño, cuerpo de plantilla genérica—: ahí no se evalúa a ciegas ni se adapta el CV contra requisitos imaginados, se dice y se convierte lo que falta en preguntas para quien publica.

Y hay que decirlo cuando la respuesta es que no. La tentación al leer una oferta es encontrar la manera de que todo encaje —siempre hay algo adyacente que se parece—, pero eso hace que la persona gaste semanas en procesos que iban a terminar en rechazo. **Que una oferta no sea para ese CV es el resultado más útil que puede dar este modo**, y se dice en la primera línea, sin envolverlo. Eso sí: separando el CV de la persona, porque a veces alguien encaja y lo que falla es que el documento no lo demuestra.

## Modo Adaptar

Lee `references/adaptar-oferta.md`. Si aún no se ha decidido aplicar, pasa antes por evaluar encaje. La regla que no se cruza: **adaptar es reordenar, reformular y elegir qué destacar de lo que es cierto. No es añadir experiencia que no existe.** Si la oferta pide algo que la persona no tiene, se dice y se decide qué hacer con ese hueco, no se rellena.

---

## Idioma y mercado

Detecta el idioma por el contexto: la oferta, la empresa, o pregunta. No traduzcas literalmente de un mercado a otro — cambian las convenciones, no solo las palabras.

`references/mercados.md` trae las diferencias España / UK / US / remoto internacional, la tabla de equivalencias académicas ES-UK-US, y los falsos amigos que delatan a un hispanohablante en la primera línea (*formation*, *investigation*, *realize*, *actual*, "*Superior Degree*"...).

---

## Generar el documento

```bash
python3 scripts/html_to_pdf.py cv.html cv.pdf
```

Usa Chrome headless y, si no está, Playwright. `assets/cv-template.html` es columna única, ATS-safe, con las variables de tipografía y color arriba del todo para ajustarlas rápido.

Lee `references/craft-visual.md` para maquetar. En corto: **la contención es la señal de criterio.** Un CV de diseñador se distingue por el ritmo vertical, la jerarquía y el espacio en blanco, no por el color ni por los iconos. Un acento cromático, dos pesos tipográficos y un espaciado impecable comunican más nivel que cualquier adorno. Si el CV parece una plantilla de Canva, resta.

Nombra el archivo `Nombre-Apellido-Product-Designer.pdf`. `cv_final_v3_ok.pdf` es lo primero que ve quien lo recibe.

---

## Ficheros de referencia

Cárgalos cuando los necesites, no todos de golpe:

- `references/bullets.md` — la escalera tarea→verbo→impacto, banco de verbos de diseño ES/EN, palabras a borrar. **Léelo siempre antes de redactar.**
- `references/entrevista.md` — guion de extracción por seniority y preguntas de rescate.
- `references/auditoria.md` — rúbrica de auditoría y checklist de salida.
- `references/mercados.md` — convenciones ES/UK/US, equivalencias académicas, falsos amigos.
- `references/craft-visual.md` — maquetación: columna única, línea de contexto, ritmo, errores frecuentes.
- `references/evaluar-encaje.md` — veredicto de encaje, eliminatorios frente a negociables, idiomas.
- `references/adaptar-oferta.md` — cómo leer una oferta y ajustar sin mentir.

---

Creada por **Gema Gutiérrez Medina** — diseñadora de producto, fundadora de [tribUX](https://escuelatribux.com) y [Píldoras UX](https://pildorasux.com).
Licencia MIT: puedes usarla, adaptarla y compartirla manteniendo la atribución.
