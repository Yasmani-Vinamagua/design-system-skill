"""Renderizado SVG/HTML a PNG con el primer renderizador disponible (solo biblioteca estándar)."""
import sys as _s
for _st in (_s.stdout, _s.stderr):
    try:
        _st.reconfigure(encoding="utf-8")
    except Exception:
        pass
import os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

CHROMIUM_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
]
CHROMIUM_NAMES = ["google-chrome", "chromium", "chromium-browser", "chrome", "msedge"]


def find_chromium():
    for p in CHROMIUM_CANDIDATES:
        if os.path.exists(p):
            return p
    for n in CHROMIUM_NAMES:
        p = shutil.which(n)
        if p:
            return p
    return None


def available():
    found = []
    try:
        import cairosvg  # noqa: F401
        found.append("cairosvg")
    except Exception:
        pass
    for tool in ("rsvg-convert", "inkscape"):
        if shutil.which(tool):
            found.append(tool)
    if find_chromium():
        found.append("chromium")
    return found


def html_to_png(html_path, png_path, width, height):
    """Captura un HTML con Chromium headless. Devuelve True si el PNG existe."""
    exe = find_chromium()
    if not exe:
        return False
    png_path = str(Path(png_path).resolve())
    profile = tempfile.mkdtemp(prefix="yas-render-")
    try:
        subprocess.run(
            [exe, "--headless=new", "--disable-gpu", "--hide-scrollbars",
             f"--user-data-dir={profile}", f"--window-size={width},{height}",
             "--default-background-color=00000000",
             f"--screenshot={png_path}", Path(html_path).resolve().as_uri()],
            capture_output=True, timeout=60)
    except Exception:
        return False
    finally:
        shutil.rmtree(profile, ignore_errors=True)
    return os.path.exists(png_path)


def svg_to_png(svg_path, png_path, size, transparent=True):
    """Renderiza un SVG a PNG de `size` px de ancho. Devuelve el nombre del renderizador o None."""
    svg_path, png_path = str(svg_path), str(png_path)
    try:
        import cairosvg
        cairosvg.svg2png(url=svg_path, write_to=png_path, output_width=size)
        return "cairosvg"
    except Exception:
        pass
    if shutil.which("rsvg-convert"):
        if subprocess.run(["rsvg-convert", "-w", str(size), "-o", png_path, svg_path],
                          capture_output=True).returncode == 0:
            return "rsvg-convert"
    if shutil.which("inkscape"):
        if subprocess.run(["inkscape", svg_path, "-w", str(size), "-o", png_path],
                          capture_output=True).returncode == 0:
            return "inkscape"
    if find_chromium():
        svg = Path(svg_path).read_text(encoding="utf-8")
        tmp = Path(tempfile.mkdtemp(prefix="yas-svg-")) / "p.html"
        tmp.write_text(
            f"<!doctype html><meta charset=utf-8><style>html,body{{margin:0;background:transparent}}"
            f"svg{{display:block;width:{size}px;height:auto}}</style>{svg}", encoding="utf-8")
        m = re.search(r'viewBox="[-\d.\s,]*?([\d.]+)[\s,]+([\d.]+)"', svg)
        h = max(1, round(size * float(m.group(2)) / float(m.group(1)))) if m else size
        ok = html_to_png(tmp, png_path, size, h)
        shutil.rmtree(tmp.parent, ignore_errors=True)
        if ok:
            return "chromium"
    return None


if __name__ == "__main__":
    print("Renderizadores disponibles:", ", ".join(available()) or "ninguno")
    sys.exit(0)
