# Craft visual del documento

Para un diseñador el CV es una muestra de trabajo antes que un documento informativo. Se le juzga la tipografía, el ritmo y la jerarquía como no se le juzga a nadie más. Al mismo tiempo, es el único artefacto de un diseñador que tiene que sobrevivir a que una máquina lo convierta en texto plano.

Casi todo lo que sigue sale de esa tensión: **cómo maquetar bien sin romper la extracción.**

## La restricción que gobierna el layout

**Columna única.** No es una preferencia estética, es la única restricción de maquetación que se cae del lado del riesgo real.

Evidencia: un CV a dos columnas, con Experiencia a la izquierda y Formación a la derecha, extraído en modo flujo produce esto:

```
Senior Product Designer & Team Lead     ← puesto (columna izq.)
Uxcel                                   ← institución educativa (columna der.)
2020 – 2023 | Timebook Software Inc.    ← fecha del puesto
2024 – Present                          ← fecha de los estudios
```

El parser asocia el cargo con la institución equivocada. Con un extractor que preserva posiciones el CV se salva; con uno que lee el flujo, no. **Un CV a dos columnas depende de la suerte del parser que le toque.** Uno de columna única no depende de nada.

Esto no obliga a hacer un documento pobre. Obliga a que la jerarquía la haga la tipografía y el espacio, que es de todas formas donde se ve el oficio.

## Cargo y empresa deben viajar juntos

Riesgo más sutil y bastante común: cuando cargo y fecha van en una fila flex y la empresa en la línea siguiente, algunos documentos extraen **todos los pares cargo+fecha primero y todas las empresas después**:

```
Senior Product Designer
May 2025 – May 2026
User Experience Lead
Sep 2021 – Sep 2024
...
Nombre de la primera empresa
Nombre de la segunda empresa
```

Visualmente el documento está perfecto; en texto plano nadie puede saber en qué empresa fue cada cargo.

No depende de `break-inside`, ni de `flex: none`, ni de usar `<p>` frente a `<h3>` — probado y descartado. La mitigación fiable es estructural: **poner cargo y empresa en el mismo nodo de texto.**

```html
<div class="role-head">
  <p class="role-title">Senior Product Designer
    <span class="role-org">— Empresa · Freelance · Remoto</span></p>
  <p class="role-dates">May 2025 – May 2026</p>
</div>
```

Sigue permitiendo dos colores y dos pesos en la misma línea, así que no se pierde jerarquía. Comprueba siempre el resultado con `--check`.

## La línea de contexto: el patrón que más rinde

Una línea corta en gris, bajo la empresa, que explica **qué es ese producto**:

> **Senior Product Designer** — Empresa · Freelance · Remoto
> *EdTech SaaS para profesorado.*

Cuesta seis palabras y hace tres cosas a la vez: sitúa a quien lee (no conoce esa empresa), aporta el vocabulario de dominio que busca el ATS, y evita gastar un bullet entero en explicar el contexto. Los bullets quedan libres para lo que importa.

Es especialmente valiosa con empresas poco conocidas, clientes de freelance o mercados extranjeros. Úsala siempre que la empresa no se explique sola.

## La sección de Leadership / Community

Para perfiles con actividad fuera del empleo — docencia, comunidad, divulgación, eventos, open source — conviene una sección propia después de la experiencia de producto:

```
LIDERAZGO, DOCENCIA Y COMUNIDAD
Fundadora · Escuela X · 2021 – Actualidad
Creadora y presentadora · Podcast Y · 2019 – Actualidad
```

Separarla resuelve un problema real: mezclada con la experiencia de producto, esa actividad diluye la trayectoria y confunde la lectura cronológica; eliminada, se pierde una señal fuerte de influencia y de seniority. En su propia sección, suma sin estorbar.

Con formato compacto — una línea de descripción, sin bullets — porque no es el argumento principal.

## Escala y ritmo

