# Visión por Computadora — Parte 1 (OpenCV)

**Profesor Titular:** Matías Barreto — Especialista en Nuevos Medios e Interactividad

Material creado por el profesor para la materia PDI de IFTS Nº 24.

Bloque de OpenCV reorganizado en secuencia plana: espacios de color, formatos de archivo, ecualización, transformaciones geométricas, operaciones gráficas, filtros de suavizado, umbralización, morfología matemática, restauración/inpainting, contornos y coincidencia por plantilla, hasta detección de rostros con Haar. Esta carpeta puede usarse de forma independiente porque incluye su propia configuración de dependencias con `uv`.

## Contenido

- `001` a `010`: secuencia principal de OpenCV (espacios de color, formatos, ecualización, transformaciones, filtros, umbralización, morfología, restauración, contornos, plantillas, rostros).
- `Utilidades_y_Plantillas.ipynb`: caja de herramientas reutilizable para la unidad.
- `exploratorios/laboratorio guiado de exploracion - color, paleta y segmentacion.ipynb`: laboratorio guiado adicional.
- `Imagenes/`: imágenes de ejemplo usadas por los notebooks.

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

`uv sync` crea `.venv` con la versión de Python fijada en `.python-version` (3.12) e instala las versiones fijadas en `uv.lock`. El archivo `pyproject.toml` contiene las dependencias directas del laboratorio (numpy, opencv-python, pillow, matplotlib) más `ipykernel` para poder usar el entorno como kernel de Jupyter/VS Code.

### Registrar el kernel con nombre propio

Como vas a tener varios entornos virtuales (uno por carpeta), conviene registrar el kernel de este con un nombre identificable en vez de dejar el genérico "Python 3 (ipykernel)". Con el entorno ya sincronizado, ejecutar:

```powershell
.venv\Scripts\python.exe -m ipykernel install --user --name pdi-004-cv1 --display-name "PDI 004 - Computer Vision 1"
```

Esto registra el kernel en tu carpeta de Jupyter (con `--user`), así que va a aparecer en VS Code/Jupyter identificado como **"PDI 004 - Computer Vision 1"**, sin mezclarse con los kernels de las demás carpetas.

## Activar el entorno

En Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

En macOS o Linux:

```bash
source .venv/bin/activate
```

## Abrir los notebooks

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

`uv lock --upgrade` actualiza `uv.lock`, pero **no** actualiza `requirements.txt` automáticamente: ese archivo se generó una vez a partir del lock y queda desactualizado si no lo volvés a exportar. Después de sincronizar, correr también:

```powershell
uv export --format requirements.txt --no-hashes -o requirements.txt
```
