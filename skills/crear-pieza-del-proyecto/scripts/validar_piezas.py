#!/usr/bin/env python3
"""Valida las piezas LOCALES de un proyecto (solo lectura, sin red).

Uso: python validar_piezas.py <carpeta-.claude> [--mapa <archivo-mapa>]
     python validar_piezas.py --help

Comprueba en <carpeta-.claude>/skills, /rules y /agents:
  * skill: SKILL.md con frontmatter; name igual a la carpeta (minusculas y guiones, hasta 64);
    description que empieza por "Usar cuando" y de hasta 1024 caracteres, sin < ni >.
  * regla: linea "Aplica a:" (error); las secciones "Por que" y "Como se aplica" (con o sin tildes) se piden como AVISO.
  * agente: frontmatter con name, description, model y effort.
  * todas: sin texto de plantilla sin reemplazar ("<...>" en frontmatter, "Describe"), sin patrones de
    secretos (una cabecera de clave privada completa, tokens con su prefijo y cuerpo) y sin rutas de usuario
    (la carpeta Users de una unidad, /home/<x>, /Users/<x>). Las lineas que empiezan por "- No:" son contraejemplos
    deliberados (convencion de las reglas del kit) y no se revisan en busca de rutas de usuario.
  * con --mapa: cada pieza (por nombre) aparece en el archivo de mapa de areas.
Sale con 0 sin errores, 1 con errores, 2 si el uso es incorrecto. Solo biblioteca estandar.
"""
import re
import sys
from pathlib import Path

SECRETOS = re.compile(r"ghp_[A-Za-z0-9]{6}|github_pat_[A-Za-z0-9]|sk-[A-Za-z0-9]{8}|AKIA[0-9A-Z]{8}|-----BEGIN [A-Z ]*PRIVATE KEY-----|xox[bp]-[0-9A-Za-z]")
RUTA_USUARIO = re.compile(r"[A-Za-z]:[\\/]Users[\\/][A-Za-z0-9][^\\/\s<>{}$%]*|/home/[a-z][a-z0-9_-]+/|/Users/[A-Za-z][A-Za-z0-9_-]+/")
AVISOS = []
NOMBRE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def sin_tildes(s):
    return s.lower().translate(str.maketrans("áéíóúü", "aeiouu"))


def frontmatter(texto):
    m = re.match(r"^---\r?\n(.*?)\r?\n---", texto, re.S)
    if not m:
        return None
    campos = {}
    for linea in m.group(1).splitlines():
        k, sep, v = linea.partition(":")
        if sep and k and not k.startswith((" ", "\t")):
            campos[k.strip()] = v.strip()
    return campos


def comunes(nombre_archivo, texto, errores):
    for n, linea in enumerate(texto.splitlines(), 1):
        if SECRETOS.search(linea):
            errores.append(f"{nombre_archivo}:{n}: posible secreto")
        if RUTA_USUARIO.search(linea) and not linea.lstrip().startswith("- No:"):
            errores.append(f"{nombre_archivo}:{n}: ruta de usuario (usar variable de entorno o ruta relativa)")


def revisar_skill(d, errores):
    f = d / "SKILL.md"
    if not f.is_file():
        errores.append(f"{d.name}: falta SKILL.md")
        return None
    texto = f.read_text(encoding="utf-8", errors="replace")
    fm = frontmatter(texto)
    rel = f"skills/{d.name}/SKILL.md"
    if fm is None:
        errores.append(f"{rel}: sin frontmatter")
        return d.name
    name, desc = fm.get("name", ""), fm.get("description", "")
    if not name:
        errores.append(f"{rel}: falta name")
    elif name != d.name:
        errores.append(f"{rel}: name '{name}' distinto de la carpeta '{d.name}'")
    elif not NOMBRE.match(name) or len(name) > 64:
        errores.append(f"{rel}: name invalido (minusculas y guiones, hasta 64)")
    if not desc:
        errores.append(f"{rel}: falta description")
    else:
        if not desc.lower().startswith("usar cuando"):
            errores.append(f"{rel}: la description debe empezar por 'Usar cuando'")
        if len(desc) > 1024:
            errores.append(f"{rel}: description de {len(desc)} caracteres (maximo 1024)")
        if "<" in desc or ">" in desc:
            errores.append(f"{rel}: la description contiene '<' o '>' (texto de plantilla sin reemplazar?)")
    if re.search(r"^\s*(Describe|Replace with)\b", texto, re.M):
        errores.append(f"{rel}: texto de plantilla sin reemplazar")
    comunes(rel, texto, errores)
    return name or d.name


def revisar_regla(f, errores):
    texto = f.read_text(encoding="utf-8", errors="replace")
    rel = f"rules/{f.name}"
    t = sin_tildes(texto)
    if not re.search(r"aplica a\s*:", t):
        errores.append(f"{rel}: falta la linea 'Aplica a:'")
    for sec in ("por que", "como se aplica"):
        if not re.search(r"^##\s+" + sec, t, re.M):
            AVISOS.append(f"{rel}: conviene la seccion '{sec}'")
    comunes(rel, texto, errores)
    return f.stem


def revisar_agente(f, errores):
    texto = f.read_text(encoding="utf-8", errors="replace")
    rel = f"agents/{f.name}"
    fm = frontmatter(texto)
    if fm is None:
        errores.append(f"{rel}: sin frontmatter")
    else:
        for k in ("name", "description", "model", "effort"):
            if not fm.get(k):
                errores.append(f"{rel}: falta '{k}' en el frontmatter")
        if any("<" in v for v in fm.values()):
            errores.append(f"{rel}: texto de plantilla sin reemplazar en el frontmatter")
    comunes(rel, texto, errores)
    return (fm or {}).get("name") or f.stem


def main(argv):
    if not argv or any(a in ("-h", "--help") for a in argv):
        print(__doc__)
        return 0 if argv else 2
    mapa = None
    if "--mapa" in argv:
        i = argv.index("--mapa")
        mapa = Path(argv[i + 1])
        argv = argv[:i] + argv[i + 2:]
    base = Path(argv[0])
    if not base.is_dir():
        print(__doc__)
        return 2
    errores, nombres = [], []
    sk = base / "skills"
    if sk.is_dir():
        for d in sorted(p for p in sk.iterdir() if p.is_dir()):
            nombres.append(revisar_skill(d, errores))
    rl = base / "rules"
    if rl.is_dir():
        for f in sorted(rl.glob("*.md")):
            nombres.append(revisar_regla(f, errores))
    ag = base / "agents"
    if ag.is_dir():
        for f in sorted(ag.glob("*.md")):
            nombres.append(revisar_agente(f, errores))
    nombres = [n for n in nombres if n]
    if mapa is not None:
        if not mapa.is_file():
            errores.append(f"no existe el archivo de mapa: {mapa}")
        else:
            m = mapa.read_text(encoding="utf-8", errors="replace")
            for n in nombres:
                if n not in m:
                    errores.append(f"'{n}' no figura en el mapa de areas ({mapa.name})")
    print(f"{len(nombres)} pieza(s) locales revisadas en {base}")
    for a in AVISOS:
        print("AVISO:", a)
    for e in errores:
        print("ERROR:", e)
    print("OK" if not errores else f"{len(errores)} error(es)")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