Lo que separa un CV que parece diseñado de uno que parece rellenado:

**Ritmo vertical.** Define tres espaciados (entre secciones, entre entradas, entre líneas) y no uses ningún otro. Los saltos arbitrarios son lo primero que delata a una plantilla.

**Jerarquía en tres niveles, no siete.** Nombre / encabezado de sección / cargo. Todo lo demás es texto o metadato. Cada nivel extra que añades resta claridad al escaneo de 7 segundos.

**Contraste por peso y color, no por tamaño.** En un documento de una página no hay espacio para una escala tipográfica amplia. Dos pesos (400 y 600) y dos colores (tinta y acento) bastan para todo.

**Un solo acento.** Y sobrio: un azul o un burdeos profundos leen mejor que un coral saturado, y sobreviven a la impresión en blanco y negro. Si el acento es lo primero que se ve, compite con el contenido.

**Densidad honesta.** Una página densa y bien compuesta gana a dos páginas aireadas. Pero apretar el interlineado por debajo de ~1.4 para que quepa todo es la señal más clara de que sobra contenido, no de que falte espacio.

**Números tabulares** (`font-variant-numeric: tabular-nums`) en las fechas: se alinean solas y el bloque de fechas deja de bailar.

## Errores de maquetación frecuentes

- **Iconos de contacto como imágenes o fuente de iconos.** Se pierden al extraer. Si un icono precede al email y el email es la única forma de contacto, es un riesgo gratuito. Texto plano.
- **URL escondida tras un texto.** Un "LinkedIn" hipervinculado sin URL visible desaparece al imprimir y al extraer. La URL del portfolio se escribe entera y visible.
- **Contacto en el header de página.** Muchos parsers descartan headers y footers. Va en el cuerpo.
- **Muros de skills.** Una lista de 30 términos separados por comas (*Product Design, Product Strategy, Design Strategy, UX, UI, Web Design, Mobile Design…*) no se lee y los ATS actuales puntúan contexto, no densidad. Agrupa por familia, 4-6 por grupo, y quita lo que no discrimina.
- **Párrafos en lugar de bullets.** Un bloque de siete líneas en primera persona no se escanea. Y empezar cada frase por "I" o "Yo" gasta la palabra más visible de la línea en un pronombre.
- **Fechas solapadas sin explicar.** Dos puestos que se pisan generan una duda que nadie va a preguntar: se resuelve con una nota o reordenando.
- **Gris demasiado claro.** El gris de moda para metadatos suele bajar de 4.5:1 y falla en impresión. Los metadatos son secundarios, no invisibles.

## Cuando se pasa de página por poco

Pasa constantemente: el documento se va a una segunda página con tres o cuatro líneas. Es peor que cualquiera de las dos alternativas, porque parece descuido.

Aprieta en este orden, que va de menos a más daño:

1. **Los espaciados**, unos 2pt en cada uno. Es lo único que no se nota.
2. **El margen de página**, de 13mm a 11mm. Por debajo de 11mm empieza a verse ahogado.
3. **El interlineado**, hasta 1.4. Nunca por debajo.
4. **Secciones redundantes.** Si cada empresa ya lleva su línea de contexto, una sección de "Sectores" repite información: fúndela con Idiomas en una sola.
5. **Bloques accesorios a formato de fila.** Formación no necesita la misma estructura que un puesto: una línea por titulación basta.
6. **Una frase del summary.** Suele haber una que repite lo que ya dicen los bullets.

Si tras esto sigue sin caber, el problema no es el espacio: sobra contenido. Recorta los puestos antiguos antes que apretar más la tipografía — un CV ahogado se ve peor que uno corto.

## Comprobación final

```bash
python3 scripts/html_to_pdf.py cv.html cv.pdf --check
```

Lee el texto que sale. Si el orden no es el que esperas, o falta el contacto, o cargo y empresa no se pueden emparejar, el documento no está listo por bien que se vea en pantalla.
