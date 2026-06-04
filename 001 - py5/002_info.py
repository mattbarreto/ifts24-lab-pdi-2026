"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║        PASO 2: Información de la ventana - Propiedades de py5                 ║
╚═══════════════════════════════════════════════════════════════════════════════╝

¿QUÉ APRENDERÁS?
════════════════════════════════════════════════════════════════════════════════
- Acceder a las propiedades de la ventana (width, height)
- Calcular información sobre píxeles
- Usar variables de py5 en tu código
- Concept: Resolución de pantalla

PRÁCTICA ANTERIOR
════════════════════════════════════════════════════════════════════════════════
En 001_basico.py aprendiste:
- setup() se ejecuta una sola vez
- draw() se ejecuta en loop
- Dibujar formas: ellipse(), fill(), no_stroke()

NOVEDAD EN ESTE SCRIPT
════════════════════════════════════════════════════════════════════════════════
- py5.width: variable que contiene el ANCHO de la ventana
- py5.height: variable que contiene el ALTO de la ventana
- Estas variables son AUTOMÁTICAS después de py5.size()
- Puedes usarlas para centrar elementos, hacer cálculos, etc.
"""

import py5


# ════════════════════════════════════════════════════════════════════════════
# CONFIGURACIÓN INICIAL
# ════════════════════════════════════════════════════════════════════════════

def setup():
    """
    Crear una ventana y obtener información sobre ella.
    """
    # Crear ventana de resolución 800×600 (HD 4:3)
    # Hay varias resoluciones comunes:
    #   - 400×400 (cuadrado)
    #   - 640×480 (VGA clásica)
    #   - 800×600 (SVGA)
    #   - 1024×768 (XGA)
    #   - 1920×1080 (Full HD)
    py5.size(800, 600)
    
    # Fondo negro
    py5.background(0)

    # ════════════════════════════════════════════════════════════════════════
    # ACCEDER A PROPIEDADES DE LA VENTANA
    # ════════════════════════════════════════════════════════════════════════
    
    # py5.width: el ANCHO en píxeles (se configura automáticamente)
    # py5.height: el ALTO en píxeles (se configura automáticamente)
    # Estas son variables "mágicas" de py5
    
    print(f"Ancho: {py5.width} píxeles")
    print(f"Alto: {py5.height} píxeles")
    print(f"Total de píxeles: {py5.width * py5.height}")
    
    # Esto imprimirá:
    # Ancho: 800 píxeles
    # Alto: 600 píxeles
    # Total de píxeles: 480000


if __name__ == "__main__":
    py5.run_sketch()


# ════════════════════════════════════════════════════════════════════════════
# CONCEPTOS IMPORTANTES
# ════════════════════════════════════════════════════════════════════════════

"""
VARIABLES ESPECIALES DE PY5:

py5.width   → Ancho de la ventana (set por py5.size())
py5.height  → Alto de la ventana (set por py5.size())
py5.mouse_x → Posición X actual del mouse
py5.mouse_y → Posición Y actual del mouse
py5.frame_count → Número de frames ejecutados
py5.frame_rate → Frames por segundo


RESOLUCIONES COMUNES:

Quadrado:
  • 400×400
  • 500×500

Apaisado (Landscape) - más ancho que alto:
  • 800×600 (4:3)
  • 1024×768 (4:3)
  • 1920×1080 (16:9) - Full HD

Portrait - más alto que ancho:
  • 400×600
  • 1080×1920


USOS DE width Y height:

1. Centrar elementos:
   py5.ellipse(py5.width / 2, py5.height / 2, 100, 100)
   → Dibuja círculo en el centro

2. Llenar toda la pantalla:
   py5.rect(0, 0, py5.width, py5.height)
   → Dibuja rectángulo de todo el tamaño

3. Cálculos relativos:
   x = py5.width * 0.25  → 25% del ancho
   y = py5.height * 0.75 → 75% del alto


EXPERIMENTA:
- Cambia py5.size(1000, 800)
- Cambia py5.size(500, 500)
- Imprime otros valores de py5


SIGUIENTE PASO: Ver 003_RGB.py
Aprenderás los modelos de COLOR (RGB vs HSV)
"""
