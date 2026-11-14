#!/usr/bin/env python3
"""Verifica la carpeta de memoria del proyecto `.memory/` (solo lectura, sin red).

Uso: python verificar_memoria.py <carpeta-.memory>
     python verificar_memoria.py --help

Comprueba:
  1. Existen README.md, PROJECT_STATE.md, decisiones.md, lecciones.md y preferencias.md.
  2. PROJECT_STATE.md tiene EXACTAMENTE un encabezado "Para retomar" (ni cero ni dos).
  3. Tamanos: PROJECT_STATE.md hasta 150 lineas; los demas hasta 400.
  4. Cada decision de decisiones.md (encabezado "## D<n>") tiene "Fecha:" y "Estado:" y el estado es uno de
     vigente, provisional o "superada por D<n>".
  5. Cada entrada de lecciones.md (encabezado "## L<n>") tiene "Fecha:".
  6. No hay patrones de secretos (ghp_, github_pat_, sk-, AKIA, -----BEGIN, xox[bp]-).
Sale con 0 sin errores, 1 con errores, 2 si el uso es incorrecto. Solo biblioteca estandar.
"""
import re
import sys
from pathlib import Path

OBLIGATORIOS = ["README.md", "PROJECT_STATE.md", "decisiones.md", "lecciones.md", "preferencias.md"]
SECRETOS = re.compile(r"ghp_[A-Za-z0-9]{6}|github_pat_[A-Za-z0-9]|sk-[A-Za-z0-9]{8}|AKIA[0-9A-Z]{8}|-----BEGIN|xox[bp]-[0-9A-Za-z]")
ESTADO_OK = re.compile(r"^(vigente|provisional|superada por D\d+)\b", re.I)


def secciones(texto, patron):
    """Devuelve [(titulo, cuerpo)] para encabezados '## ...' que cumplen el patron."""
    partes = re.split(r"^##\s+", texto, flags=re.M)[1:]
    out = []
    for p in partes:
        titulo, _, cuerpo = p.partition("\n")
        if re.match(patron, titulo.strip()):
            out.append((titulo.strip(), cuerpo))
    return out


def valor(cuerpo, clave):
    m = re.search(r"^\W*" + clave + r"\W*:\s*(.+)$", cuerpo, re.M | re.I)
    return m.group(1).strip().lstrip("*_` ") if m else None


def main(argv):
    if len(argv) == 2 and argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0
    if len(argv) != 2 or not Path(argv[1]).is_dir():
        print(__doc__)
        return 2
    base = Path(argv[1])
    errores = []
    textos = {}
    for n in OBLIGATORIOS:
        f = base / n
        if not f.is_file():
            errores.append(f"falta {n}")
        else:
            textos[n] = f.read_text(encoding="utf-8", errors="replace")
    for n, t in textos.items():
        lineas = len(t.splitlines())
        tope = 150 if n == "PROJECT_STATE.md" else 400
        if lineas > tope:
            errores.append(f"{n}: {lineas} lineas (maximo {tope}); resumir y mover el detalle a docs/")
        for ln, linea in enumerate(t.splitlines(), 1):
            if SECRETOS.search(linea):
                errores.append(f"{n}:{ln}: posible secreto (nunca va en la memoria)")
    if "PROJECT_STATE.md" in textos:
        n = len(re.findall(r"^#{1,3}\s+Para retomar\b", textos["PROJECT_STATE.md"], re.M | re.I))
        if n != 1:
            errores.append(f"PROJECT_STATE.md: debe haber exactamente un bloque 'Para retomar' (hay {n})")
    if "decisiones.md" in textos:
        for titulo, cuerpo in secciones(textos["decisiones.md"], r"D\d+\b"):
            f, e = valor(cuerpo, "Fecha"), valor(cuerpo, "Estado")
            if not f:
                errores.append(f"decisiones.md: {titulo.split()[0]} sin 'Fecha:'")
            if not e:
                errores.append(f"decisiones.md: {titulo.split()[0]} sin 'Estado:'")
            elif not ESTADO_OK.match(e):
                errores.append(f"decisiones.md: {titulo.split()[0]} con estado invalido '{e}' (vigente, provisional o superada por D<n>)")
    if "lecciones.md" in textos:
        for titulo, cuerpo in secciones(textos["lecciones.md"], r"L\d+\b"):
            if not valor(cuerpo, "Fecha"):
                errores.append(f"lecciones.md: {titulo.split()[0]} sin 'Fecha:'")
    print(f"{len(textos)} archivo(s) revisados en {base}")
    for e in errores:
        print("ERROR:", e)
    print("OK" if not errores else f"{len(errores)} error(es)")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
