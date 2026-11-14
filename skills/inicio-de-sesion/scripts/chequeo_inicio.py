#!/usr/bin/env python3
"""Chequeo de inicio de sesion (solo lectura).

Uso: python chequeo_inicio.py [carpeta]      (por defecto la carpeta actual)
     python chequeo_inicio.py --help

Hace: si la carpeta esta en un repo git, ejecuta `git status --porcelain`,
`git fetch --dry-run` y cuenta commits adelante/atras respecto al remoto;
si no es un repo, lo dice y continua. Busca rutas absolutas con nombre de
usuario (unidad:\\Users\\<x>, /home/<x>, /Users/<x>) en archivos de
configuracion y documentacion de la carpeta. No modifica nada ni imprime
secretos.
Salida: 0 sin alertas, 1 con alertas, 2 si la carpeta no existe.
"""
import re
import subprocess
import sys
from pathlib import Path

EXT = {".json", ".toml", ".yaml", ".yml", ".ini", ".cfg", ".conf", ".env",
       ".md", ".txt", ".bat", ".cmd", ".ps1", ".sh", ".py", ".js", ".ts",
       ".xml", ".properties", ".gradle", ".kts"}
IGNORAR = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist",
           "build", ".gradle"}
MAX_BYTES = 512 * 1024
PATRON = re.compile(
    r"(?:[A-Za-z]:[\\/]+Users[\\/]+(?!Public\b|Default\b|<|%|\{|\$|\*|\.\.)[^\\/\s\"'`<>:*?|]+"
    r"|/home/(?!<|\$|\{|\*)[A-Za-z0-9._-]+"
    r"|/Users/(?!<|\$|\{|\*|Shared\b)[A-Za-z0-9._-]+)")


def git(carpeta, *args):
    try:
        r = subprocess.run(["git", "-C", str(carpeta), *args], capture_output=True,
                           text=True, timeout=60)
        return r.returncode, (r.stdout + r.stderr).strip()
    except (OSError, subprocess.TimeoutExpired) as e:
        return 127, str(e)


def chequeo_git(carpeta):
    alertas = 0
    print("== Estado del repo ==")
    rc, out = git(carpeta, "rev-parse", "--is-inside-work-tree")
    if rc != 0 or out.strip() != "true":
        print("No es un repo git (o git no esta disponible): se omite el chequeo de repo.")
        return 0
    rc, rama = git(carpeta, "branch", "--show-current")
    print(f"Rama: {rama or '(HEAD desprendido)'}")
    rc, out = git(carpeta, "status", "--porcelain")
    lineas = [l for l in out.splitlines() if l.strip()]
    if lineas:
        alertas += 1
        print(f"ALERTA: {len(lineas)} cambio(s) locales sin commit (primeros 10):")
        for l in lineas[:10]:
            print("  " + l)
    else:
        print("Arbol de trabajo limpio.")
    rc, out = git(carpeta, "fetch", "--dry-run")
    if rc != 0:
        alertas += 1
        print(f"ALERTA: fetch --dry-run fallo: {out[:200]}")
    elif out:
        alertas += 1
        print("ALERTA: el remoto tiene novedades (fetch --dry-run):")
        print("  " + out.replace("\n", "\n  ")[:500])
    else:
        print("fetch --dry-run: sin novedades en el remoto.")
    rc, out = git(carpeta, "rev-list", "--left-right", "--count", "@{u}...HEAD")
    if rc == 0 and len(out.split()) == 2:
        atras, adelante = out.split()
        print(f"Respecto al remoto: {adelante} adelante, {atras} atras.")
        if atras != "0":
            alertas += 1
            print("ALERTA: local detras del remoto; si ademas hay commits adelante, "
                  "diverge: parar y entender antes de pull/merge/reset.")
        elif adelante != "0":
            print("Aviso: hay commits locales sin subir.")
    else:
        print("Sin rama remota de seguimiento configurada: no se puede comparar.")
    return alertas


def buscar_rutas(carpeta):
    print("== Rutas de usuario hardcodeadas ==")
    hallazgos = []
    for p in carpeta.rglob("*"):
        if any(parte in IGNORAR for parte in p.relative_to(carpeta).parts):
            continue
        if not p.is_file() or (p.suffix.lower() not in EXT and p.name != ".env"):
            continue
        try:
            if p.stat().st_size > MAX_BYTES:
                continue
            texto = p.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for n, linea in enumerate(texto.splitlines(), 1):
            m = PATRON.search(linea)
            if m:
                hallazgos.append((p.relative_to(carpeta), n, m.group(0)))
    for ruta, n, frag in hallazgos[:50]:
        print(f"  {ruta}:{n}: {frag}")
    if hallazgos:
        print(f"ALERTA: {len(hallazgos)} ruta(s) con usuario. Sustituir por variable de "
              "entorno o ruta relativa (ignorar falsos positivos que sean ejemplos).")
        return 1
    print("Sin rutas de usuario detectadas.")
    return 0


def main(argv):
    if any(a in ("-h", "--help") for a in argv):
        print(__doc__)
        return 0
    carpeta = Path(argv[0] if argv else ".").resolve()
    if not carpeta.is_dir():
        print(f"No existe la carpeta: {carpeta}")
        return 2
    alertas = chequeo_git(carpeta) + buscar_rutas(carpeta)
    print("== Resultado ==")
    print("Sin alertas." if not alertas else f"{alertas} alerta(s): revisar antes de trabajar.")
    print("Recordatorio: leer la ultima bitacora y el estado para retomar.")
    return 1 if alertas else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
