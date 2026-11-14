#!/usr/bin/env python3
"""Valida un prompt largo guardado para otra IA y, si se da, su version corta (solo lectura, sin red).

Uso: python validar_prompt.py <archivo.md> [--corto "texto"] [--max-corto N]
     python validar_prompt.py --help

Comprueba en el archivo largo:
  * lineas "**Fecha:**" y "**Tipo:**" al inicio;
  * secciones Contexto, Objetivo, Condicion de termino, Restricciones, Como trabajar y Entrega (con o sin tildes);
  * dentro de "Condicion de termino": "Estado final medible", "Comprobacion" y "Tope", cada uno con contenido;
  * ningun marcador "<...>" sin reemplazar, ningun patron de secreto y ninguna ruta de usuario;
  * aviso si pasa de 15000 caracteres (un prompt enorme entierra lo importante).
Comprueba en el corto (--corto): nombra un archivo .md, menciona un tope (turnos, tokens, minutos, horas, tiempo, tope, limite)
y no pasa de --max-corto caracteres (por defecto 4000, el limite mas estricto conocido de un objetivo persistente).
Sale con 0 sin errores, 1 con errores, 2 si el uso es incorrecto. Solo biblioteca estandar.
"""
import re
import sys
from pathlib import Path

SECCIONES = {
    "Contexto": r"contexto",
    "Objetivo": r"objetivo",
    "Condicion de termino": r"condici[oó]n de t[eé]rmino",
    "Restricciones": r"restricciones",
    "Como trabajar": r"c[oó]mo trabajar",
    "Entrega": r"entrega",
}
CAMPOS = {"Estado final medible": r"estado final medible", "Comprobacion": r"comprobaci[oó]n", "Tope": r"tope"}
SECRETOS = re.compile(r"ghp_[A-Za-z0-9]{6}|github_pat_[A-Za-z0-9]|sk-[A-Za-z0-9]{8}|AKIA[0-9A-Z]{8}|-----BEGIN|xox[bp]-[0-9A-Za-z]")
RUTA_USUARIO = re.compile(r"[A-Za-z]:[\\/]Users[\\/][A-Za-z0-9][^\\/\s<>{}$%]*|/home/[a-z][a-z0-9_-]+/|/Users/[A-Za-z][A-Za-z0-9_-]+/")
MARCADOR = re.compile(r"<[^<>\n`]{2,80}>")
MAX_LARGO = 15000


def sin_codigo(texto):
    return re.sub(r"`[^`\n]*`", "", re.sub(r"```.*?```", "", texto, flags=re.S))


def validar_largo(texto):
    errores = []
    cabecera = "\n".join(texto.splitlines()[:8])
    for etiqueta in ("Fecha", "Tipo"):
        if not re.search(rf"\*\*{etiqueta}:\*\*[ \t]*\S", cabecera):
            errores.append(f"falta la linea '**{etiqueta}:**' al inicio")
    cuerpo = {}
    partes = re.split(r"^##\s+", texto, flags=re.M)[1:]
    for p in partes:
        titulo, _, resto = p.partition("\n")
        cuerpo[titulo.strip().lower()] = resto
    for nombre, patron in SECCIONES.items():
        clave = next((t for t in cuerpo if re.match(patron, t)), None)
        if clave is None:
            errores.append(f"falta la seccion '{nombre}'")
    clave = next((t for t in cuerpo if re.match(SECCIONES["Condicion de termino"], t)), None)
    if clave is not None:
        for nombre, patron in CAMPOS.items():
            m = re.search(rf"^[ \t]*[-*][ \t]*\*\*{patron}:?\*\*:?[ \t]*(.*)$", cuerpo[clave], re.M | re.I)
            if not m or not m.group(1).strip():
                errores.append(f"en 'Condicion de termino' falta '{nombre}' o esta vacio")
    if MARCADOR.search(sin_codigo(texto)):
        errores.append("quedan marcadores <...> sin reemplazar")
    for n, linea in enumerate(texto.splitlines(), 1):
        if SECRETOS.search(linea):
            errores.append(f"linea {n}: posible secreto")
        if RUTA_USUARIO.search(linea):
            errores.append(f"linea {n}: ruta de usuario (usar rutas relativas al proyecto)")
    return errores


def validar_corto(texto, maximo):
    errores = []
    if not re.search(r"[\w./-]+\.md\b", texto):
        errores.append("el prompt corto no nombra el archivo .md con el prompt largo")
    if not re.search(r"turnos?|tokens?|minutos?|horas?|tiempo|tope|l[ií]mite", texto, re.I):
        errores.append("el prompt corto no menciona un tope (turnos, tokens, minutos, horas, tiempo)")
    if len(texto) > maximo:
        errores.append(f"el prompt corto tiene {len(texto)} caracteres (maximo {maximo})")
    return errores


def main(argv):
    if not argv or any(a in ("-h", "--help") for a in argv):
        print(__doc__)
        return 0 if argv else 2
    corto, maximo = None, 4000
    resto = list(argv)
    if "--corto" in resto:
        i = resto.index("--corto")
        corto = resto[i + 1]
        resto = resto[:i] + resto[i + 2:]
    if "--max-corto" in resto:
        i = resto.index("--max-corto")
        maximo = int(resto[i + 1])
        resto = resto[:i] + resto[i + 2:]
    if len(resto) != 1 or not Path(resto[0]).is_file():
        print(__doc__)
        return 2
    texto = Path(resto[0]).read_text(encoding="utf-8", errors="replace")
    errores = validar_largo(texto)
    if corto is not None:
        errores += ["corto: " + e for e in validar_corto(corto, maximo)]
    if len(texto) > MAX_LARGO:
        print(f"AVISO  el prompt largo tiene {len(texto)} caracteres (mas de {MAX_LARGO}); conviene acortarlo")
    for e in errores:
        print("ERROR:", e)
    print("OK" if not errores else f"{len(errores)} error(es)")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
