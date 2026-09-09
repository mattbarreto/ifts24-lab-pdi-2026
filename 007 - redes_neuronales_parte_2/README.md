# Unidad 007 — Redes Neuronales (Parte 2)

**Tecnicatura Superior en Ciencias de Datos e IA — IFTS24**  
Laboratorio de Tecnologías de la Imagen Digital · Matías Barreto, 2026

Colección de 10 notebooks que cubren redes neuronales densas, redes convolucionales, modelos preentrenados, Hugging Face, despliegue con Gradio y OCR crítico.

---

## Contenido

| Notebook | Tema |
|---|---|
| `01_Fundamentos_Red_Neuronal_Simple` | Perceptrón, propagación hacia adelante y función de pérdida |
| `02_Clasificacion_Letras_MLP` | Red densa (MLP) sobre el dataset EMNIST |
| `03_Clasificacion_Letras_CNN` | Red convolucional (CNN) sobre EMNIST |
| `04_Visualizacion_Filtros_y_Activaciones_CNN` | Interpretabilidad: filtros y mapas de activación |
| `05_Clasificacion_Preentrenados_ResNet18` | Inferencia con ResNet18 preentrenada (PyTorch) |
| `06_Transfer_Learning_MobileNetV2` | Transfer Learning con MobileNetV2 (Keras / TensorFlow) |
| `07_Modelos_Preentrenados_HuggingFace` | ViT, CLIP y DETR desde 🤗 Transformers |
| `08_Laboratorio_Desarrollo_Space_Gradio` | De Jupyter Notebook a Hugging Face Space con Gradio |
| `09_Laboratorio_Integrador_Redes` | Proyecto integrador de la unidad |
| `10_Laboratorio_OCR_Investigacion_Critica` | OCR con modelos de IA y análisis crítico de los resultados |

La carpeta `datos/` contiene los archivos de soporte usados por los notebooks (imágenes de ejemplo, datasets locales).

---

## Cómo descargar esta carpeta

Esta es una subcarpeta dentro de un repositorio más grande. Para descargarla sola, sin clonar todo el repositorio, hay dos herramientas web gratuitas que no requieren registro:

### Opción 1 — Download Directory

Una de las opciones más limpias y directas:

1. Copiá el enlace completo de esta carpeta en GitHub o Hugging Face.
2. Entrá en **[download-directory.github.io](https://download-directory.github.io)**.
3. Pegá la URL en el cuadro de búsqueda y presioná Enter.
4. Se va a descargar automáticamente un archivo `.zip` con únicamente esta carpeta y todos sus archivos.

### Opción 2 — DownGit

Alternativa clásica y muy confiable:

1. Entrá en **[downgit.github.io](https://downgit.github.io)**.
2. Pegá el enlace de la carpeta en el campo que dice *GitHub URL*.
3. Hacé clic en el botón **Download**.

---

## Configuración del entorno local

Esta carpeta incluye su propia configuración de dependencias con `uv` (`pyproject.toml` + `uv.lock`), para poder usarse de forma independiente y reproducible.

### Requisitos previos

- **Python 3.12** — [descarga oficial](https://www.python.org/downloads/).
- Git — [descarga oficial](https://git-scm.com/downloads).
- `uv` instalado y disponible en el PATH. Ver [cómo instalar uv](INSTALACION_UV.md).
- Visual Studio Code con las extensiones necesarias. Ver [cómo instalar VS Code y sus extensiones](INSTALACION_VSCODE.md).

> ✦ Esta unidad usa TensorFlow y PyTorch simultáneamente. La primera sincronización puede
> demorar varios minutos dependiendo de la conexión. Se recomienda una conexión
> estable y al menos 5 GB de espacio libre en disco.

---

### Paso 1 — Crear el entorno

Desde esta carpeta, ejecutar:

```powershell
uv sync
```

`uv sync` crea `.venv` con la versión de Python fijada en `.python-version` (3.12) e instala las versiones fijadas en `uv.lock` (numpy, pandas, seaborn, scikit-learn, requests, pillow, tensorflow, tensorflow-datasets, torch, torchvision, transformers, datasets, gradio, opencv-python-headless, más `ipykernel`).

---

### Paso 2 — Registrar el kernel con nombre propio

Como vas a tener varios entornos virtuales (uno por carpeta), conviene registrar el kernel de este con un nombre identificable en vez de dejar el genérico "Python 3 (ipykernel)":

```powershell
.venv\Scripts\python.exe -m ipykernel install --user --name pdi-007-redes2 --display-name "PDI 007 - Redes Neuronales 2"
```

Así va a aparecer en VS Code/Jupyter identificado como **"PDI 007 - Redes Neuronales 2"**, sin mezclarse con los kernels de las demás carpetas.

---

### Paso 3 — Activar el entorno

**Linux / macOS:**
```bash
source .venv/bin/activate
```

**Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

El prompt de la terminal va a mostrar `(.venv)` cuando el entorno esté activo.

---

### Paso 4 — Abrir los notebooks

La forma recomendada es VS Code (ver [instalación y selección del kernel](INSTALACION_VSCODE.md)): abrir esta carpeta en VS Code y seleccionar `.venv\Scripts\python.exe` (Windows) o `.venv/bin/python` (macOS/Linux) como intérprete/kernel.

Si preferís Jupyter Lab en el navegador:

```powershell
uv run --with jupyter jupyter lab
```

---

### Actualizar dependencias

```powershell
uv lock --upgrade
uv sync
```

`uv lock --upgrade` actualiza `uv.lock`, pero **no** actualiza `requirements.txt` automáticamente: ese archivo se generó una vez a partir del lock y queda desactualizado si no lo volvés a exportar. Después de sincronizar, correr también:

```powershell
uv export --format requirements.txt --no-hashes -o requirements.txt
```

---

## Notas importantes

**Sobre `from google.colab import ...`**  
Algunos notebooks tienen líneas como `from google.colab import drive` o `from google.colab import files`. Esas líneas son específicas de Google Colab y van a generar un error al ejecutarse localmente. Se pueden comentar o eliminar — solo afectan la subida de archivos en Colab y no alteran la lógica del notebook.

**Sobre GPU**  
Los notebooks funcionan en CPU, pero el entrenamiento de redes convolucionales (notebooks 03 y 06) va a ser considerablemente más lento sin GPU. Para acelerar, podés usar Google Colab (gratuito con GPU) o una máquina con CUDA.

**Sobre versiones de Python**  
Este entorno está fijado en Python 3.12 (`.python-version`) y `uv.lock` ya confirma que TensorFlow, PyTorch y Transformers resuelven correctamente en esa versión.

**Sobre la carpeta `datos/`**  
La carpeta `datos/` debe estar en el mismo nivel que los notebooks. Si la descarga sola (sin el resto de la carpeta), algunos notebooks no van a encontrar los archivos de ejemplo. Download Directory y DownGit descargan la carpeta completa, incluyendo `datos/`.

---

## Desactivar el entorno cuando terminás

```bash
deactivate
```
