# CV para Product Designers — Skill de Claude Code

Skill que crea, audita, evalúa y adapta CVs de diseño de producto, en español o en inglés, y genera el documento maquetado listo para exportar a PDF.

La idea que la ordena: **un CV de diseño no es un resumen de tu vida laboral, es un tráiler cuyo único trabajo es conseguir que alguien abra tu portfolio.** El portfolio demuestra tu criterio; el CV solo tiene que ganarse el clic.

## Los cuatro modos

| Modo | Cuándo | Qué devuelve |
|---|---|---|
| **Crear** | No hay CV, o el que hay no sirve | Te entrevista, escribe los bullets y monta el documento |
| **Auditar** | Hay un CV y quieres mejorarlo | Informe con los bullets reescritos, no solo señalados |
| **Evaluar encaje** | Hay una oferta y dudas si aplicar | Veredicto por escrito y qué te falta |
| **Adaptar** | Ya has decidido aplicar | El CV ajustado a esa vacante |

No hace falta invocarla por su nombre. Se activa sola con frases como *«revisa mi CV»*, *«¿encajo en esta oferta?»* o *«no me llaman a entrevistas»*.

## Instalación

**Opción rápida** — descarga [`cv-product-designer.skill`](cv-product-designer.skill) y ábrelo en Claude: aparece un botón **Save skill**.

**Opción manual** — descomprime el paquete en tu carpeta de skills:

```bash
unzip cv-product-designer.skill -d ~/.claude/skills/
```

A partir de ahí funciona en cualquier proyecto.

## Requisitos

Solo para generar el PDF: **Chrome** o **Playwright** instalados. Si no tienes ninguno, el CV en HTML se genera igual y puedes imprimirlo a PDF desde el navegador — solo pierdes la comprobación automática de ATS.

Opcional: `poppler` (`brew install poppler`) para que la verificación de ATS lea el texto del PDF automáticamente.

## Qué hace distinto

**Persigue el impacto, no el proceso.** Todo diseñador hace research, wireframes y prototipos. La skill trabaja con una escalera de tres peldaños —tarea → verbo activo → impacto— y la mayoría de guías de CV se quedan en el segundo.

**No inventa métricas.** Nunca. Si no hay números, usa escala, alcance, adopción o lo que dejó de pasar gracias a tu trabajo. Un número inventado se cae en la primera entrevista y arrastra la credibilidad de todo lo demás.

**Sabe decir que no.** El modo de evaluar encaje distingue requisitos eliminatorios de negociables. Si la oferta pide un C1 de inglés y tu CV dice B1, te lo dice — no lo maquilla. Que una oferta no sea para tu CV es el resultado más útil que puede darte: te ahorra semanas.

**Es ATS-safe de verdad.** Columna única, cargo y empresa en el mismo nodo de texto, contacto en el cuerpo del documento. El script incluye un `--check` que extrae el texto del PDF y te enseña exactamente lo que ve un ATS.

**Conoce los mercados.** España, Reino Unido, Estados Unidos y remoto internacional cambian en foto, longitud, datos personales y ortografía. Incluye la tabla de equivalencias académicas ES/UK/US y los falsos amigos que delatan a un hispanohablante en la primera línea.

## Comprobar el PDF antes de enviarlo

```bash
python3 ~/.claude/skills/cv-product-designer/scripts/html_to_pdf.py cv.html cv.pdf --check
```

Lo que imprime es lo que ve un ATS. Si sale desordenado o falta el contacto, el CV no está listo por bien que se vea en pantalla.

## Estructura

```
cv-product-designer/
├── SKILL.md                    Los cuatro modos y las reglas que los gobiernan
├── assets/cv-template.html     Plantilla de columna única
├── scripts/html_to_pdf.py      Generación de PDF y verificación de ATS
└── references/
    ├── bullets.md              Escalera tarea→impacto, verbos de diseño ES/EN
    ├── entrevista.md           Guion por seniority y preguntas de rescate
    ├── auditoria.md            Rúbrica de auditoría en siete pasos
    ├── craft-visual.md         Maquetación y errores frecuentes
    ├── mercados.md             ES/UK/US, equivalencias, falsos amigos
    ├── evaluar-encaje.md       Veredicto, eliminatorios vs. negociables
    └── adaptar-oferta.md       Ajustar a una vacante sin mentir
```

Puedes ver el resultado de la plantilla en [`ejemplo/cv-ejemplo.pdf`](ejemplo/cv-ejemplo.pdf).

## Licencia

MIT. Úsala, modifícala y compártela.

---

Hecha para la comunidad de [tribUX](https://escuelatribux.com).
