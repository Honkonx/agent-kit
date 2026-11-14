#!/usr/bin/env python3
"""Verifica la carpeta de bitacora humana (solo lectura).

Uso: python verificar_bitacora.py <carpeta-bitacora>
     python verificar_bitacora.py --help

Archivos considerados: humano1.md, humano2.md, ... (INDEX.md y otros se ignoran). Comprueba:
  1. Numeracion consecutiva sin saltos, desde 1 (sin tope).
  1b. La fecha va DENTRO de cada archivo: una linea con 'Fecha' en las primeras 12 lineas.
  2. Cada archivo CERRADO tiene de 6 a 9 puntos ("## N. titulo"); el ultimo
     archivo puede estar abierto (1 a 9 puntos). Mas de 9 es error siempre.
  3. Cada punto contiene "Lo que pidió" y "Cómo lo entendí".
  4. No hay patrones de secretos: ghp_, sk-, -----BEGIN.
Sale con 0 si todo bien, 1 si hay errores, 2 si el uso es incorrecto.
Solo biblioteca estandar.
"""
import re
import sys
from pathlib import Path

CABECERA = re.compile(r"^##\s+\d+\.\s", re.MULTILINE)
SECRETOS = re.compile(r"ghp_[A-Za-z0-9]|sk-[A-Za-z0-9]|-----BEGIN")
ARCHIVO = re.compile(r"^humano(\d+)\.md$")


def main(argv):
    if len(argv) == 2 and argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0
    if len(argv) != 2 or not Path(argv[1]).is_dir():
        print(__doc__)
        return 2
    archivos = []
    for f in Path(argv[1]).iterdir():
        m = ARCHIVO.match(f.name)
        if f.is_file() and m:
            archivos.append((int(m.group(1)), f))
    archivos.sort()
    errores = []
    if not archivos:
        errores.append("no hay archivos humano<N>.md (humano1.md, humano2.md, ...)")
    elif archivos[0][0] != 1:
        errores.append("la numeracion debe empezar en humano1.md (empieza en humano%d.md)" % archivos[0][0])
    for i in range(1, len(archivos)):
        if archivos[i][0] != archivos[i - 1][0] + 1:
            errores.append("salto de numeracion: humano%d -> humano%d"
                           % (archivos[i - 1][0], archivos[i][0]))
    for i, (_, f) in enumerate(archivos):
        texto = f.read_text(encoding="utf-8", errors="replace")
        ultimo = i == len(archivos) - 1
        if not any("Fecha" in l for l in texto.splitlines()[:12]):
            errores.append("%s: falta la fecha dentro del archivo (linea '**Fecha:**' al inicio)" % f.name)
        n = len(CABECERA.findall(texto))
        if n > 9:
            errores.append("%s: %d puntos (maximo 9)" % (f.name, n))
        elif n == 0:
            errores.append("%s: sin puntos" % f.name)
        elif n < 6 and not ultimo:
            errores.append("%s: %d puntos en un archivo cerrado (minimo 6)" % (f.name, n))
        for k, t in enumerate(CABECERA.split(texto)[1:], 1):
            if "Lo que pidió" not in t:
                errores.append("%s: punto %d sin 'Lo que pidió'" % (f.name, k))
            if "Cómo lo entendí" not in t:
                errores.append("%s: punto %d sin 'Cómo lo entendí'" % (f.name, k))
        for ln, linea in enumerate(texto.splitlines(), 1):
            if SECRETOS.search(linea):
                errores.append("%s:%d: posible secreto" % (f.name, ln))
    print("%d archivo(s) revisados" % len(archivos))
    for e in errores:
        print("ERROR:", e)
    print("OK" if not errores else "%d error(es)" % len(errores))
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
