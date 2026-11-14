#!/usr/bin/env python3
"""Valida una o varias skills del kit.

Uso: python validar_skill.py [--secciones | --estricto] [--calidad] <carpeta-skill> [<carpeta-skill> ...]
     python validar_skill.py [--secciones | --estricto] [--calidad] --todas <carpeta-skills>

Comprueba: SKILL.md con frontmatter, name == carpeta (kebab-case, max 64),
description (max 1024, sin < ni >, empieza por "Usar cuando" salvo skills de
terceros), nombres de proyecto o rutas de usuario, archivos grandes, enlaces
`references/...` / `scripts/...` que no existen y (aviso) nombres de scripts
citados entre comillas invertidas que no existen dentro de la skill.
Opcional, para skills nuevas de proceso (las de terceros se omiten):
  --secciones  AVISA de cada seccion que falte: "Cuando NO usar", "Excusas -> realidad",
               "Senales de alarma / errores comunes" y "Verificacion".
  --estricto   lo mismo, pero como ERROR.
  --calidad    AVISA (nunca error) de: enlaces markdown relativos rotos fuera de bloques de codigo,
               campos del frontmatter fuera de la especificacion, description de menos de 50
               caracteres y texto de plantilla sin reemplazar (criterios inspirados en el linter
               skill-check, MIT, reescritos aqui con codigo propio).
Sale con 0 si no hay errores, 1 si los hay. Solo biblioteca estandar.
"""
import re
import sys
from pathlib import Path

# Se arma por partes para que este archivo no se marque a si mismo.
_NOMBRES = ["kai" + "ros", "lap" + "lace", "loom" + "wick", "sabo" + "res",
            "global rep" + "uestos", "pagi" + "na1", "hon" + "kon", "jho" + "sw",
            "C:" + r"\\Users"]
PROHIBIDOS = re.compile("|".join(_NOMBRES), re.IGNORECASE)
MAX_BYTES = 300 * 1024
# Secciones de una skill de proceso (se buscan en los encabezados). Origen de la idea: validador de estructura
# de agent-skills (MIT), reescrito aqui con criterios propios.
SECCIONES = {
    "Cuando NO usar": re.compile(r"^#{1,4}\s*(cu[aá]ndo no usar|no usar (cuando|si)|l[ií]mites|alcance y l[ií]mites)", re.I | re.M),
    "Excusas -> realidad": re.compile(r"^#{1,4}\s*.*(excusa|racionalizaci)", re.I | re.M),
    "Senales de alarma / errores comunes": re.compile(r"^#{1,4}\s*.*(se[ñn]ales de alarma|errores comunes|red flags|antipatrones|anti-patrones)", re.I | re.M),
    "Verificacion": re.compile(r"^#{1,4}\s*.*(verificaci[oó]n|verificar|c[oó]mo verificar|comprobar|validar)", re.I | re.M),
}
# Campos del frontmatter que Claude Code o la especificacion de skills reconocen (ver docs/investigaciones/claude-code-docs.md).
CAMPOS_ESTANDAR = {"name", "description", "license", "compatibility", "metadata", "allowed-tools", "when_to_use",
                   "argument-hint", "disable-model-invocation", "user-invocable", "model", "effort", "context",
                   "agent", "hooks", "paths", "shell", "version"}
ENLACE_MD = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
PLANTILLA = re.compile(r"^\s*(?:[-*]\s*)?(?:Describe|Replace with|TODO|Escribe aqu)\b", re.I | re.M)
GUION_SIN_RUTA = re.compile(r"`([\w.-]+\.(?:py|sh|js|mjs|cjs|ps1))`")


def frontmatter(texto):
    m = re.match(r"^---\r?\n(.*?)\r?\n---", texto, re.DOTALL)
    if not m:
        return None
    datos, clave = {}, None
    for linea in m.group(1).splitlines():
        k = re.match(r"^([A-Za-z_-]+):\s*(.*)$", linea)
        if k:
            clave = k.group(1)
            datos[clave] = k.group(2).strip().strip(">|").strip()
        elif clave and linea.startswith((" ", "\t")):
            datos[clave] = (datos[clave] + " " + linea.strip()).strip()
    return datos


