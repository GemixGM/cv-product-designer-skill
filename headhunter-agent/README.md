# Headhunter — agente de Claude Code

Agente que hace barridos de ofertas de empleo de diseño de producto recién publicadas, valora el encaje de cada una contra tu CV, y lleva un dashboard semanal de las candidaturas que has enviado (comprobando tu Gmail para ver si te han contestado).

Se dispara solo con frases como *"buenos días head hunter"*, *"dime las ofertas de hoy"* o *"dashboard semanal"*.

## Instalación

Copia `headhunter.md` a `.claude/agents/headhunter.md` en tu proyecto:

```bash
mkdir -p .claude/agents
cp headhunter.md .claude/agents/headhunter.md
```

## Antes de usarlo, ajusta tres cosas

1. **Tu CV**: el agente busca con `Glob` una versión Lead/Senior en una carpeta `cv/` en la raíz del proyecto. Pon ahí tu CV (o cambia la ruta en el prompt).
2. **Gmail (opcional, solo para el dashboard semanal)**: el frontmatter tiene `mcp__<tu-conector-gmail>__...` como placeholder. Sustitúyelo por los nombres reales de las herramientas de **lectura** de tu propio conector de Gmail (`search_threads`, `get_thread`, `get_message`, `list_labels` o sus equivalentes) — nunca le des herramientas de envío, reenvío, etiquetado o borrado. Si no quieres esta función, quita esas cuatro entradas del `tools:` y borra la sección "Dashboard semanal" / "Nunca contestas ni archivas" del prompt.
3. **Filtros de país/región**: el agente viene ajustado a España. Busca "España" en el archivo y cámbialo por tu propio mercado.

## Cómo trabaja con la skill de CV

Cuando detecta que una oferta encaja pero tu CV necesitaría un ajuste, invoca la skill hermana de este repo, [`cv-product-designer`](../cv-product-designer/SKILL.md), en vez de editar el documento él mismo. Instálala también si quieres esta parte del flujo.

## Lo que nunca hace

No aplica por ti. No usa navegador. No contesta ni archiva tu correo. Su trabajo termina en la oferta, el encaje y qué versión de CV usar — el envío real de cualquier candidatura lo haces tú (o tu sesión principal, contigo delante).
