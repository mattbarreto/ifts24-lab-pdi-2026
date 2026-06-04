"""
╔════════════════════════════════════════════════════════════════════════════╗
║ PIZARRA PASO 2: Interactividad por teclado - Cambiar colores               ║
╚════════════════════════════════════════════════════════════════════════════╝

¿QUÉ APRENDEREMOS?
──────────────────────────────────────────────────────────────────────────────
En este segundo paso extendemos la pizarra con interacción por teclado:

1. Variables de estado:
   - current_color: almacena el color actual (tupla RGB)
   - La palabra clave 'global' para modificar variables globales

2. Manejo de eventos de teclado:
   - key_pressed(): función que se dispara cuando presionas una tecla
   - py5.key: variable que contiene la tecla presionada

3. Modelo de color RGB:
   - (0, 0, 0) = Negro (sin luz)
   - (255, 0, 0) = Rojo puro
   - (255, 255, 255) = Blanco (máxima luz en todos los canales)

¿CÓMO FUNCIONA?
──────────────────────────────────────────────────────────────────────────────
- Almacenamos el color actual en una variable global
- Cuando presionas una tecla, se ejecuta key_pressed()
- El color se cambia según la tecla (1=negro, 2=rojo, C=limpiar)
- En mouse_dragged(), usamos el color almacenado en current_color
- El operador * "desempaqueta" la tupla: (255, 0, 0) → 255, 0, 0
"""

import py5

# ════════════════════════════════════════════════════════════════════════════
# VARIABLES GLOBALES
# ════════════════════════════════════════════════════════════════════════════
# Estas variables mantienen el "estado" de la aplicación entre ejecuciones

current_color = (0, 0, 0)  # Color inicial: Negro (RGB)


def setup():
    """
    Configuración inicial: tamaño de ventana y propiedades de trazo
    """
    py5.size(700, 500)
    py5.background(255)        # Fondo blanco
    py5.stroke_weight(12)      # Grosor de trazo


def draw():
    """
    Loop de dibujo: muestra instrucciones y estado actual
    """
    # Panel de instrucciones
    py5.fill(200)
    py5.no_stroke()
    py5.rect(0, 0, py5.width, 65)
    
    # Textos informativos
    py5.fill(0)
    py5.text_size(14)
    py5.text("PASO 2: Cambio de color con teclas", 10, 20)
    py5.text("Presiona: 1=NEGRO | 2=ROJO | C=LIMPIAR", 10, 40)
    
    # Mostrar color actual (para retroalimentación visual)
    color_text = f"Color actual: RGB{current_color}"
    py5.text(color_text, 10, 60)


def mouse_dragged():
    """
    Dibuja mientras arrastras el mouse.
    Usa el color almacenado en current_color.
    
    Nota: El operador * desempaqueta la tupla:
    py5.stroke(*(255, 0, 0))  equivale a  py5.stroke(255, 0, 0)
    """
    py5.stroke(*current_color)  # Desempaqueta la tupla de color
    py5.stroke_weight(12)
    py5.point(py5.mouse_x, py5.mouse_y)


def key_pressed():
    """
    Se ejecuta cuando presionas una tecla.
    Cambiar current_color según la tecla presionada.
    
    Nota: Necesitamos 'global current_color' para modificar la variable
    global desde dentro de esta función.
    """
    global current_color
    
    key = py5.key  # Obtén la tecla presionada
    
    if key == '1':
        current_color = (0, 0, 0)      # Negro
        print("✓ Color: NEGRO")
        
    elif key == '2':
        current_color = (255, 0, 0)    # Rojo puro
        print("✓ Color: ROJO")
        
    elif key.lower() == 'c':
        py5.background(255)             # Limpia el canvas
        print("✓ Pizarra limpiada")


if __name__ == '__main__':
    py5.run_sketch()