def validar(carpeta, secciones=False, estricto=False, calidad=False):
    errores, avisos = [], []
    carpeta = Path(carpeta)
    md = carpeta / "SKILL.md"
    if not md.exists():
        return [f"{carpeta}: falta SKILL.md"], avisos
    texto = md.read_text(encoding="utf-8", errors="replace")
    fm = frontmatter(texto)
    if fm is None:
        return [f"{carpeta.name}: sin frontmatter YAML"], avisos
    nombre, desc = fm.get("name", "").strip("\"'"), fm.get("description", "").strip("\"'")
    if not nombre:
        errores.append("falta name")
    else:
        if nombre != carpeta.name:
            errores.append(f"name '{nombre}' distinto de la carpeta '{carpeta.name}'")
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", nombre) or len(nombre) > 64:
            errores.append("name debe ser kebab-case de hasta 64 caracteres")
    if not desc:
        errores.append("falta description")
    else:
        if len(desc) > 1024:
            errores.append(f"description de {len(desc)} caracteres (max 1024)")
        if "<" in desc or ">" in desc:
            errores.append("description contiene < o >")
        if not desc.lower().startswith("usar cuando"):
            avisos.append("description no empieza por 'Usar cuando' (ok solo en skills de terceros)")
    lineas = texto.count("\n") + 1
    if lineas > 500:
        errores.append(f"SKILL.md de {lineas} lineas (max 500; ideal menos de 250)")
    elif lineas > 250:
        avisos.append(f"SKILL.md de {lineas} lineas (ideal menos de 250)")
    for archivo in carpeta.rglob("*"):
        if archivo.is_file():
            if archivo.stat().st_size > MAX_BYTES:
                errores.append(f"{archivo.relative_to(carpeta)} pesa mas de 300 KB")
            if archivo.suffix.lower() in {".md", ".py", ".sh", ".txt", ".json", ".yaml", ".yml"}:
                try:
                    cont = archivo.read_text(encoding="utf-8", errors="replace")
                except OSError:
                    continue
                for n, lin in enumerate(cont.splitlines(), 1):
                    if PROHIBIDOS.search(lin):
                        errores.append(f"{archivo.relative_to(carpeta)}:{n} nombre de proyecto o ruta de usuario")
                        break
    for ref in set(re.findall(r"`?((?:references|scripts|assets)/[\w./-]+\.\w+)`?", texto)):
        if not (carpeta / ref).exists():
            errores.append(f"enlace roto: {ref}")
    # Scripts citados sin carpeta (p. ej. `verificar_x.py`): aviso si no existen en ningun lugar de la skill.
    existentes = {a.name for a in carpeta.rglob("*") if a.is_file()}
    cuerpo = texto.split("---", 2)[-1] if texto.startswith("---") else texto
    for nombre_s in sorted(set(GUION_SIN_RUTA.findall(cuerpo))):
        if nombre_s not in existentes and "/" not in nombre_s:
            avisos.append(f"cita el script `{nombre_s}` pero no existe dentro de la skill (ok si es de otra skill o de tools/)")
    if (secciones or estricto) and desc.lower().startswith("usar cuando"):
        for etiqueta, patron in SECCIONES.items():
            if not patron.search(cuerpo):
                (errores if estricto else avisos).append(f"falta la seccion '{etiqueta}'")
    if calidad:
        raros = sorted(k for k in fm if k not in CAMPOS_ESTANDAR)
        if raros:
            avisos.append("campos fuera de la especificacion en el frontmatter: " + ", ".join(raros))
        if desc and len(desc) < 50:
            avisos.append(f"description de {len(desc)} caracteres (se recomiendan al menos 50)")
        sin_codigo = re.sub(r"`[^`\n]*`", "", re.sub(r"```.*?```", "", cuerpo, flags=re.DOTALL))
        if PLANTILLA.search(sin_codigo):
            avisos.append("texto de plantilla sin reemplazar (Describe..., Replace with..., TODO...)")
        for destino in sorted(set(ENLACE_MD.findall(sin_codigo))):
            ruta = destino.split("#")[0]
            if (not ruta or re.match(r"^[a-z][a-z0-9+.-]*:", ruta) or any(c in ruta for c in "<>{}$*")
                    or ruta.startswith(("references/", "scripts/", "assets/"))):
                continue
            if not (carpeta / ruta).exists():
                avisos.append(f"enlace markdown roto: {destino}")
    return [f"{carpeta.name}: {e}" for e in errores], [f"{carpeta.name}: {a}" for a in avisos]


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 2 if not argv else 0
    secciones = estricto = calidad = False
    while argv and argv[0] in ("--secciones", "--estricto", "--calidad"):
        secciones = secciones or argv[0] == "--secciones"
        estricto = estricto or argv[0] == "--estricto"
        calidad = calidad or argv[0] == "--calidad"
        argv = argv[1:]
    if not argv:
        print(__doc__)
        return 2
    if argv[0] == "--todas":
        raiz = Path(argv[1])
        carpetas = sorted(p for p in raiz.iterdir() if p.is_dir() and not p.name.startswith("_"))
    else:
        carpetas = [Path(a) for a in argv]
    total_err = 0
    for c in carpetas:
        errores, avisos = validar(c, secciones, estricto, calidad)
        for a in avisos:
            print("AVISO ", a)
        for e in errores:
            print("ERROR ", e)
        total_err += len(errores)
        if not errores:
            print("OK    ", c.name)
    return 1 if total_err else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
