#!/usr/bin/env python3
"""Comprueba que un mensaje de commit (o de PR) es tecnico y no lleva enlaces, correos ni atribuciones de sesion.

Uso:
  python validar_mensaje_commit.py ARCHIVO            valida el mensaje de un archivo (sirve como hook commit-msg de git)
  python validar_mensaje_commit.py - < mensaje.txt    lo lee de la entrada estandar
  python validar_mensaje_commit.py --log [N]          revisa los ultimos N commits del repositorio actual (por defecto 20); solo informa
  --permitir-coautor    admite una linea `Co-Authored-By: <nombre> <noreply@anthropic.com>` (el unico correo aceptado)
Sale con 0 si no hay problemas y con 1 si los hay. Solo lectura; no modifica el repositorio.
"""
import re
import subprocess
import sys

URL = re.compile(r"https?://|www\.|\b[a-z0-9-]+\.(?:com|ai|io|dev|org|net)/", re.I)
CORREO = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
SESION = re.compile(r"^\s*(Claude-Session|Session|Co-Authored-By:\s*Claude Code Session)\s*:", re.I | re.M)
PUBLICIDAD = re.compile(r"generated with|generado con|made with|🤖|claude\.com|claude\.ai", re.I)
COAUTOR = re.compile(r"^Co-Authored-By:\s*[^<>\n]+<noreply@anthropic\.com>\s*$", re.I | re.M)
MAX_ASUNTO = 72


def problemas(texto, permitir_coautor=False):
    res = []
    lineas = [l for l in texto.splitlines() if not l.startswith("#")]
    cuerpo = "\n".join(lineas).strip()
    if not cuerpo:
        return ["mensaje vacio"]
    asunto = cuerpo.splitlines()[0]
    if len(asunto) > MAX_ASUNTO:
        res.append(f"asunto de {len(asunto)} caracteres (maximo {MAX_ASUNTO})")
    if asunto.rstrip().endswith("."):
        res.append("el asunto no termina en punto")
    if permitir_coautor:
        cuerpo = COAUTOR.sub("", cuerpo)
    if SESION.search(cuerpo):
        res.append("lleva una linea de sesion (Claude-Session u otra): quitarla")
    if URL.search(cuerpo):
        res.append("lleva un enlace (URL): quitarlo")
    if CORREO.search(cuerpo):
        res.append("lleva un correo electronico: quitarlo" + ("" if permitir_coautor else " (o usar --permitir-coautor solo para el noreply de la herramienta)"))
    if PUBLICIDAD.search(cuerpo):
        res.append("lleva texto de atribucion o publicidad de la herramienta (Generated with, robot, marca)")
    return res


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0 if argv else 2
    permitir = "--permitir-coautor" in argv
    args = [a for a in argv if a != "--permitir-coautor"]
    if args and args[0] == "--log":
        n = args[1] if len(args) > 1 else "20"
        try:
            out = subprocess.run(["git", "log", f"-{int(n)}", "--format=%H%x1f%B%x1e"], capture_output=True, text=True, encoding="utf-8", check=True).stdout
        except (subprocess.CalledProcessError, FileNotFoundError, ValueError) as e:
            print("No se pudo leer el historial de git:", e)
            return 2
        malos = 0
        for bloque in out.split("\x1e"):
            if "\x1f" not in bloque:
                continue
            h, msg = bloque.strip().split("\x1f", 1)
            ps = problemas(msg, permitir)
            if ps:
                malos += 1
                print(f"{h[:10]}: " + "; ".join(ps))
        print(f"{malos} commit(s) con problemas entre los ultimos {n}. Solo informe: reescribir el historial exige orden aparte.")
        return 1 if malos else 0
    texto = sys.stdin.read() if args[0] == "-" else open(args[0], encoding="utf-8").read()
    ps = problemas(texto, permitir)
    for p in ps:
        print("ERROR ", p)
    print("OK" if not ps else f"{len(ps)} problema(s).")
    return 1 if ps else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
