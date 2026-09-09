# Unidad 008 — Visión Artificial Aplicada

**Tecnicatura Superior en Ciencias de Datos e IA — IFTS24**  
Laboratorio de Tecnologías de la Imagen Digital · Matías Barreto, 2026

Colección de notebooks sobre detección de puntos clave, control gestual e integración de modelos de visión con interfaces web, usando MediaPipe y Gradio.

---

## Contenido

| Notebook | Tema |
|---|---|
| `01_Detección_Puntos_Clave_Faciales` | Face Mesh: 478 landmarks faciales sobre imagen estática |
| `02_Control_Volumen_con_Manos` | Hand Landmarker: control de volumen en tiempo real por gestos |
| `03_Integración_Gradio_y_MediaPipe` | Gradio (Interface / Blocks) + MediaPipe · concepto de Skills |
| `04_Proyecto_Pose_y_Despliegue` | Proyecto integrador: Pose estimation + deploy en HF Spaces + GitHub |

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

> ✦ Esta unidad tiene dependencias livianas comparadas con la 007. La sincronización demora aproximadamente 2–5 minutos.

---

### Paso 1 — Crear el entorno

Desde esta carpeta, ejecutar:

```powershell
uv sync
```

`uv sync` crea `.venv` con la versión de Python fijada en `.python-version` (3.12) e instala las versiones fijadas en `uv.lock` (mediapipe, opencv-python-headless, gradio, numpy, matplotlib, más `ipykernel`). En Windows también instala automáticamente `pycaw` y `comtypes` (necesarios solo para el notebook 02, ver más abajo); en Linux/macOS se omiten solos.

---

### Paso 2 — Registrar el kernel con nombre propio

Como vas a tener varios entornos virtuales (uno por carpeta), conviene registrar el kernel de este con un nombre identificable en vez de dejar el genérico "Python 3 (ipykernel)":

```powershell
.venv\Scripts\python.exe -m ipykernel install --user --name pdi-008-vision-aplicada --display-name "PDI 008 - Vision Artificial Aplicada"
```

Así va a aparecer en VS Code/Jupyter identificado como **"PDI 008 - Vision Artificial Aplicada"**, sin mezclarse con los kernels de las demás carpetas.

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

---

## Nota para el notebook 02 — Control de volumen (solo Windows)

El notebook `02_Control_Volumen_con_Manos` usa la API de audio del sistema para controlar el volumen. Los paquetes `pycaw` y `comtypes` que necesita ya están declarados en `pyproject.toml` con marcador `sys_platform == 'win32'`, así que `uv sync` los instala automáticamente en Windows y los omite en Linux/macOS sin que haga falta instalar nada aparte.

En Linux y macOS el loop de detección de manos va a funcionar, pero el control de volumen del sistema no está disponible sin configuración adicional.

---

## Nota para el notebook 04 — Proyecto de deploy

El notebook `04_Proyecto_Pose_y_Despliegue` genera una carpeta con los archivos `app.py` y `requirements.txt` listos para subir a Hugging Face Spaces. Para el deploy necesitás:

- Una cuenta gratuita en [huggingface.co](https://huggingface.co)
- Git instalado en el sistema
- (Opcional) Una cuenta en [github.com](https://github.com) para el repositorio de código

El proceso de deploy completo está documentado en el Cheatsheet de Extras:  
`Extras/Guias/HuggingFace-Spaces/Cheatsheet_Desarrollo_Space.ipynb`

---

## Desactivar el entorno cuando terminás

```bash
deactivate
```
