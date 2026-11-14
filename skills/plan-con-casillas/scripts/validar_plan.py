#!/usr/bin/env python3
"""Valida un plan con fases y casillas (ver la skill plan-con-casillas).

Uso: python validar_plan.py <plan.md> [<plan2.md> ...]
Sale con codigo 1 si hay errores. Solo lee archivos; no modifica nada.

Reglas comprobadas:
  1. Cada tabla de metas tiene las columnas Hecho y Listo.
  2. Una meta con Hecho [x] tiene una linea "Evidencia <id>:" no vacia.
  3. Una meta con Listo [x] tiene Hecho [x] (Listo = meta cerrada, la marca el asistente; la aceptacion del
     producto por el usuario NO se valida aqui: va en una linea "Aceptacion del usuario:" del plan).
  4. Una fase marcada [x] solo tiene metas [x] o [-]; con una [ ] o [~] no puede ser [x].
"""
import re
import sys

ESTADOS = {"[ ]", "[x]", "[~]", "[-]"}
FASE = re.compile(r"^##\s+(F\d+)\b.*?(\[[ x~-]\])\s*`?\s*$", re.I)
FASE_LAX = re.compile(r"^##\s+(F\d+)\b", re.I)
FILA = re.compile(r"^\|\s*(F\d+\.\d+)\s*\|")
EVID = re.compile(r"^\s*Evidencia\s+(F\d+\.\d+)\s*:\s*(.*)$", re.I)
CONF = re.compile(r"^\s*Confirmaci[oó]n\s+(F\d+\.\d+)\s*:\s*(.*)$", re.I)


def celdas(linea):
    return [c.strip() for c in linea.strip().strip("|").split("|")]


def validar(ruta):
    errores = []
    lineas = open(ruta, encoding="utf-8").read().splitlines()
    fase_actual = None
    fases = {}      # id -> estado
    metas = {}      # id -> (fase, hecho, listo)
    evidencia = {}
    confirmacion = {}
    cols = None
    for n, l in enumerate(lineas, 1):
        m = FASE.match(l.strip())
        if m:
            fase_actual = m.group(1).upper()
            fases[fase_actual] = m.group(2).lower()
            cols = None
            continue
        if FASE_LAX.match(l.strip()):
            fase_actual = FASE_LAX.match(l.strip()).group(1).upper()
            fases.setdefault(fase_actual, None)
            cols = None
            continue
        if l.strip().startswith("|") and "Meta" in l and "Hecho" in l:
            cols = [c.lower() for c in celdas(l)]
            if "listo" not in cols:
                errores.append(f"{ruta}:{n}: la tabla no tiene la columna Listo")
            continue
        if l.strip().startswith("|") and "Meta" in l and "Hecho" not in l:
            errores.append(f"{ruta}:{n}: la tabla de metas no tiene la columna Hecho")
            continue
        f = FILA.match(l)
        if f and cols:
            c = celdas(l)
            if len(c) != len(cols):
                errores.append(f"{ruta}:{n}: la fila {c[0]} tiene {len(c)} celdas y la tabla {len(cols)}")
                continue
            hecho = c[cols.index("hecho")].lower() if "hecho" in cols else ""
            listo = c[cols.index("listo")].lower() if "listo" in cols else ""
            for nom, v in (("Hecho", hecho), ("Listo", listo)):
                if v and v not in ESTADOS:
                    errores.append(f"{ruta}:{n}: {c[0]} tiene un estado {nom} invalido: {v!r}")
            metas[c[0].upper()] = (fase_actual, hecho, listo)
            continue
        e = EVID.match(l)
        if e:
            evidencia[e.group(1).upper()] = e.group(2).strip()
        k = CONF.match(l)
        if k:
            confirmacion[k.group(1).upper()] = k.group(2).strip()

    if not metas:
        errores.append(f"{ruta}: no se encontro ninguna meta (filas F<n>.<m>)")
    for mid, (fase, hecho, listo) in metas.items():
        if hecho == "[x]" and not (evidencia.get(mid) and not evidencia[mid].startswith("<")):
            errores.append(f"{ruta}: {mid} esta [x] pero no tiene linea 'Evidencia {mid}:' con contenido")
        if listo == "[x]" and hecho != "[x]":
            errores.append(f"{ruta}: {mid} tiene Listo [x] pero Hecho no esta [x]")
    for fid, est in fases.items():
        if est == "[x]":
            abiertas = [mid for mid, (fase, h, _) in metas.items() if fase == fid and h not in ("[x]", "[-]")]
            if abiertas:
                errores.append(f"{ruta}: la fase {fid} esta [x] pero tiene metas abiertas o parciales: {', '.join(abiertas)}")
    return errores


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    todos = []
    for r in argv[1:]:
        todos += validar(r)
    for e in todos:
        print("ERROR", e)
    if not todos:
        print("OK: plan(es) validos")
    return 1 if todos else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
