#!/usr/bin/env python3
"""Verifica el mapa de areas contra las carpetas reales (solo lectura).

Uso: python verificar_mapa.py <mapa.json> <carpeta-skills> <carpeta-reglas> <carpeta-agentes>
     python verificar_mapa.py --help

Comprueba:
  1. Toda skill, regla y agente referenciado en "areas" existe
     (skills: carpeta con SKILL.md; reglas y agentes: archivo <nombre>.md).
  2. Toda skill, regla y agente presente figura en algun area o en "archivadas".
Se ignoran entradas que empiezan por "_". Sale con 0 si todo bien, 1 si hay
errores, 2 si el uso es incorrecto. Solo biblioteca estandar.
"""
import json
import sys
from pathlib import Path


def existentes(carpeta, tipo):
    p = Path(carpeta)
    if not p.is_dir():
        raise SystemExit(f"No existe la carpeta: {carpeta}")
    if tipo == "skills":
        return {d.name for d in p.iterdir()
                if d.is_dir() and not d.name.startswith("_") and (d / "SKILL.md").is_file()}
    return {f.stem for f in p.glob("*.md") if not f.name.startswith("_")}


def main(argv):
    if len(argv) == 2 and argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0
    if len(argv) != 5:
        print(__doc__)
        return 2
    try:
        mapa = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        print(f"ERROR: no se pudo leer el mapa: {e}")
        return 1
    carpetas = {"skills": argv[2], "reglas": argv[3], "agentes": argv[4]}
    errores = []
    for tipo, carpeta in carpetas.items():
        hay = existentes(carpeta, tipo)
        ref = set()
        for area, datos in mapa.get("areas", {}).items():
            for nombre in datos.get(tipo, []):
                ref.add(nombre)
                if nombre not in hay:
                    errores.append(f"area '{area}': {tipo[:-1]} '{nombre}' no existe")
        archivadas = set(mapa.get("archivadas", {}).get(tipo, []))
        for nombre in sorted(hay - ref - archivadas):
            errores.append(f"{tipo[:-1]} '{nombre}' existe pero no figura en el mapa")
        print(f"{tipo}: {len(hay)} presentes, {len(ref)} referenciadas, {len(archivadas)} archivadas")
    for e in errores:
        print("ERROR:", e)
    print("OK" if not errores else f"{len(errores)} error(es)")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
