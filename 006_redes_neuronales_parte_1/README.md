# Unidad 006 — Redes Neuronales (Parte 1)

**Profesor Titular:** Matías Barreto — Especialista en Nuevos Medios e Interactividad

Material creado por el profesor para la materia PDI de IFTS Nº 24.

Colección de notebooks sobre redes neuronales: perceptrón y regresión, clasificación, redes convolucionales completas y un laboratorio de Teachable Machine con dataset propio desplegado en Gradio. Esta carpeta puede usarse de forma independiente porque incluye su propia configuración de dependencias con `uv`.

## Contenido

- `001_Red_Neuronal.ipynb`: fundamentos de red neuronal simple.
- `002_Clasificacion.ipynb`: clasificación con red densa.
- `003_CNNs_Full.ipynb`: redes convolucionales (CNN) completas.
- `004_Teachable_Machine_Dataset_Propio_Gradio.ipynb`: laboratorio integrador con dataset propio y despliegue en Gradio.
- `datos/celsius.csv`: datos de soporte usados por los notebooks.

## Requisitos

- Python 3.12 — [descarga oficial](https://www.python.org/downloads/).
- Git — [descarga oficial](https://git-scm.com/downloads).
- `uv` instalado y disponible en el PATH. Ver [cómo instalar uv](INSTALACION_UV.md).
- Visual Studio Code con las extensiones necesarias. Ver [cómo instalar VS Code y sus extensiones](INSTALACION_VSCODE.md).

> ✦ Esta unidad usa TensorFlow. La primera sincronización puede demorar varios minutos según la conexión.

## Crear el entorno

Desde esta carpeta, ejecutar:

```powershell
uv sync
```

`uv sync` crea `.venv` con la versión de Python fijada en `.python-version` (3.12) e instala las versiones fijadas en `uv.lock`. El archivo `pyproject.toml` contiene las dependencias directas del laboratorio (numpy, matplotlib, pandas, seaborn, scikit-learn, tensorflow, tensorflow-datasets, pillow, gradio, opencv-python-headless) más `ipykernel` para poder usar el entorno como kernel de Jupyter/VS Code.

### Registrar el kernel con nombre propio

Como vas a tener varios entornos virtuales (uno por carpeta), conviene registrar el kernel de este con un nombre identificable en vez de dejar el genérico "Python 3 (ipykernel)". Con el entorno ya sincronizado, ejecutar:

```powershell
.venv\Scripts\python.exe -m ipykernel install --user --name pdi-006-redes1 --display-name "PDI 006 - Redes Neuronales 1"
```

Esto registra el kernel en tu carpeta de Jupyter (con `--user`), así que va a aparecer en VS Code/Jupyter identificado como **"PDI 006 - Redes Neuronales 1"**, sin mezclarse con los kernels de las demás carpetas.

> Nota: en versiones anteriores de esta carpeta el kernel se registraba como `neural-networks-uv` ("Python (neural-networks-uv)"). Se renombró a `pdi-006-redes1` para seguir el mismo criterio de nombres que el resto de las carpetas del laboratorio.

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

## Librerías incluidas

- `numpy` / `pandas`: manejo numérico y de tablas.
- `matplotlib` / `seaborn`: visualización, incluyendo matrices de confusión.
- `scikit-learn`: métricas y herramientas de evaluación.
- `tensorflow` / `tensorflow-datasets`: construcción, entrenamiento y datasets (MNIST, EMNIST, cats_vs_dogs).
- `pillow`: manejo de imágenes.
- `gradio`: interfaces web para probar modelos.
- `opencv-python-headless`: procesamiento de imágenes sin interfaz gráfica.

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
