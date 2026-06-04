# Guía para crear un entorno virtual exclusivo y separado para redes neuronales

Este instructivo sirve para crear un entorno virtual exclusivo del proyecto de redes neuronales, separado de cualquier otro `venv`, cuando querés partir de una instalación limpia.

## Archivos de dependencias que se van a usar

- `requirements.txt` en la raíz del proyecto.
- `007 - redes_neuronales_parte_2/requirements.txt`.

## Versión recomendada para este laboratorio

La idea es instalar primero las dependencias base del proyecto y después sumar las específicas de la unidad de redes neuronales parte 2, manteniendo este entorno aislado del anterior. Este entorno cubre todos los notebooks de `006 - redes_neuronales_parte_1` y `007 - redes_neuronales_parte_2`, excepto `004_Teachable_Machine_Dataset_Propio_Gradio.ipynb`, que sigue usando su propio `venv`.

## 1. Cerrar Jupyter y terminales activas

Antes de borrar nada:

- Cerrá Jupyter Lab o Jupyter Notebook.
- Cerrá cualquier terminal que esté usando el entorno virtual anterior.
- Si tenés notebooks abiertos, guardalos primero.
- Sali del entorno virtual con deactivate

## 2. Borrar el entorno virtual anterior (OPCIONAL) 

Si no queres borrar el entorno viejo, saltea este paso

Desde la raíz del proyecto, eliminá la carpeta del entorno anterior.

        ### PowerShell

        ```powershell
        Remove-Item -Recurse -Force .\venv
        ```

        ### CMD

        ```cmd
        rmdir /s /q venv
        ```

        Si tu entorno anterior se llama `.venv` en lugar de `venv`, borrá esa carpeta con el mismo criterio.

## 3. Crear un entorno virtual nuevo y exclusivo

Parate desde terminal en la carpeta donde vas a crear el venv.
Usá el Python que tengas instalado en el sistema:

```bash
python -m venv venv_redes_neuronales
```

Si preferís mantener el formato oculto, podés usar:

```bash
python -m venv .venv_redes_neuronales
```

## 4. Activar el entorno

### PowerShell

```powershell
.\venv_redes_neuronales\Scripts\Activate.ps1
```

### CMD

```cmd
venv_redes_neuronales\Scripts\activate.bat
```

### Git Bash / Linux / macOS

```bash
source venv_redes_neuronales/bin/activate
```

Cuando el entorno esté activo vas a ver algo como `(venv_redes_neuronales)` al inicio de la línea de la terminal.

## 5. Actualizar `pip`

Conviene dejar `pip` al día antes de instalar el resto:

```bash
python -m pip install --upgrade pip
```

## 6. Instalar las dependencias base

Primero instalá las dependencias base:

```bash
pip install -r requirements.txt
```

## 7. Instalar las dependencias de redes neuronales parte 2

Después agregá las dependencias específicas de la carpeta `007 - redes_neuronales_parte_2`.

Ese archivo incluye las librerías de deep learning, visión artificial, Hugging Face y Jupyter que necesitan los notebooks de la parte 2. Para mantener compatibilidad con los modelos guardados y con los cuadernos de esta unidad, fijá TensorFlow y Keras en 2.15 antes o después de instalar el resto:

```bash
pip install -r "007 - redes_neuronales_parte_2/requirements.txt"
pip install -q tfds-nightly
pip install -q tensorflow-datasets
```

## 8. Verificar Jupyter

Probá que Jupyter quedó disponible:

```bash
jupyter lab
```

Si preferís la interfaz clásica:

```bash
jupyter notebook
```

## 9. Registrar el kernel con un nombre personalizado

Para poder identificar este entorno fácilmente desde Jupyter y VS Code, registrá el kernel con un nombre propio.

Ejemplo recomendado:

```bash
python -m ipykernel install --user --name pdi-redes-neuronales --display-name "PDI Redes Neuronales"
```

Esto hace que el entorno aparezca con el nombre `PDI Redes Neuronales` en el selector de kernels.

Una vez cambiado el nombre, cerra VSC y volve a abrir

Cada vez que quieras usar este entorno cambia el entorno en la terminal y en el notebook.


## Nota

Si encontrás conflictos entre versiones, la causa más común es que alguno de los dos archivos de dependencias pide paquetes con versiones incompatibles. En ese caso conviene revisar el error de instalación y resolverlo paquete por paquete, pero este entorno está pensado para cubrir todo lo necesario de redes neuronales 1 y 2 sin incluir el notebook de Teachable Machine.

## Librerías incluidas

Este entorno deja disponibles, entre otras, estas librerías para los notebooks de redes neuronales 1 y 2:

- `opencv-python-headless`
- `seaborn`
- `tensorflow`
- `pandas`
- `matplotlib`
- `numpy`
- `Pillow` / `PIL`
- `torchvision`
- `torch`
- `transformers`
- `gradio`
- `scikit-learn`
- `tensorflow-datasets`
- `requests`
- `jupyter`
- `ipykernel`
