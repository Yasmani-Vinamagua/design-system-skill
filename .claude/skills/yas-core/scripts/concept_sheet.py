#!/usr/bin/env python3
"""Genera la vista comparativa de conceptos (concepto/opciones.html + PNG) desde un JSON.

Uso: python concept_sheet.py conceptos.json [-o concepto]
JSON: [{"letra":"A","nombre":"...","idea":"...","traduccion":"...","fortalezas":"...",
        "riesgos":"...","svg":"ruta/al/boceto.svg","recomendado":true}, ...]
"""
import argparse, html, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import _render

E = html.escape


def card(c, base):
    svg = ""
    if c.get("svg"):
        p = Path(c["svg"])
        p = p if p.is_absolute() else base / p
        svg = p.read_text(encoding="utf-8") if p.exists() else "<em>Boceto no encontrado</em>"
        if svg.lstrip().startswith("<?xml"):
            svg = svg[svg.index("?>") + 2:]
    rec = '<span class="rec">Recomendado</span>' if c.get("recomendado") else ""
    rows = "".join(f"<dt>{k}</dt><dd>{E(str(c[f]))}</dd>" for f, k in
                   (("idea", "Idea central"), ("traduccion", "Traducción visual"),
                    ("fortalezas", "Fortalezas"), ("riesgos", "Riesgos")) if c.get(f))
    return (f'<article class="{"is-rec" if c.get("recomendado") else ""}"><h2><b>{E(c["letra"])}</b> '
            f'{E(c["nombre"])} {rec}</h2><div class="art">{svg}</div>'
            f'<p class="note">Boceto de concepto, no es el logo final</p><dl>{rows}</dl></article>')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("json")
    ap.add_argument("-o", "--out", default=".")
    a = ap.parse_args()
    src = Path(a.json)
    items = json.loads(src.read_text(encoding="utf-8"))
    if not 2 <= len(items) <= 4:
        print("Aviso: se esperan 3 conceptos.", file=sys.stderr)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    doc = f"""<!doctype html><html lang="es"><meta charset="utf-8"><title>Opciones de concepto</title>
<style>body{{font:14px system-ui,sans-serif;margin:24px;background:#f4f4f2;color:#222}}
h1{{font-size:20px}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px}}
article{{background:#fff;border:1px solid #ccc;border-radius:8px;padding:16px}}article.is-rec{{border:2px solid #111}}
h2{{font-size:16px;margin:0 0 12px}}h2 b{{display:inline-block;background:#111;color:#fff;border-radius:4px;padding:0 8px;margin-right:6px}}
.rec{{font-size:11px;background:#111;color:#fff;border-radius:10px;padding:2px 8px;vertical-align:middle}}
.art{{height:180px;display:flex;align-items:center;justify-content:center;background:#fafafa;border:1px solid #eee}}
.art svg{{max-width:80%;max-height:160px}}.note{{font-size:11px;color:#777;text-align:center;margin:6px 0 12px}}
dt{{font-weight:600;margin-top:8px}}dd{{margin:2px 0 0;color:#444}}</style>
<h1>Opciones de concepto</h1><div class="grid">{"".join(card(c, src.parent) for c in items)}</div></html>"""
    f = out / "opciones.html"
    f.write_text(doc, encoding="utf-8")
    print(f"HTML: {f}")
    png = out / "opciones.png"
    if _render.html_to_png(f, png, 1100, 760):
        print(f"PNG:  {png}")
    else:
        print("PNG no generado: no hay navegador Chromium.", file=sys.stderr)


if __name__ == "__main__":
    main()
