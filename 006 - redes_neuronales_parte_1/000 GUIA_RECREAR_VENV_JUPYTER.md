# Guía para borrar y recrear el entorno virtual de Jupyter

Este instructivo sirve para reiniciar el entorno virtual del proyecto cuando el `venv` existente quedó roto, desactualizado o querés partir de una instalación limpia.

## Archivos de dependencias que se van a usar

- `requirements.txt` en la raíz del proyecto.
- `007 - redes_neuronales_parte_2/requirements.txt`.

La idea es instalar primero las dependencias base del proyecto y después sumar las específicas de la unidad de redes neuronales parte 2.

## 1. Cerrar Jupyter y terminales activas

Antes de borrar nada:

- Cerrá Jupyter Lab o Jupyter Notebook.
- Cerrá cualquier terminal que esté usando el entorno virtual.
- Si tenés notebooks abiertos, guardalos primero.

## 2. Borrar el entorno virtual existente

Desde la raíz del proyecto, eliminá la carpeta `venv`.

### PowerShell

```powershell
Remove-Item -Recurse -Force .\venv
```

### CMD

```cmd
rmdir /s /q venv
```

Si tu entorno se llama `.venv` en lugar de `venv`, borrá esa carpeta con el mismo criterio.

## 3. Crear un entorno virtual nuevo

Usá el Python que tengas instalado en el sistema:

```bash
python -m venv venv
```

Si preferís mantener el nombre `.venv`, podés usar:

```bash
python -m venv .venv
```

## 4. Activar el entorno

### PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

### CMD

```cmd
venv\Scripts\activate.bat
```

### Git Bash / Linux / macOS

```bash
source venv/bin/activate
```

Cuando el entorno esté activo vas a ver algo como `(venv)` o `(.venv)` al inicio de la línea de la terminal.

## 5. Actualizar `pip`

Conviene dejar `pip` al día antes de instalar el resto:

```bash
python -m pip install --upgrade pip
```

## 6. Instalar las dependencias base

Primero instalá el `requirements.txt` principal del proyecto:

```bash
pip install -r requirements.txt
```

## 7. Instalar las dependencias de redes neuronales parte 2

Después agregá las dependencias específicas de la carpeta `007 - redes_neuronales_parte_2`:

```bash
pip install -r "007 - redes_neuronales_parte_2/requirements.txt"
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
python -m ipykernel install --user --name pdi-jupyter --display-name "PDI Jupyter"
```

Esto hace que el entorno aparezca con el nombre `PDI Jupyter` en el selector de kernels.

Si preferís otro nombre, podés cambiar:

- `--name`: identificador interno, sin espacios.
- `--display-name`: nombre visible que vas a ver en Jupyter y VS Code.

## 10. Verificación rápida

Si querés comprobar que el entorno quedó sano, ejecutá:

```bash
python -c "import jupyter, numpy; print('Entorno listo')"
```

## 11. Cómo encontrar el kernel en VS Code

En VS Code, abrí un notebook `.ipynb` y buscá el selector de kernel en la parte superior derecha.

Después:

- hacé clic en el nombre del kernel actual
- elegí `PDI Jupyter`

Si no aparece de entrada:

- revisá que el entorno esté activado e instalado correctamente
- volvé a ejecutar el comando `python -m ipykernel install ...`
- usá `Ctrl+Shift+P` y buscá `Python: Select Interpreter` para verificar que VS Code apunte al Python del entorno correcto

## Orden resumido

```bash
Remove-Item -Recurse -Force .\venv
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -r "007 - redes_neuronales_parte_2/requirements.txt"
python -m ipykernel install --user --name pdi-jupyter --display-name "PDI Jupyter"
jupyter lab
```

## Nota

Si encontrás conflictos entre versiones, la causa más común es que alguno de los dos archivos de dependencias pide paquetes con versiones incompatibles. En ese caso conviene revisar el error de instalación y resolverlo paquete por paquete.
