"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║              INTRODUCCIÓN A PY5: Tu primer sketch                             ║
╚═══════════════════════════════════════════════════════════════════════════════╝

¿QUÉ ES PY5?
════════════════════════════════════════════════════════════════════════════════

py5 es una librería de Python que nos permite crear gráficos interactivos.
Está basada en Processing (un lenguaje de programación visual creado en MIT).

py5 es ideal para:
  • Aprender programación de manera visual
  • Crear arte generativo (arte creado con código)
  • Procesar imágenes y video
  • Prototipado rápido de ideas visuales
  • Enseñanza de conceptos de PDI (Procesamiento Digital de Imágenes)

CONCEPTOS FUNDAMENTALES
════════════════════════════════════════════════════════════════════════════════

1. CANVAS (Lienzo): área donde dibujamos, ventana 2D
2. setup(): función que se ejecuta una sola vez al iniciar
3. draw(): función que se ejecuta continuamente (~60 veces/segundo)
4. FORMAS: rect(), circle(), line(), point(), triangle()
5. PROPIEDADES: fill(), stroke(), stroke_weight(), background()

¿CÓMO USAR COLORES?
════════════════════════════════════════════════════════════════════════════════

1. Escala de grises (0-255): py5.fill(0) = negro, py5.fill(255) = blanco
2. RGB: py5.fill(255, 0, 0) = rojo puro
3. Hexadecimal: py5.fill("#FF0000") = rojo
"""

# ════════════════════════════════════════════════════════════════════════════
# IMPORTAR LIBRERÍAS NECESARIAS
# ════════════════════════════════════════════════════════════════════════════

import py5              # Importar py5 para usar sus funciones de gráficos
from pathlib import Path  # Para manejar rutas de archivos de forma segura


# ════════════════════════════════════════════════════════════════════════════
# FUNCIÓN ESPECIAL: setup()
# ════════════════════════════════════════════════════════════════════════════

def setup():
    """
    Se ejecuta UNA SOLA VEZ cuando inicia el programa.
    Configuramos aquí el tamaño de ventana y propiedades iniciales.
    """
    
    # PASO 1: Crear una ventana de 500×500 píxeles
    py5.size(500, 500)
    
    # PASO 2: Establecer el color de relleno (verde claro)
    py5.fill("#00D92F")
    
    # PASO 3: Dibujar un rectángulo
    # Parámetros: (x, y, ancho, alto)
    # (150, 150) es la esquina superior izquierda
    py5.rect(150, 150, 200, 200)
    
    # PASO 4: Guardar la imagen resultante
    # Crear el directorio si no existe (parents=True, exist_ok=True)
    output_dir = Path("img/testing")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Guardar el archivo PNG
    output_path = output_dir / "000_intro_py5.png"
    py5.save(str(output_path))
    
    print(f"✓ Imagen guardada en: {output_path}")


# ════════════════════════════════════════════════════════════════════════════
# FUNCIÓN ESPECIAL: draw() (OPCIONAL)
# ════════════════════════════════════════════════════════════════════════════

def draw():
    """
    Se ejecuta continuamente (~60 veces/segundo).
    En este ejemplo no la usamos (solo dibujamos una vez).
    """
    pass


# ════════════════════════════════════════════════════════════════════════════
# EJECUTAR EL SKETCH
# ════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    """
    Verifica que el script se ejecuta directamente (no importado).
    py5.run_sketch() inicia el programa y abre la ventana.
    """
    py5.run_sketch()


# ════════════════════════════════════════════════════════════════════════════
# NOTAS
# ════════════════════════════════════════════════════════════════════════════

"""
ERRORES COMUNES Y SOLUCIONES:

1. Error: "No such file or directory: img/testing"
   Solución: Usamos mkdir(parents=True, exist_ok=True)
            Esto crea el directorio automáticamente si no existe

2. Error: "No module named 'py5'"
   Solución: Instalar con: pip install py5

3. ¿No aparece la ventana?
   - En local: debería aparecer una ventana
   - En Colab: usa py5_tools.screenshot() para ver la imagen
   - En Jupyter: la imagen se guardó en img/testing/

PRÓXIMOS PASOS:

1. Modificar colores: py5.fill("#FF0000") para rojo
2. Cambiar tamaño: py5.size(800, 600)
3. Agregar más formas:
   py5.circle(250, 250, 100)
   py5.line(0, 0, 500, 500)
4. Ver: 001_basico.py para interactividad con mouse

RECURSOS:
https://py5coding.org/
"""
