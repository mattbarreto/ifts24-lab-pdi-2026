# Repaso de Python — Imágenes como datos

**Profesor Titular:** Matías Barreto — Especialista en Nuevos Medios e Interactividad

Material creado por el profesor para la materia PDI de IFTS Nº 24.

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
$env:UV_PROJECT_ENVIRONMENT = ".venv_002a"
uv venv .venv_002a --python 3.12
uv sync
```

> ⚠️ `UV_PROJECT_ENVIRONMENT` solo dura mientras esa terminal esté abierta. Si cerrás la terminal y abrís otra para correr `uv sync`, `uv run` o `uv lock` en esta carpeta, hay que volver a setear la variable antes (`$env:UV_PROJECT_ENVIRONMENT = ".venv_002a"`) — si no, uv va a crear un `.venv` genérico nuevo en vez de usar `.venv_002a`.

`uv sync` crea `.venv_002a` con la versión de Python fijada en `.python-version` (3.12) e instala las versiones fijadas en `uv.lock`. El archivo `pyproject.toml` contiene las dependencias directas del laboratorio (numpy, matplotlib, pillow, gradio) más `ipykernel` para poder usar el entorno como kernel de Jupyter/VS Code.

### Registrar el kernel con nombre propio

Como vas a tener varios entornos virtuales (uno por carpeta), conviene registrar el kernel de este con un nombre identificable en vez de dejar el genérico "Python 3 (ipykernel)". Con el entorno ya sincronizado, ejecutar:

```powershell
.venv_002a\Scripts\python.exe -m ipykernel install --user --name pdi-002a-repaso-python --display-name "PDI 002a - Repaso de Python"
```

Esto registra el kernel en tu carpeta de Jupyter (con `--user`), así que va a aparecer en VS Code/Jupyter identificado como **"PDI 002a - Repaso de Python"**, sin mezclarse con los kernels de las demás carpetas.

## Activar el entorno

En Windows PowerShell:

```powershell
.venv_002a\Scripts\Activate.ps1
```

En macOS o Linux:

```bash
source .venv_002a/bin/activate
```

## Abrir el notebook

La forma recomendada es VS Code (ver [instalación y selección del kernel](INSTALACION_VSCODE.md)): abrir esta carpeta en VS Code y seleccionar `.venv_002a\Scripts\python.exe` (Windows) o `.venv_002a/bin/python` (macOS/Linux) como intérprete/kernel.

Si preferís Jupyter Lab en el navegador:

```powershell
uv run --with jupyter jupyter lab
```

## Actualizar dependencias

Para actualizar el lockfile y sincronizar el entorno:

```powershell
$env:UV_PROJECT_ENVIRONMENT = ".venv_002a"
uv lock --upgrade
uv sync
```

`uv lock --upgrade` actualiza `uv.lock`, pero **no** actualiza `requirements.txt` automáticamente: ese archivo se generó una vez a partir del lock y queda desactualizado si no lo volvés a exportar. Después de sincronizar, correr también:

```powershell
uv export --format requirements.txt --no-hashes -o requirements.txt
```
