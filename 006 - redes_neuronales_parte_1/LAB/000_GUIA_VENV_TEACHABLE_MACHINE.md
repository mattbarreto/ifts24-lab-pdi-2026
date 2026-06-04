# Guía de entorno exclusivo para Teachable Machine

Este instructivo sirve para crear un entorno virtual separado, dedicado solo al notebook `004_Teachable_Machine_Dataset_Propio_Gradio.ipynb`.

## Objetivo

Usar un entorno aislado evita mezclar dependencias con el resto de los notebooks de redes neuronales.

## Versión recomendada

Para que `keras_model.h5` cargue sin el error de `DepthwiseConv2D`, este entorno debe quedar con:

- `tensorflow==2.15.*`
- `keras==2.15.*`

## Nombre del entorno

Usá este nombre para no confundirlo con otros entornos del proyecto:

- carpeta del entorno: `venv_teachable`
- kernel de Jupyter: `PDI Teachable Machine`

Si estas dentro de un venv, sali con .\deactivate

## 1. Crear el entorno

Desde la carpeta `006 - redes_neuronales_parte_1/LAB`, ejecutá:

```powershell
python -m venv venv_teachable
```

## 2. Activarlo

### PowerShell

```powershell
.\venv_teachable\Scripts\Activate.ps1
```

### CMD

```cmd
venv_teachable\Scripts\activate.bat
```

## 3. Instalar dependencias mínimas

Instalá solo lo necesario para este notebook:

```powershell
python -m pip install --upgrade pip
pip install "tensorflow==2.15.*" "keras==2.15.*" gradio pillow numpy
pip install ipykernel
```

## 4. Registrar el kernel

```powershell
python -m ipykernel install --user --name pdi-teachable-machine --display-name "PDI Teachable Machine"
```

REINICIA EL VISUAL STUDIO CODE (CERRA EL PROGRAMA Y VOLVE A ABRIR)

## 5. Usarlo en el notebook

Abrí `004_Teachable_Machine_Dataset_Propio_Gradio.ipynb` y elegí:

`PDI Teachable Machine`

