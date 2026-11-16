#!/usr/bin/env python3
"""Audita un SVG de logo: validez, estructura y señales de poca calidad de construcción.

Uso: python svg_audit.py logo-master.svg [--json]
Solo diagnostica. Cada comprobación es OK, AVISO o FALLO; no presenta como superado lo que no mide.
"""
import json, math, re, sys
for _st in (sys.stdout, sys.stderr):
    try:
        _st.reconfigure(encoding="utf-8")
    except Exception:
        pass
import xml.etree.ElementTree as ET

NS = "{http://www.w3.org/2000/svg}"
NUM = re.compile(r"-?\d*\.?\d+(?:[eE][-+]?\d+)?")
CMD = re.compile(r"([MmLlHhVvCcSsQqTtAaZz])([^MmLlHhVvCcSsQqTtAaZz]*)")
ARGS = {"M": 2, "L": 2, "H": 1, "V": 1, "C": 6, "S": 4, "Q": 4, "T": 2, "A": 7, "Z": 0}
GOOD_ANGLES = (0, 15, 30, 45, 60, 75, 90)


def tag(e):
    return e.tag.replace(NS, "")


def path_points(d):
    """Devuelve (nº de anclas, lista de segmentos rectos como pares de puntos absolutos)."""
    x = y = sx = sy = 0.0
    anchors = 0
    lines = []
    for cmd, body in CMD.findall(d):
        nums = [float(n) for n in NUM.findall(body)]
        up = cmd.upper()
        rel = cmd.islower()
        n = ARGS[up]
        if up == "Z":
            if (x, y) != (sx, sy):
                lines.append(((x, y), (sx, sy)))
            x, y = sx, sy
            continue
        for i in range(0, len(nums), n or 1):
            a = nums[i:i + n]
            if len(a) < n:
                break
            if up == "H":
                nx, ny = (x + a[0] if rel else a[0]), y
            elif up == "V":
                nx, ny = x, (y + a[0] if rel else a[0])
            else:
                ex, ey = a[-2], a[-1]
                nx, ny = (x + ex, y + ey) if rel else (ex, ey)
            if up == "M":
                sx, sy = nx, ny
            elif up in ("L", "H", "V"):
                lines.append(((x, y), (nx, ny)))
            anchors += 1
            x, y = nx, ny
    return anchors, lines


def line_angle(p, q):
    dx, dy = q[0] - p[0], q[1] - p[1]
    return math.degrees(math.atan2(abs(dy), abs(dx))), math.hypot(dx, dy)


