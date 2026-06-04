"""
PASO 8: Interacción con mouse - Proyectos interactivos
Usar py5.mouse_x, py5.mouse_y y mouse_pressed()
"""

import py5


def setup():
    """Configuración inicial."""
    py5.size(400, 400)
    
    # Dibujar rectángulos desde su CENTRO (no desde esquina)
    py5.rect_mode(py5.CENTER)
    
    # Sin contorno
    py5.no_stroke()
    
    # Color inicial
    py5.fill(100, 150, 200)


def draw():
    """
    Dibujar cuadrado pequeño siguiendo la posición del mouse.
    """
    # py5.mouse_x: coordenada X actual del mouse
    # py5.mouse_y: coordenada Y actual del mouse
    # Se actualizan automáticamente cada frame (~60 veces/segundo)
    py5.square(py5.mouse_x, py5.mouse_y, 10)


def mouse_pressed():
    """
    Se ejecuta cuando el usuario PRESIONA el botón del mouse.
    UNA sola vez por click (no continuamente).
    """
    # Cambiar a color aleatorio
    py5.fill(py5.random_int(255), py5.random_int(255), py5.random_int(255))
    print(f"✓ Click detectado en ({py5.mouse_x}, {py5.mouse_y})")


if __name__ == "__main__":
    py5.run_sketch()

