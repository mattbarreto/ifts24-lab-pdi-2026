"""
╔════════════════════════════════════════════════════════════════════════════╗
║ PIZARRA PASO 1: Introducción a py5 - Dibujo básico con el mouse            ║
╚════════════════════════════════════════════════════════════════════════════╝

¿QUÉ APRENDEREMOS?
──────────────────────────────────────────────────────────────────────────────
En este primer paso crearemos una pizarra interactiva simple. Aprenderemos:

1. Funciones básicas de py5:
   - setup(): se ejecuta una sola vez al iniciar
   - draw(): se repite constantemente (loop de dibujo)
   - mouse_dragged(): función especial que detecta cuando el mouse se mueve
                      mientras está presionado

2. Conceptos clave:
   - Coordenadas (x, y): posición del mouse en la ventana
   - Dibujo de primitivas: py5.point() dibuja píxeles
   - Propiedades de trazo: color, grosor (stroke_weight)

¿CÓMO FUNCIONA?
──────────────────────────────────────────────────────────────────────────────
- Inicialmente, creamos un canvas (lienzo) de 700×500 píxeles
- El fondo se rellena de color blanco (255 en escala RGB)
- py5 entra en un loop: llama a draw() continuamente (~60 veces por segundo)
- Cuando arrastras el mouse, se dispara mouse_dragged()
- Cada punto donde está el mouse se dibuja con color negro
"""

import py5

# ════════════════════════════════════════════════════════════════════════════
# PASO 1: CONFIGURACIÓN INICIAL (setup)
# ════════════════════════════════════════════════════════════════════════════

def setup():
    """
    Se ejecuta UNA SOLA VEZ cuando inicia el programa.
    Aquí configuramos el tamaño de la ventana y propiedades iniciales.
    """
    py5.size(700, 500)              # Crea una ventana de 700×500 píxeles
    py5.background(255)             # Rellena el fondo con color blanco (255, 255, 255)
    py5.stroke_weight(12)           # Define el grosor del trazo: 12 píxeles


# ════════════════════════════════════════════════════════════════════════════
# PASO 2: LOOP DE DIBUJO (draw)
# ════════════════════════════════════════════════════════════════════════════

def draw():
    """
    Se ejecuta continuamente (~60 veces por segundo).
    Aquí dibujamos la interfaz: área de instrucciones.
    """
    # Área de instrucciones en la parte superior
    py5.fill(200)                   # Color gris para el fondo del panel
    py5.no_stroke()                 # Sin contorno
    py5.rect(0, 0, py5.width, 40)  # Rectángulo que ocupa todo el ancho
    
    # Texto con instrucciones
    py5.fill(0)                     # Color negro para el texto
    py5.text_size(14)               # Tamaño de fuente: 14 píxeles
    py5.text("PASO 1: Arrastra el mouse para dibujar puntos", 10, 20)


# ════════════════════════════════════════════════════════════════════════════
# PASO 3: INTERACCIÓN CON EL MOUSE (mouse_dragged)
# ════════════════════════════════════════════════════════════════════════════

def mouse_dragged():
    """
    Esta función se dispara automáticamente cuando:
    - El botón del mouse está presionado
    - El mouse se está moviendo
    
    Variables disponibles:
    - py5.mouse_x: posición X actual del mouse
    - py5.mouse_y: posición Y actual del mouse
    """
    py5.stroke(0)                   # Color negro para el trazo: RGB(0, 0, 0)
    py5.stroke_weight(12)           # Grosor del punto: 12 píxeles
    py5.point(py5.mouse_x, py5.mouse_y)  # Dibuja un punto en la posición del mouse


if __name__ == '__main__':
    py5.run_sketch()