def audit(path):
    res = []

    def add(name, status, detail):
        res.append({"prueba": name, "estado": status, "detalle": detail})

    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as e:
        add("XML válido", "FALLO", str(e))
        return res
    if tag(root) != "svg":
        add("Raíz svg", "FALLO", f"La raíz es <{tag(root)}>")
        return res
    add("XML válido", "OK", "Se analiza sin errores.")

    vb = root.get("viewBox")
    if not vb:
        add("viewBox", "FALLO", "Falta viewBox; el SVG no escala bien.")
        W = H = None
    else:
        vals = [float(v) for v in NUM.findall(vb)]
        W, H = (vals[2], vals[3]) if len(vals) == 4 else (None, None)
        add("viewBox", "OK", vb)
    if root.get("width") or root.get("height"):
        add("Dimensiones fijas", "AVISO", "El maestro tiene width/height; mejor solo viewBox.")

    els = list(root.iter())
    names = [tag(e) for e in els]
    ids = {e.get("id") for e in els if e.get("id")}

    for bad, why in (("image", "imagen rasterizada incrustada"), ("filter", "filtros (no imprimibles)"),
                     ("style", "bloque <style>; usa atributos fill"), ("script", "script"),
                     ("foreignObject", "foreignObject")):
        if bad in names:
            add(f"Sin <{bad}>", "FALLO", f"Hay {why}.")
    if "text" in names:
        add("Texto", "AVISO", "Hay <text>: depende de una fuente; convierte a trazados para el arte final.")
    for m in ("mask", "clipPath"):
        if m in names:
            add(f"<{m}>", "AVISO", "Evita en el maestro; conviértelo en trazados en los archivos finales.")

    # referencias rotas
    broken = []
    for e in els:
        for v in e.attrib.values():
            for r in re.findall(r"url\(#([^)]+)\)", v):
                if r not in ids:
                    broken.append(r)
        h = e.get("{http://www.w3.org/1999/xlink}href") or e.get("href")
        if h and h.startswith("#") and h[1:] not in ids:
            broken.append(h[1:])
        if h and not h.startswith("#"):
            add("Recurso externo", "FALLO", f"Referencia externa: {h[:60]}")
    add("Referencias internas", "FALLO" if broken else "OK",
        ("Rotas: " + ", ".join(sorted(set(broken)))) if broken else "Sin referencias rotas.")

    if any(e.get("transform") for e in els if e is not root):
        n = sum(1 for e in els if e.get("transform"))
        add("Transformaciones", "AVISO", f"{n} elemento(s) con transform; aplica a las coordenadas si hay anidadas.")

    # colores
    colors = set()
    for e in els:
        for k in ("fill", "stroke"):
            v = e.get(k)
            if v and v.lower() not in ("none", "currentcolor", "transparent") and not v.startswith("url("):
                colors.add(v.lower())
    if "linearGradient" in names or "radialGradient" in names:
        add("Degradados", "AVISO", "Hay degradados; entrega también versión de color sólido.")
    add("Colores planos", "AVISO" if len(colors) > 3 else "OK",
        f"{len(colors)} color(es): {', '.join(sorted(colors)) or '—'} (≤ 3 recomendado).")

    # trazos sin expandir
    strokes = [e for e in els if e.get("stroke") and e.get("stroke").lower() != "none"]
    if strokes:
        add("Trazos", "AVISO", f"{len(strokes)} elemento(s) con stroke; documenta o expande a contornos.")

    # trazados
    total_anchors = 0
    near, tiny, precise = [], 0, 0
    paths = [e for e in els if tag(e) == "path" and e.get("d")]
    for e in paths:
        d = e.get("d")
        precise += len([n for n in NUM.findall(d) if "." in n and len(n.split(".")[1]) > 3])
        if not re.search(r"[Zz]\s*$", d.strip()) and not e.get("stroke") and e.get("fill", "") != "none":
            add("Trazado cerrado", "AVISO", f"Trazado «{e.get('id') or d[:20]}» relleno sin Z final.")
        a, lines = path_points(d)
        total_anchors += a
        for p, q in lines:
            ang, ln = line_angle(p, q)
            if W and ln < max(W, H) / 64 and ln > 0:
                tiny += 1
            if W and ln >= max(W, H) / 32:
                off = min(abs(ang - g) for g in GOOD_ANGLES)
                if 0.3 < off <= 2.0:
                    near.append(f"{ang:.1f}°")
    add("Anclas totales", "AVISO" if total_anchors > 120 else "OK",
        f"{total_anchors} anclas en {len(paths)} trazado(s). Más de ~120 sugiere sobrecomplejidad.")
    add("Ángulos casi enteros", "AVISO" if near else "OK",
        ("Rectas a " + ", ".join(sorted(set(near))) + " (¿45°, 30°, 0°, 90°?).") if near
        else "Sin rectas a 0,3°–2° de un ángulo limpio.")
    add("Microdetalles", "AVISO" if tiny else "OK",
        f"{tiny} segmento(s) < 1/64 del lienzo; desaparecen al reducir." if tiny else "Sin segmentos diminutos.")
    add("Precisión de coordenadas", "AVISO" if precise > 6 else "OK",
        f"{precise} número(s) con más de 3 decimales; redondea a 1–2." if precise > 6 else "Coordenadas limpias.")
    if not any(e.get("id") for e in els if tag(e) == "g"):
        add("Grupos identificables", "AVISO", "Sin <g id=…> (simbolo, nombre, tagline); dificulta los lockups.")
    if root.find(f"{NS}title") is None:
        add("Accesibilidad", "AVISO", "Falta <title> con el nombre de la marca.")
    return res


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    res = audit(sys.argv[1])
    if "--json" in sys.argv:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        for r in res:
            print(f"[{r['estado']:<5}] {r['prueba']}: {r['detalle']}")
        f = sum(r["estado"] == "FALLO" for r in res)
        a = sum(r["estado"] == "AVISO" for r in res)
        print(f"\nResumen: {f} fallo(s), {a} aviso(s). Mide construcción, no calidad de diseño.")
    sys.exit(1 if any(r["estado"] == "FALLO" for r in res) else 0)


if __name__ == "__main__":
    main()
