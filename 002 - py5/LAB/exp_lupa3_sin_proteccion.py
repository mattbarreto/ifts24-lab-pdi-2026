"""
EXPERIMENTO 3: Sin protección (error de límites)

¿Qué hace?
SIN usar py5.constrain(), accede directamente a mouse_x y mouse_y.
Esto permite que el cursor se salga del área de la imagen.

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

    # SIN PROTECCIÓN: acceso directo sin constrain
    # Mové el mouse rápidamente fuera de la imagen para ver el error
    mx = py5.mouse_x
    my = py5.mouse_y

    try:
        # Obtener el color del píxel en esa posición
        color_pixel = py5.get_pixels(int(mx), int(my))

        # Separar el color en sus tres canales
        r = py5.red(color_pixel)
        g = py5.green(color_pixel)
        b = py5.blue(color_pixel)

        # Mostrar el color como un cuadrado en la mitad derecha (la "lupa")
        py5.fill(color_pixel)
        py5.stroke(0)
        py5.rect(450, 50, 300, 300)

        # Mostrar los valores numéricos
        py5.fill(0)
        py5.text_size(18)
        py5.text(f"Posición: ({mx}, {my})", 450, 30)
        py5.text(f"R: {r:.0f}   G: {g:.0f}   B: {b:.0f}", 450, 380)
    except:
        # Si hay error, mostrar mensaje
        py5.fill(200)
        py5.rect(450, 50, 300, 300)
        py5.fill(255, 0, 0)
        py5.text_size(16)
        py5.text("ERROR: ¡Fuera de límites!", 450, 150)
        py5.text(f"Posición: ({mx}, {my})", 450, 300)
        py5.text("Mové el mouse sobre la imagen", 450, 330)

py5.run_sketch()
