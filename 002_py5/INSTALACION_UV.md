# Instalación de uv

`uv` es el gestor de proyectos y dependencias de Python utilizado por este laboratorio.

## Windows

Abrir PowerShell y ejecutar el instalador oficial:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Cerrar y volver a abrir la terminal. Comprobar la instalación:

```powershell
uv --version
```

También se puede consultar la [documentación oficial de instalación de uv](https://docs.astral.sh/uv/getting-started/installation/).

## macOS y Linux

Abrir una terminal y ejecutar:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Reabrir la terminal y comprobar la instalación:

```bash
uv --version
```

## Uso en este laboratorio

Desde la carpeta que contiene este archivo. Esta carpeta usa `.venv_002` en vez de `.venv` genérico (para distinguirla de las demás carpetas del laboratorio), así que primero seteamos esa ruta con la variable `UV_PROJECT_ENVIRONMENT`:

```powershell
$env:UV_PROJECT_ENVIRONMENT = ".venv_002"
uv venv .venv_002 --python 3.12
uv sync
```

El archivo `uv.lock` fija las versiones exactas para que todas las instalaciones sean reproducibles.

> ⚠️ `UV_PROJECT_ENVIRONMENT` solo dura mientras esa terminal esté abierta. Si cerrás la terminal y abrís otra para correr `uv sync`, `uv run` o `uv lock` en esta carpeta, hay que volver a setear la variable antes (`$env:UV_PROJECT_ENVIRONMENT = ".venv_002"`) — si no, uv va a crear un `.venv` genérico nuevo en vez de usar `.venv_002`.

### Registrar el kernel con nombre propio

Si vas a usar varios entornos virtuales a la vez (uno por carpeta del laboratorio), registrá el kernel de este con un nombre identificable en vez del genérico "Python 3 (ipykernel)":

```powershell
.venv_002\Scripts\python.exe -m ipykernel install --user --name pdi-002-py5-fundamentos --display-name "PDI 002 - Py5 Fundamentos"
```

Así aparece en el selector de kernel de VS Code/Jupyter como **"PDI 002 - Py5 Fundamentos"**, distinguible de los kernels de las otras carpetas.
