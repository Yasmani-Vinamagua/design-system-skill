#!/usr/bin/env python3
"""Genera una hoja de pruebas del logo (HTML + PNG) para inspeccionarla visualmente.

Uso: python test_sheet.py logo-master.svg [-o carpeta] [--name "Marca"]
Incluye: tamaños reducidos (16–128 px de alto), una tinta negra, blanco sobre negro, color, desenfoque,
giro 90°/180°, espejo y fondos de contraste. Sirve de evidencia visual; el criterio sigue siendo humano.
"""
import argparse, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import _render

SIZES = [16, 24, 32, 48, 64, 128]


def cell(svg, label, size, bg="#fff", fg=None, css=""):
    style = f"height:{size}px;{css}"
    return (f'<figure><div class="box" style="background:{bg};{("color:" + fg) if fg else ""}">'
            f'<div class="logo" style="{style}">{svg}</div></div><figcaption>{label}</figcaption></figure>')


def build(svg, name):
    row = lambda title, items: f'<section><h2>{title}</h2><div class="row">{"".join(items)}</div></section>'
    mono = "filter:brightness(0);"
    white = "filter:brightness(0) invert(1);"
    parts = [
        row("Tamaños reducidos (color)", [cell(svg, f"{s} px", s) for s in SIZES]),
        row("Una tinta negra sobre blanco", [cell(svg, f"{s} px", s, css=mono) for s in (16, 32, 64, 128)]),
        row("Blanco sobre negro (irradiación: ¿parece más pesado?)",
            [cell(svg, f"{s} px", s, bg="#000", css=white) for s in (16, 32, 64, 128)]),
        row("Fondos de contraste", [cell(svg, n, 96, bg=b) for n, b in
            (("blanco", "#fff"), ("gris claro", "#ddd"), ("gris medio", "#888"), ("gris oscuro", "#333"), ("negro", "#000"))]),
        row("Lecturas no intencionadas", [
            cell(svg, "giro 90°", 96, css="transform:rotate(90deg)"),
            cell(svg, "giro 180°", 96, css="transform:rotate(180deg)"),
            cell(svg, "espejo", 96, css="transform:scaleX(-1)"),
            cell(svg, "desenfoque", 96, css="filter:blur(3px)"),
            cell(svg, "silueta", 96, css=mono + "filter:brightness(0) blur(1px);"),
            cell(svg, "escala de grises", 96, css="filter:grayscale(1)")]),
    ]
    return f"""<!doctype html><html lang="es"><meta charset="utf-8"><title>Hoja de pruebas · {name}</title>
<style>body{{font:13px system-ui,sans-serif;margin:24px;background:#f4f4f2;color:#222;width:1000px}}
h1{{font-size:18px;margin:0 0 4px}}p{{margin:0 0 16px;color:#666}}h2{{font-size:13px;margin:18px 0 6px}}
.row{{display:flex;gap:14px;align-items:flex-end;flex-wrap:wrap}}figure{{margin:0;text-align:center}}
.box{{padding:12px;border:1px solid #ccc;display:flex;align-items:center;justify-content:center;min-width:40px}}
.logo svg{{height:100%;width:auto;display:block}}figcaption{{color:#666;font-size:11px;margin-top:4px}}</style>
<h1>Hoja de pruebas: {name}</h1><p>Evidencia visual. No sustituye la revisión: marca cada prueba como verificada, fallida o no verificada.</p>
{"".join(parts)}</html>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("svg")
    ap.add_argument("-o", "--out", default=".")
    ap.add_argument("--name", default=None)
    a = ap.parse_args()
    src = Path(a.svg)
    svg = src.read_text(encoding="utf-8")
    if svg.lstrip().startswith("<?xml"):
        svg = svg[svg.index("?>") + 2:]
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    html = out / "hoja-pruebas.html"
    html.write_text(build(svg, a.name or src.stem), encoding="utf-8")
    print(f"HTML: {html}")
    png = out / "hoja-pruebas.png"
    if _render.html_to_png(html, png, 1060, 1500):
        print(f"PNG:  {png}")
    else:
        print("PNG no generado: no hay Chromium/Chrome/Edge. Abre el HTML en un navegador.", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
