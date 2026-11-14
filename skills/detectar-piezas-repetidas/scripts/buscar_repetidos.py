#!/usr/bin/env python3
"""Busca candidatas a pieza propia del proyecto (solo lectura, sin red).

Uso: python buscar_repetidos.py <carpeta-.memory> [<carpeta-bitacora>] [--minimo N]
     python buscar_repetidos.py --help

Muestra:
  1. Lecciones de lecciones.md con "Veces: N" >= minimo (por defecto 3) que NO estan automatizadas.
  2. Si se da la carpeta de bitacora (humanoN.md): frases de "Lo que pidio" que aparecen
     al menos `minimo` veces (misma instruccion repetida), normalizadas a minusculas.
Salida: 0 siempre que el uso sea correcto (es un informe, no una validacion); 2 si el uso es incorrecto.
Solo biblioteca estandar.
"""
import re
import sys
from collections import Counter
from pathlib import Path


def lecciones(memoria, minimo):
    f = memoria / "lecciones.md"
    if not f.is_file():
        return []
    texto = f.read_text(encoding="utf-8", errors="replace")
    out = []
    for parte in re.split(r"^##\s+", texto, flags=re.M)[1:]:
        titulo, _, cuerpo = parte.partition("\n")
        m = re.search(r"Veces\W*:\W*(\d+)", cuerpo, re.I)
        auto = re.search(r"Automatizada\W*:\W*(.+)", cuerpo, re.I)
        veces = int(m.group(1)) if m else 1
        automatizada = bool(auto) and auto.group(1).strip().lstrip("*_` ").lower().startswith("s")
        if veces >= minimo and not automatizada:
            out.append((titulo.strip(), veces))
    return out


def frases_repetidas(carpeta, minimo):
    cont = Counter()
    for f in sorted(carpeta.glob("humano*.md")):
        for m in re.finditer(r"\*\*Lo que pidió:\*\*\s*\*?\"?(.+?)\"?\*?\s*$", f.read_text(encoding="utf-8", errors="replace"), re.M):
            frase = re.sub(r"\s+", " ", m.group(1).strip().lower())[:120]
            if len(frase) > 15:
                cont[frase] += 1
    return [(k, v) for k, v in cont.most_common() if v >= minimo]


def main(argv):
    if not argv or any(a in ("-h", "--help") for a in argv):
        print(__doc__)
        return 0 if argv else 2
    minimo = 3
    if "--minimo" in argv:
        i = argv.index("--minimo")
        minimo = int(argv[i + 1])
        argv = argv[:i] + argv[i + 2:]
    memoria = Path(argv[0])
    if not memoria.is_dir():
        print(__doc__)
        return 2
    cands = lecciones(memoria, minimo)
    print(f"Lecciones con {minimo}+ repeticiones sin automatizar: {len(cands)}")
    for t, v in cands:
        print(f"  - {t} (x{v})")
    if len(argv) > 1 and Path(argv[1]).is_dir():
        fr = frases_repetidas(Path(argv[1]), minimo)
        print(f"Instrucciones repetidas en la bitacora ({minimo}+): {len(fr)}")
        for k, v in fr:
            print(f"  - x{v}: {k}")
    print("Informe de candidatas; proponer al usuario antes de crear nada.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
