"""
EXPERIMENTO 3: Controlar un canal distinto con ambos ejes del mouse

¿Qué hace?
Controla el canal verde con la posición X del mouse y el azul con la posición Y.
Más interactivo que los experimentos anteriores: mové el mouse para ver cómo
varían los colores en tiempo real. Podés observar cómo los canales se amplifican
o suprimen según tu posición.
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

    # EXPERIMENTO 3: Controlar un canal distinto
    # Calcular factores según la posición del mouse
    factor_verde = py5.remap(py5.mouse_x, 0, py5.width, 0, 2.5)
    factor_azul = py5.remap(py5.mouse_y, 0, py5.height, 0, 2.5)

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

            # Modificar canales según mouse
            g = g * factor_verde
            b = b * factor_azul

            # Limitar los valores para que no superen 255
            if g > 255:
                g = 255
            if b > 255:
                b = 255

            # Calcular el índice del mismo píxel en el lienzo (desplazado 400px a la derecha)
            indice_canvas = (x + 400) + y * py5.width
            py5.pixels[indice_canvas] = py5.color(r, g, b)

    # Aplicar los cambios al lienzo
    py5.update_pixels()

py5.run_sketch()
