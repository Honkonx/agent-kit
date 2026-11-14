#!/usr/bin/env python3
"""Corre las comprobaciones que el PROYECTO define y muestra un tablero pass/fail (sin red propia, solo biblioteca estandar).

Uso: python tablero_estado.py <estado-del-proyecto.json> [--sin-git] [--json]
     python tablero_estado.py --help

El archivo de configuracion es del proyecto (no de este kit):
  {"comprobaciones": [
      {"nombre": "Lint",  "comando": ["pnpm", "run", "lint"], "tiempo_max": 120},
      {"nombre": "Tipos", "comando": "mypy src", "tiempo_max": 300},
      {"nombre": "Pruebas", "comando": ["python", "-m", "unittest"], "cwd": "."},
      {"nombre": "Auditoria de dependencias", "comando": ""}  <- comando vacio = OMITIDA (no configurada)
  ]}
`comando` puede ser una lista (recomendado) o un texto; se ejecuta SIN shell. `cwd` es relativo al archivo de configuracion.
Estados: PASA (codigo 0), FALLA (codigo distinto de 0, o expira `tiempo_max`, por defecto 300 s), OMITIDA (sin comando).
Resumen general: "todas pasan", "hay fallos" u "sin comprobaciones configuradas". Ademas muestra rama, adelante/atras y cambios
locales si hay git (se omite con --sin-git). Sale con 0 si ninguna comprobacion FALLA, 1 si alguna falla, 2 si el uso es incorrecto.
Seguridad: ejecuta solo lo que el proyecto escribio en su configuracion; se niega si el archivo esta dentro de una carpeta llamada
`referencias` (clones ajenos, no confiables). No imprime el entorno ni guarda salidas completas (solo la ultima linea).
Idea inspirada en la skill "status" de claude-code-agent-scaffold (Apache-2.0); implementacion propia.
"""
import json
import os
import shlex
import subprocess
import sys
import time
from pathlib import Path

MAX_LINEA = 140


def partir(comando):
    if isinstance(comando, list):
        return [str(x) for x in comando]
    return shlex.split(comando, posix=(os.name != "nt"))


def ultima_linea(salida):
    lineas = [l.strip() for l in salida.splitlines() if l.strip()]
    return (lineas[-1] if lineas else "")[:MAX_LINEA]


def correr(c, base):
    comando = c.get("comando", "")
    if not comando:
        return {"nombre": c["nombre"], "estado": "OMITIDA", "segundos": 0.0, "detalle": "no configurada"}
    cwd = (base / c["cwd"]).resolve() if c.get("cwd") else base
    inicio = time.time()
    try:
        r = subprocess.run(partir(comando), cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace",
                           timeout=float(c.get("tiempo_max", 300)))
        estado = "PASA" if r.returncode == 0 else "FALLA"
        detalle = ultima_linea(r.stdout + "\n" + r.stderr) or f"codigo {r.returncode}"
    except subprocess.TimeoutExpired:
        estado, detalle = "FALLA", f"expiro tras {c.get('tiempo_max', 300)} s"
    except (OSError, ValueError) as e:
        estado, detalle = "FALLA", f"no se pudo ejecutar: {type(e).__name__}"
    return {"nombre": c["nombre"], "estado": estado, "segundos": round(time.time() - inicio, 1), "detalle": detalle}


def git(base, *args):
    try:
        r = subprocess.run(["git", *args], cwd=base, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=30)
        return r.stdout.strip() if r.returncode == 0 else None
    except (OSError, subprocess.TimeoutExpired):
        return None


def estado_git(base):
    if git(base, "rev-parse", "--is-inside-work-tree") != "true":
        return None
    rama = git(base, "branch", "--show-current") or "(sin rama)"
    cambios = git(base, "status", "--porcelain") or ""
    modif = sum(1 for l in cambios.splitlines() if not l.startswith("??"))
    nuevos = sum(1 for l in cambios.splitlines() if l.startswith("??"))
    cuenta = git(base, "rev-list", "--left-right", "--count", "@{upstream}...HEAD")
    if cuenta:
        atras, adelante = cuenta.split()
        sincro = f"{adelante} adelante / {atras} atras"
    else:
        sincro = "sin remoto configurado"
    return {"rama": rama, "sincronizacion": sincro, "modificados": modif, "sin_seguimiento": nuevos}


def main(argv):
    if not argv or any(a in ("-h", "--help") for a in argv):
        print(__doc__)
        return 0 if argv else 2
    con_git = "--sin-git" not in argv
    salida_json = "--json" in argv
    rutas = [a for a in argv if not a.startswith("--")]
    if len(rutas) != 1 or not Path(rutas[0]).is_file():
        print(__doc__)
        return 2
    cfg = Path(rutas[0]).resolve()
    if "referencias" in {p.lower() for p in cfg.parts}:
        print("Me niego: el archivo de configuracion esta dentro de una carpeta 'referencias' (material ajeno, no confiable).")
        return 2
    try:
        datos = json.loads(cfg.read_text(encoding="utf-8"))
        comprobaciones = datos.get("comprobaciones", [])
        assert all(isinstance(c, dict) and c.get("nombre") for c in comprobaciones)
    except (ValueError, AssertionError, OSError):
        print("Configuracion invalida: se espera {\"comprobaciones\": [{\"nombre\": ..., \"comando\": ...}]}")
        return 2
    base = cfg.parent
    resultados = [correr(c, base) for c in comprobaciones]
    hay_fallos = any(r["estado"] == "FALLA" for r in resultados)
    if not [r for r in resultados if r["estado"] != "OMITIDA"]:
        resumen = "sin comprobaciones configuradas"
    else:
        resumen = "hay fallos" if hay_fallos else "todas pasan"
    g = estado_git(base) if con_git else None
    if salida_json:
        print(json.dumps({"resultados": resultados, "resumen": resumen, "git": g}, ensure_ascii=False, indent=2))
    else:
        print("| Comprobacion | Estado | Segundos | Detalle |\n|---|---|---|---|")
        for r in resultados:
            print(f"| {r['nombre']} | {r['estado']} | {r['segundos']} | {r['detalle']} |")
        print(f"\nResumen: {resumen} (esto habla de las comprobaciones configuradas, no de que el producto este bien).")
        if g:
            print(f"Git: rama {g['rama']}, {g['sincronizacion']}, {g['modificados']} modificados, {g['sin_seguimiento']} sin seguimiento.")
    return 1 if hay_fallos else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
