# Guía de entorno para `venv_facemesh`

Este instructivo sirve para usar el entorno virtual `venv_facemesh`, pensado para los notebooks de FaceMesh de la carpeta `008 - vision_artificial_aplicada`.

## Entorno de referencia

La versión instalada hoy en `venv_facemesh` incluye, entre otras, estas versiones clave:

- `mediapipe==0.10.14`
- `opencv-python==4.10.0.84`
- `numpy==1.26.4`
- `matplotlib==3.10.9`
- `scikit-image==0.25.2`
- `scipy==1.15.3`
- `protobuf==4.25.9`
- `jupyterlab==4.5.8`
- `ipykernel==7.2.0`

## Crear el entorno

Desde la raíz del proyecto:

```powershell
python -m venv venv_facemesh
```

## Activar el entorno

### PowerShell

```powershell
.\venv_facemesh\Scripts\Activate.ps1
```

### CMD

```cmd
venv_facemesh\Scripts\activate.bat
```

Cuando el entorno está activo vas a ver `venv_facemesh` al comienzo de la terminal.

## Instalar dependencias

Para instalar los paquetes, primero tenés que estar parado en la terminal dentro de `venv_facemesh` y después ejecutar el archivo de requisitos de la raíz:

```powershell
pip install -r requirements_facemesh.txt
```

Si querés replicar el estado actual del entorno, este archivo es la referencia que tenés que usar.

## Registrar el kernel

```powershell
python -m ipykernel install --user --name venv_facemesh --display-name "Facemesh"
```

## Verificar

```powershell
python -c "import mediapipe as mp; print(mp.__version__)"
```

