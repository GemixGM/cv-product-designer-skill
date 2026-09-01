#!/usr/bin/env python3
"""
Convierte el CV en HTML a PDF con texto seleccionable.

    python3 html_to_pdf.py cv.html cv.pdf [--check]

Usa Chrome/Chromium en modo headless y, si no está, Playwright.
Con --check extrae el texto del PDF resultante y lo imprime: es lo mismo
que verá un ATS. Si sale desordenado o faltan cosas, el CV no está listo.
"""

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

CHROME_PATHS = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
]


def find_chrome():
    for name in ("google-chrome", "chromium", "chromium-browser", "microsoft-edge"):
        path = shutil.which(name)
        if path:
            return path
    for path in CHROME_PATHS:
        if os.path.exists(path):
            return path
    return None


def via_chrome(chrome, html_path, pdf_path):
    with tempfile.TemporaryDirectory() as profile:
        subprocess.run(
            [
                chrome,
                "--headless",
                "--disable-gpu",
                "--no-sandbox",
                f"--user-data-dir={profile}",
                "--no-pdf-header-footer",
                f"--print-to-pdf={pdf_path}",
                html_path.as_uri(),
            ],
            check=True,
            capture_output=True,
            timeout=90,
        )


def via_playwright(html_path, pdf_path):
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(html_path.as_uri(), wait_until="networkidle")
        page.pdf(
            path=str(pdf_path),
            format="A4",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
        browser.close()


def extract_text(pdf_path):
    """Lo que ve el ATS. Devuelve None si no hay ningún extractor disponible."""
    pdftotext = shutil.which("pdftotext")
    if pdftotext:
        try:
            out = subprocess.run(
                [pdftotext, str(pdf_path), "-"],
                check=True, capture_output=True, text=True, timeout=30,
            )
            return out.stdout
        except Exception:
            pass
    try:
        from pypdf import PdfReader
    except ImportError:
        try:
            from PyPDF2 import PdfReader  # type: ignore
        except ImportError:
            return None
    reader = PdfReader(str(pdf_path))
    return "\n".join(page.extract_text() or "" for page in reader.pages)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("html")
    ap.add_argument("pdf", nargs="?")
    ap.add_argument(
        "--check",
        action="store_true",
        help="extrae el texto del PDF para comprobar cómo lo lee un ATS",
    )
    args = ap.parse_args()

    html_path = Path(args.html).expanduser().resolve()
    if not html_path.is_file():
        sys.exit(f"No existe: {html_path}")

    pdf_path = Path(args.pdf).expanduser().resolve() if args.pdf else html_path.with_suffix(".pdf")

    chrome = find_chrome()
    try:
        if chrome:
            via_chrome(chrome, html_path, pdf_path)
        else:
            via_playwright(html_path, pdf_path)
    except Exception as exc:
        if chrome:
            try:
                via_playwright(html_path, pdf_path)
            except Exception:
                sys.exit(f"No se pudo generar el PDF: {exc}")
        else:
            sys.exit(
                f"No se pudo generar el PDF: {exc}\n"
                "Instala Chrome, o Playwright con:  pip install playwright && playwright install chromium"
            )

    if not pdf_path.is_file():
        sys.exit("El PDF no se llegó a escribir.")

    size_kb = pdf_path.stat().st_size / 1024
    print(f"PDF generado: {pdf_path}  ({size_kb:.0f} KB)")

    if args.check:
        text = extract_text(pdf_path)
        if text is None:
            print(
                "\n[--check] No hay extractor de texto instalado.\n"
                "Instala poppler (brew install poppler) o pypdf (pip install pypdf).\n"
                "Comprobación manual: abre el PDF, selecciona todo, copia y pega en\n"
                "un editor de texto plano. Eso es lo que ve el ATS."
            )
        else:
            words = len(text.split())
            print(f"\n{'─' * 60}\nTEXTO EXTRAÍDO — esto es lo que ve el ATS ({words} palabras)\n{'─' * 60}")
            print(text.strip() or "(vacío)")
            print("─" * 60)
            if words < 50:
                print(
                    "AVISO: se ha extraído muy poco texto. Probablemente el PDF sea\n"
                    "una imagen, o el contenido esté dentro de elementos que el parser\n"
                    "no lee. Un ATS lo descartaría."
                )


if __name__ == "__main__":
    main()
