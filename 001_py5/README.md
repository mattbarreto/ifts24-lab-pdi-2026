# Introducción a py5

**Profesor Titular:** Matías Barreto — Especialista en Nuevos Medios e Interactividad

Material creado por el profesor para la materia PDI de IFTS Nº 24.

Unidad inicial con scripts sueltos de introducción a `py5` (Processing para Python): dibujo básico, color RGB/HSV, lectura de información de imágenes, manejo de píxeles, filtros simples e interacción con mouse. Esta carpeta puede usarse de forma independiente porque incluye su propia configuración de dependencias con `uv`.

## Contenido

Scripts `.py` numerados en orden de dificultad creciente (000 a 015): setup básico, colores RGB/HSV, carga de imágenes, lectura y edición de píxeles, filtros y dibujo con eventos de mouse. `info.txt` es un resumen rápido de la API de py5 usada en los scripts.

## Requisitos

- Python 3.12 — [descarga oficial](https://www.python.org/downloads/).
- **Java (JDK)** — `py5` lo necesita para correr Processing por debajo. Ver la [guía oficial de instalación de py5](https://py5coding.org/content/install.html), que detalla cómo instalar Java según el sistema operativo.
- Git — [descarga oficial](https://git-scm.com/downloads).
- `uv` instalado y disponible en el PATH. Ver [cómo instalar uv](INSTALACION_UV.md).
- Visual Studio Code con las extensiones necesarias. Ver [cómo instalar VS Code y sus extensiones](INSTALACION_VSCODE.md).

## Crear el entorno

Desde esta carpeta, ejecutar:

```powershell
uv sync
```

`uv sync` crea `.venv` con la versión de Python fijada en `.python-version` (3.12) e instala las versiones fijadas en `uv.lock`. El archivo `pyproject.toml` contiene la dependencia directa del laboratorio (`py5`) más `ipykernel` para poder usar el entorno como kernel de VS Code.

### Registrar el kernel con nombre propio

Como vas a tener varios entornos virtuales (uno por carpeta), conviene registrar el kernel de este con un nombre identificable en vez de dejar el genérico "Python 3 (ipykernel)". Con el entorno ya sincronizado, ejecutar:

```powershell
.venv\Scripts\python.exe -m ipykernel install --user --name pdi-001-py5 --display-name "PDI 001 - Py5 Intro"
```

Esto registra el kernel en tu carpeta de Jupyter (con `--user`), así que va a aparecer en VS Code/Jupyter identificado como **"PDI 001 - Py5 Intro"**, sin mezclarse con los kernels de las demás carpetas.

## Activar el entorno

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

En macOS o Linux:

```bash
source .venv/bin/activate
```

## Ejecutar los scripts

Los archivos de esta carpeta son scripts `.py`, no notebooks. En VS Code (ver [instalación y selección del intérprete](INSTALACION_VSCODE.md)): abrir esta carpeta, seleccionar `.venv\Scripts\python.exe` (Windows) o `.venv/bin/python` (macOS/Linux) como intérprete, y ejecutar cada script con `F5` o el botón de play.

También se puede ejecutar sin activar el entorno:

```powershell
uv run python "000_intro_py5.py"
```

## Actualizar dependencias

Para actualizar el lockfile y sincronizar el entorno:

```powershell
uv lock --upgrade
uv sync
```

`uv lock --upgrade` actualiza `uv.lock`, pero **no** actualiza `requirements.txt` automáticamente: ese archivo se generó una vez a partir del lock y queda desactualizado si no lo volvés a exportar. Después de sincronizar, correr también:

```powershell
uv export --format requirements.txt --no-hashes -o requirements.txt
```
