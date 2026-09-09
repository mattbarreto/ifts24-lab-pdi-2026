# Introducción a scikit-image, Histogramas y Umbrales

**Profesor Titular:** Matías Barreto — Especialista en Nuevos Medios e Interactividad

Material creado por el profesor para la materia PDI de IFTS Nº 24.

Secuencia de 3 notebooks que introducen `scikit-image` y NumPy sobre imágenes de ejemplo incluidas en la propia librería (`skimage.data`), avanzando desde la estructura de una imagen digital hasta los histogramas y la umbralización (thresholding). Esta carpeta puede usarse de forma independiente porque incluye su propia configuración de dependencias con `uv`.

## Contenido

- `01_intro_pdi_scikit_image_y_numpy.ipynb`: introducción al procesamiento digital de imágenes con scikit-image y NumPy.
- `02_histogramas.ipynb`: histogramas como "huella" de una imagen.
- `03_umbrales.ipynb`: umbralización (thresholding) para separar objetos del fondo.

No requieren imágenes propias: usan los datasets de ejemplo incluidos en `skimage.data` (rocket, moon, coins, page).

## Requisitos

- Python 3.12 — [descarga oficial](https://www.python.org/downloads/).
- Git — [descarga oficial](https://git-scm.com/downloads).
- `uv` instalado y disponible en el PATH. Ver [cómo instalar uv](INSTALACION_UV.md).
- Visual Studio Code con las extensiones necesarias. Ver [cómo instalar VS Code y sus extensiones](INSTALACION_VSCODE.md).

## Crear el entorno

Desde esta carpeta, ejecutar:

```powershell
$env:UV_PROJECT_ENVIRONMENT = ".venv_002b"
uv venv .venv_002b --python 3.12
uv sync
```

> ⚠️ `UV_PROJECT_ENVIRONMENT` solo dura mientras esa terminal esté abierta. Si cerrás la terminal y abrís otra para correr `uv sync`, `uv run` o `uv lock` en esta carpeta, hay que volver a setear la variable antes (`$env:UV_PROJECT_ENVIRONMENT = ".venv_002b"`) — si no, uv va a crear un `.venv` genérico nuevo en vez de usar `.venv_002b`.

`uv sync` crea `.venv_002b` con la versión de Python fijada en `.python-version` (3.12) e instala las versiones fijadas en `uv.lock`. El archivo `pyproject.toml` contiene las dependencias directas del laboratorio (numpy, matplotlib, scikit-image) más `ipykernel` para poder usar el entorno como kernel de Jupyter/VS Code.

### Registrar el kernel con nombre propio

Como vas a tener varios entornos virtuales (uno por carpeta), conviene registrar el kernel de este con un nombre identificable en vez de dejar el genérico "Python 3 (ipykernel)". Con el entorno ya sincronizado, ejecutar:

```powershell
.venv_002b\Scripts\python.exe -m ipykernel install --user --name pdi-002b-histogramas-umbrales --display-name "PDI 002b - Histogramas y Umbrales"
```

Esto registra el kernel en tu carpeta de Jupyter (con `--user`), así que va a aparecer en VS Code/Jupyter identificado como **"PDI 002b - Histogramas y Umbrales"**, sin mezclarse con los kernels de las demás carpetas.

## Activar el entorno

En Windows PowerShell:

```powershell
.venv_002b\Scripts\Activate.ps1
```

En macOS o Linux:

```bash
source .venv_002b/bin/activate
```

## Abrir los notebooks

La forma recomendada es VS Code (ver [instalación y selección del kernel](INSTALACION_VSCODE.md)): abrir esta carpeta en VS Code y seleccionar `.venv_002b\Scripts\python.exe` (Windows) o `.venv_002b/bin/python` (macOS/Linux) como intérprete/kernel.

Si preferís Jupyter Lab en el navegador:

```powershell
uv run --with jupyter jupyter lab
```

## Actualizar dependencias

Para actualizar el lockfile y sincronizar el entorno:

```powershell
$env:UV_PROJECT_ENVIRONMENT = ".venv_002b"
uv lock --upgrade
uv sync
```

`uv lock --upgrade` actualiza `uv.lock`, pero **no** actualiza `requirements.txt` automáticamente: ese archivo se generó una vez a partir del lock y queda desactualizado si no lo volvés a exportar. Después de sincronizar, correr también:

```powershell
uv export --format requirements.txt --no-hashes -o requirements.txt
```
