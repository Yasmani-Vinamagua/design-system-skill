#!/usr/bin/env python3
"""Deriva variantes y PNG desde el maestro. Nunca sobrescribe sin --force.

Uso: python export_variants.py logo-master.svg -o logo/ [--color "#fff"] [--sizes 16 32 64 256 512] [--png] [--ico]
Genera: logo-1tinta-negro.svg, logo-1tinta-blanco.svg y, con --png, PNG de cada tamaño (maestro y 1 tinta negro).
Las variantes de color, negativo, horizontal/vertical y reducido requieren decisiones de diseño: no se generan aquí.
"""
import argparse, re, struct, sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import _render

SVG_NS = "http://www.w3.org/2000/svg"


def recolor(src, color):
    ET.register_namespace("", SVG_NS)
    ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")
    root = ET.parse(src).getroot()
    for e in root.iter():
        for k in ("fill", "stroke"):
            v = e.get(k)
            if v and v.lower() not in ("none", "transparent"):
                e.set(k, color)
        if e.tag.endswith("}stop"):
            e.set("stop-color", color)
    if root.get("fill") is None:
        root.set("fill", color)
    return ET.tostring(root, encoding="unicode")


def write(path, text, force, done):
    if path.exists() and not force:
        done.append(f"omitido (existe): {path}")
        return False
    path.write_text(text, encoding="utf-8")
    done.append(f"creado: {path}")
    return True


def build_ico(pngs, dest):
    data = [(p.read_bytes()) for p in pngs]
    head = struct.pack("<HHH", 0, 1, len(data))
    off = 6 + 16 * len(data)
    entries = b""
    for p, d in zip(pngs, data):
        w = int(p.stem.rsplit("-", 1)[-1])
        entries += struct.pack("<BBBBHHII", 0 if w >= 256 else w, 0 if w >= 256 else w, 0, 0, 1, 32, len(d), off)
        off += len(d)
    dest.write_bytes(head + entries + b"".join(data))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("master")
    ap.add_argument("-o", "--out", default=".")
    ap.add_argument("--sizes", nargs="*", type=int, default=[16, 32, 48, 180, 512])
    ap.add_argument("--png", action="store_true")
    ap.add_argument("--ico", action="store_true", help="favicon.ico con 16/32/48 (requiere --png)")
    ap.add_argument("--force", action="store_true")
    a = ap.parse_args()
    master = Path(a.master)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    done = []
    black = out / "logo-1tinta-negro.svg"
    write(black, recolor(master, "#000000"), a.force, done)
    write(out / "logo-1tinta-blanco.svg", recolor(master, "#ffffff"), a.force, done)
    pngs = []
    if a.png:
        renderer = None
        png_dir = out / "png"
        png_dir.mkdir(exist_ok=True)
        for s in a.sizes:
            for label, src in (("logo", master), ("logo-1tinta-negro", black)):
                if not src.exists():
                    continue
                dest = png_dir / f"{label}-{s}.png"
                if dest.exists() and not a.force:
                    done.append(f"omitido (existe): {dest}")
                    pngs.append(dest) if label == "logo" else None
                    continue
                r = _render.svg_to_png(src, dest, s)
                renderer = renderer or r
                done.append(f"creado ({r}): {dest}" if r else f"FALLO sin renderizador: {dest}")
                if r and label == "logo":
                    pngs.append(dest)
        if a.ico:
            ico = [p for p in pngs if int(p.stem.rsplit('-', 1)[-1]) in (16, 32, 48)]
            if ico:
                build_ico(sorted(ico, key=lambda p: int(p.stem.rsplit('-', 1)[-1])), out / "favicon.ico")
                done.append(f"creado: {out / 'favicon.ico'}")
        if renderer is None and not any("omitido" in d for d in done):
            done.append("Sin renderizador (cairosvg, rsvg-convert, inkscape o Chromium): PNG no generados.")
    print("\n".join(done))
    if any(d.startswith(("FALLO", "Sin renderizador")) for d in done):
        sys.exit(2)


if __name__ == "__main__":
    main()
