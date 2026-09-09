# Repaso de Python — Imágenes como datos

**Material desarrollado para el IFTS Nº 24 (2026) — Laboratorio de Tecnologías de la Imagen Digital.**

Clase de repaso de Python (90 minutos) pensada como puente entre las unidades de py5 y el bloque técnico de fundamentos de PDI: recorre `pathlib`, lectura de metadatos de imágenes, conversión de una imagen a matriz de números con Pillow/NumPy, estructuras de control, funciones reutilizables y un cierre armando una mini interfaz con Gradio. Esta carpeta puede usarse de forma independiente porque incluye su propia configuración de dependencias con `uv`.

## Contenido

- `00 - repaso de python.ipynb`: notebook único de la clase de repaso.
- `Imagenes/escena_urbana.png`: imagen de ejemplo usada a lo largo del cuaderno.

## Requisitos

- Python 3.12 — [descarga oficial](https://www.python.org/downloads/).
- Git — [descarga oficial](https://git-scm.com/downloads).
- `uv` instalado y disponible en el PATH. Ver [cómo instalar uv](INSTALACION_UV.md).
- Visual Studio Code con las extensiones necesarias. Ver [cómo instalar VS Code y sus extensiones](INSTALACION_VSCODE.md).

## Crear el entorno

Desde esta carpeta, ejecutar:

```powershell
uv sync
```

`uv sync` crea `.venv` con la versión de Python fijada en `.python-version` (3.12) e instala las versiones fijadas en `uv.lock`. El archivo `pyproject.toml` contiene las dependencias directas del laboratorio (numpy, matplotlib, pillow, gradio) más `ipykernel` para poder usar el entorno como kernel de Jupyter/VS Code.

### Registrar el kernel con nombre propio

Como vas a tener varios entornos virtuales (uno por carpeta), conviene registrar el kernel de este con un nombre identificable en vez de dejar el genérico "Python 3 (ipykernel)". Con el entorno ya sincronizado, ejecutar:

```powershell
.venv\Scripts\python.exe -m ipykernel install --user --name pdi-002a-repaso-python --display-name "PDI 002a - Repaso de Python"
```

Esto registra el kernel en tu carpeta de Jupyter (con `--user`), así que va a aparecer en VS Code/Jupyter identificado como **"PDI 002a - Repaso de Python"**, sin mezclarse con los kernels de las demás carpetas.

## Activar el entorno

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

En macOS o Linux:

```bash
source .venv/bin/activate
```

## Abrir el notebook

La forma recomendada es VS Code (ver [instalación y selección del kernel](INSTALACION_VSCODE.md)): abrir esta carpeta en VS Code y seleccionar `.venv\Scripts\python.exe` (Windows) o `.venv/bin/python` (macOS/Linux) como intérprete/kernel.

Si preferís Jupyter Lab en el navegador:

```powershell
uv run --with jupyter jupyter lab
```

## Actualizar dependencias

Para actualizar el lockfile y sincronizar el entorno:

```powershell
uv lock --upgrade
uv sync
```
