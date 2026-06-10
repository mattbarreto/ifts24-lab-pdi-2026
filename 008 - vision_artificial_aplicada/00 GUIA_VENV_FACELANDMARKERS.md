# Guía de entorno para `venv_facelandmarkers`

Este instructivo sirve para usar el entorno virtual `venv_facelandmarkers`, pensado para los notebooks de Face Landmarker de la carpeta `008 - vision_artificial_aplicada`.

## Entorno de referencia

La versión instalada hoy en `venv_facelandmarkers` incluye, entre otras, estas versiones clave:

- `mediapipe==0.10.35`
- `opencv-python==4.13.0.92`
- `numpy==2.2.6`
- `matplotlib==3.10.9`
- `scikit-image==0.25.2`
- `scipy==1.15.3`
- `protobuf==3.20.3`
- `jupyterlab==4.5.8`
- `ipykernel==7.2.0`

## Crear el entorno

Desde la raíz del proyecto:

```powershell
python -m venv venv_facelandmarkers
```

## Activar el entorno

### PowerShell

```powershell
.\venv_facelandmarkers\Scripts\Activate.ps1
```

### CMD

```cmd
venv_facelandmarkers\Scripts\activate.bat
```

Cuando el entorno está activo vas a ver `venv_facelandmarkers` al comienzo de la terminal.

## Instalar dependencias

Para instalar los paquetes, primero tenés que estar parado en la terminal dentro de `venv_facelandmarkers` y después ejecutar el archivo de requisitos de la raíz:

```powershell
pip install -r requirements_facelandmarkers.txt
```

Si querés replicar el estado actual del entorno, este archivo es la referencia que tenés que usar.

## Registrar el kernel

```powershell
python -m ipykernel install --user --name venv_facelandmarkers --display-name "Facelandmarkers"
```

## Verificar

```powershell
python -c "import mediapipe as mp; print(mp.__version__)"
```

