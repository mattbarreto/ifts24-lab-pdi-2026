"""
EXPERIMENTO 1: Color negativo (complementario)

¿Qué hace?
Muestra el color complementario del píxel bajo el mouse. 
Reemplaza el color con su negativo: (255 - r, 255 - g, 255 - b).
Un rojo puro (255, 0, 0) se convierte en cian (0, 255, 255).
"""

import py5
import os

img = None

def setup():
    global img
    py5.size(800, 400)
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(script_dir, "img", "imagen.jpg")
    img = py5.load_image(img_path)
    img.resize(400, 400)

def draw():
    py5.background(255)

    # Mostrar la imagen en la mitad izquierda
    py5.image(img, 0, 0)

    # Limitar las coordenadas del mouse al área de la imagen
    # Esto evita errores si el cursor sale de la imagen
    mx = py5.constrain(py5.mouse_x, 0, 399)
    my = py5.constrain(py5.mouse_y, 0, 399)

    # Obtener el color del píxel en esa posición
    color_pixel = py5.get_pixels(int(mx), int(my))

    # Separar el color en sus tres canales
    r = py5.red(color_pixel)
    g = py5.green(color_pixel)
    b = py5.blue(color_pixel)

    # Mostrar el color NEGATIVO (complementario) en el cuadrado de la derecha
    py5.fill(255 - r, 255 - g, 255 - b)
    py5.stroke(0)
    py5.rect(450, 50, 300, 300)

    # Mostrar los valores numéricos
    py5.fill(0)
    py5.text_size(18)
    py5.text(f"Posición: ({mx}, {my})", 450, 30)
    py5.text(f"Original R: {r:.0f}   G: {g:.0f}   B: {b:.0f}", 450, 350)
    py5.text(f"Negativo R: {255-r:.0f}   G: {255-g:.0f}   B: {255-b:.0f}", 450, 380)

py5.run_sketch()
