# Guía de entorno para la unidad 008

Este documento explica cómo preparar y usar el entorno virtual específico de la carpeta `008 - vision_artificial_aplicada/`.

El entorno esperado para esta unidad es:

`c:\Users\Cynthia\Desktop\ifts24-lab-pdi-2026-MATIAS\venv_mediapipe`

---

## 1. Requisitos previos

- Python 3.10 o superior.
- `pip` disponible en tu instalación de Python.
- Acceso a Internet para instalar las dependencias.

---

## 2. Crear y Activar el entorno

Si todavía no existe, primero crealo desde la raíz del proyecto con:

```powershell
python -m venv venv_mediapipe
```

Luego activalo:

### Windows PowerShell

Desde la raíz del proyecto:

```powershell
.\venv_mediapipe\Scripts\Activate.ps1
```

### Windows CMD

```cmd
venv_mediapipe\Scripts\activate.bat
```

Cuando el entorno está activo, vas a ver algo como `venv_mediapipe` al inicio de la terminal.

### Opcional: registrar un kernel con nombre personalizado

Si querés que Jupyter muestre este entorno con un nombre más claro, instalá `ipykernel` y registrá el kernel con un nombre personalizado:

```powershell
python -m pip install ipykernel
python -m ipykernel install --user --name mediapipe-008 --display-name "Python (MediaPipe 008)"
```

- `--name` define el identificador interno del kernel.
- `--display-name` define el nombre visible en JupyterLab, VS Code y otras herramientas.

Si más adelante querés cambiar el nombre visible, podés repetir el segundo comando con otro `--display-name`.

---

## 3. Instalar dependencias

Ubicate dentro de la carpeta de la unidad:

```powershell
cd "008 - vision_artificial_aplicada"
```

Luego instalá las dependencias de este material:

```powershell
python -m pip install -r requirements.txt
```

Si preferís hacerlo desde la raíz del proyecto sin cambiar de carpeta, también sirve:

```powershell
python -m pip install -r "008 - vision_artificial_aplicada\requirements.txt"

```

---

## 4. Verificar que MediaPipe quedó instalado

Podés comprobarlo con:

```powershell
python -c "import mediapipe as mp; print(mp.__version__)"
```

Si ese comando imprime una versión, el entorno quedó listo.

---


## 5. Paquetes principales de esta unidad

- `mediapipe`: detección de manos, rostro y pose.
- `opencv-python-headless`: lectura y procesamiento de imágenes y video.
- `gradio`: interfaces web simples para demos.
- `numpy`: operaciones numéricas.
- `matplotlib`: visualización.
- `jupyterlab`: ejecución de notebooks.

---

