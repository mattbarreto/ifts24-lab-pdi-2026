"""
EXPERIMENTO 1: Suprimir el canal rojo por completo

¿Qué hace?
Supprime completamente el canal rojo (r = 0). La imagen de la derecha muestra
solo los canales verde y azul. Observá qué pasa con las zonas que eran
originalmente rojas: deberían aparecer en tonos cian (azul + verde).
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
    py5.background(35)

    # Imagen original en la mitad izquierda (sin modificar)
    py5.image(img, 0, 0)

    # Acceder a la matriz de píxeles del lienzo completo
    img.load_pixels()
    py5.load_pixels()

    for x in range(img.width):
        for y in range(img.height):

            # La imagen es un arreglo lineal. Para acceder al píxel (x, y):
            # índice = x + y * ancho
            indice_img = x + y * img.width
            pixel = img.pixels[indice_img]

            # Separar los canales
            r = py5.red(pixel)
            g = py5.green(pixel)
            b = py5.blue(pixel)

            # EXPERIMENTO 1: Suprimir el canal rojo por completo
            r = 0

            # Calcular el índice del mismo píxel en el lienzo (desplazado 400px a la derecha)
            indice_canvas = (x + 400) + y * py5.width
            py5.pixels[indice_canvas] = py5.color(r, g, b)

    # Aplicar los cambios al lienzo
    py5.update_pixels()

py5.run_sketch()
