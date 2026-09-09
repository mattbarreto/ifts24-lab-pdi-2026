# Fundamentos de py5

**Profesor Titular:** Matías Barreto — Especialista en Nuevos Medios e Interactividad

Material creado por el profesor para la materia PDI de IFTS Nº 24.

Unidad de fundamentos teóricos y prácticos con `py5` (Processing para Python), con versiones para Google Colab y para entorno local. Incluye el laboratorio de la cámara oscura. Esta carpeta puede usarse de forma independiente porque incluye su propia configuración de dependencias con `uv`.

## Contenido

- `00_setup_colab.ipynb`: configuración del entorno en Google Colab.
- `02a_fundamentos_teoria_colab.ipynb` / `02a_fundamentos_teoria_local.ipynb`: teoría de fundamentos (versión Colab y versión local).
- `02b_fundamentos_practica_local.ipynb`: práctica de fundamentos en entorno local.
- `02c_laboratorio_fundamentos.ipynb`: laboratorio "La cámara oscura".

## Requisitos

- Python 3.12 — [descarga oficial](https://www.python.org/downloads/).
- **Java (JDK)** — `py5` lo necesita para correr Processing por debajo. El paquete `install-jdk` (dependencia de este proyecto) puede instalar un JDK automáticamente si hace falta; ver también la [guía oficial de instalación de py5](https://py5coding.org/content/install.html).
- Git — [descarga oficial](https://git-scm.com/downloads).
- `uv` instalado y disponible en el PATH. Ver [cómo instalar uv](INSTALACION_UV.md).
- Visual Studio Code con las extensiones necesarias. Ver [cómo instalar VS Code y sus extensiones](INSTALACION_VSCODE.md).

## Crear el entorno

Desde esta carpeta, ejecutar:

```powershell
uv sync
```

`uv sync` crea `.venv` con la versión de Python fijada en `.python-version` (3.12) e instala las versiones fijadas en `uv.lock`. El archivo `pyproject.toml` contiene las dependencias directas del laboratorio (`py5`, `install-jdk`) más `ipykernel` para poder usar el entorno como kernel de Jupyter/VS Code.

### Registrar el kernel con nombre propio

Como vas a tener varios entornos virtuales (uno por carpeta), conviene registrar el kernel de este con un nombre identificable en vez de dejar el genérico "Python 3 (ipykernel)". Con el entorno ya sincronizado, ejecutar:

```powershell
.venv\Scripts\python.exe -m ipykernel install --user --name pdi-002-py5-fundamentos --display-name "PDI 002 - Py5 Fundamentos"
```

Esto registra el kernel en tu carpeta de Jupyter (con `--user`), así que va a aparecer en VS Code/Jupyter identificado como **"PDI 002 - Py5 Fundamentos"**, sin mezclarse con los kernels de las demás carpetas.

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

La forma recomendada es VS Code (ver [instalación y selección del kernel](INSTALACION_VSCODE.md)): abrir esta carpeta en VS Code y seleccionar `.venv\Scripts\python.exe` (Windows) o `.venv/bin/python` (macOS/Linux) como intérprete/kernel. Usar las versiones `_local` de los notebooks; las versiones `_colab` son para Google Colab.

Si preferís Jupyter Lab en el navegador:

```powershell
uv run --with jupyter jupyter lab
```

## Actualizar dependencias

Para actualizar el lockfile y sincronizar el entorno:

```powershell
uv lock --upgrade
uv sync
```
