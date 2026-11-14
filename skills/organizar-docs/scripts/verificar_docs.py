#!/usr/bin/env python3
"""Verifica una carpeta de documentacion (solo lectura).

Uso: python verificar_docs.py <carpeta-docs> [--raiz <carpeta-proyecto>]
     python verificar_docs.py --help

Comprueba:
  1. Documentos VIGENTES que citan archivos inexistentes (rutas entre
     comillas invertidas con extension conocida, resueltas contra la carpeta
     del documento, la carpeta docs o la raiz del proyecto).
  2. Enlaces markdown `[texto](ruta)` rotos (se omiten URLs y anclas).
  3. Carpetas con mas de 5 documentos .md sin indice (README.md o INDEX.md).
Se consideran FOTOS FECHADAS (excluidas de 1 por diseno): los archivos en una
carpeta de fotos (planes, decisiones, investigaciones, auditorias, qa, humano,
informes, archivo/archivado/archive), o con la linea "Tipo: foto fechada" en
las primeras 15 lineas, o (por compatibilidad) con nombre que empieza por una
fecha AAAA-MM-DD o por NNNN-. La fecha va DENTRO del archivo, no en el nombre.
El resto es vigente. Los
enlaces rotos (2) se revisan en todos, tambien en fotos.
--raiz: raiz del proyecto para resolver rutas (por defecto, la carpeta padre
de docs). Salida: 0 sin problemas, 1 con problemas, 2 si la carpeta no existe.
"""
import re
import sys
from pathlib import Path

EXT = r"(?:md|py|js|ts|tsx|json|ya?ml|toml|sh|bat|ps1|kt|go|rs|java|html|css|sql|txt|cfg|ini)"
RE_CODIGO = re.compile(r"`([^`\s]+\.%s)(?::\d+(?:-\d+)?)?`" % EXT)
RE_ENLACE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
RE_FECHA = re.compile(r"^(\d{4}-\d{2}-\d{2}|\d{4})[-_]")
CARPETAS_ARCHIVO = {"archivo", "archivado", "archive", "archived", "planes", "decisiones", "investigaciones",
                    "investigacion", "auditorias", "qa", "humano", "informes", "retros"}
RE_TIPO_FOTO = re.compile(r"tipo:\W*foto fechada", re.I)
LIMITE = 5


def es_foto(p, docs):
    rel = p.relative_to(docs).parts
    if bool(RE_FECHA.match(p.name)) or any(x.lower() in CARPETAS_ARCHIVO for x in rel[:-1]):
        return True
    try:
        cabecera = "\n".join(p.read_text(encoding="utf-8", errors="ignore").splitlines()[:15])
    except OSError:
        return False
    return bool(RE_TIPO_FOTO.search(cabecera))


def sin_bloques(texto):
    return re.sub(r"```.*?```", "", texto, flags=re.DOTALL)


def existe(ref, doc, docs, raiz):
    if any(c in ref for c in "<>*{}$%") or ref.startswith(("http", "~")):
        return True  # marcador o patron: no se puede comprobar
    for base in (doc.parent, docs, raiz):
        if (base / ref).exists():
            return True
    return False


def main(argv):
    if not argv or any(a in ("-h", "--help") for a in argv):
        print(__doc__)
        return 0
    raiz = None
    if "--raiz" in argv:
        i = argv.index("--raiz")
        raiz = Path(argv[i + 1]).resolve()
        argv = argv[:i] + argv[i + 2:]
    docs = Path(argv[0]).resolve()
    if not docs.is_dir():
        print(f"No existe la carpeta: {docs}")
        return 2
    raiz = raiz or docs.parent
    problemas = []
    mds = sorted(docs.rglob("*.md"))
    for p in mds:
        rel = p.relative_to(docs)
        try:
            texto = sin_bloques(p.read_text(encoding="utf-8", errors="ignore"))
        except OSError:
            continue
        if not es_foto(p, docs):
            for n, linea in enumerate(texto.splitlines(), 1):
                for m in RE_CODIGO.finditer(linea):
                    if not existe(m.group(1), p, docs, raiz):
                        problemas.append(f"{rel}:{n}: vigente cita archivo inexistente `{m.group(1)}`")
        for n, linea in enumerate(texto.splitlines(), 1):
            for m in RE_ENLACE.finditer(linea):
                destino = m.group(1).split("#")[0]
                if not destino or re.match(r"^[a-z]+:", destino) or any(c in destino for c in "<>{}$"):
                    continue
                if not existe(destino, p, docs, raiz):
                    problemas.append(f"{rel}:{n}: enlace roto ({destino})")
    carpetas = {docs} | {d for d in docs.rglob("*") if d.is_dir()}
    for d in sorted(carpetas):
        docs_md = [f for f in d.glob("*.md")]
        nombres = {f.name.lower() for f in docs_md}
        if len(docs_md) > LIMITE and not ({"readme.md", "index.md"} & nombres):
            problemas.append(f"{d.relative_to(docs) if d != docs else '.'}/: {len(docs_md)} documentos sin indice (README.md o INDEX.md)")
    print(f"Revisados {len(mds)} documento(s) en {docs}")
    for pr in problemas:
        print("PROBLEMA " + pr)
    print("Sin problemas." if not problemas else f"{len(problemas)} problema(s).")
    return 1 if problemas else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
