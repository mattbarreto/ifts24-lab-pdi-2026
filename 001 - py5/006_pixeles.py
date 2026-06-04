"""
PASO 6: Manipulación de píxeles - CORE de PDI
Acceder directamente al array de píxeles para crear patrones
"""

import py5


def setup():
    """Crear patrón procedimental de píxeles."""
    py5.size(400, 400)
    py5.load_pixels()  # Cargar array de píxeles en memoria

    # Iterar sobre TODOS los píxeles
    for x in range(py5.width):
        for y in range(py5.height):
            # Convertir 2D (x,y) a índice 1D: index = x + y * width
            index = x + y * py5.width

            # Calcular color basado en posición
            r = (x * 255) // py5.width      # Rojo: izquierda a derecha
            g = (y * 255) // py5.height    # Verde: arriba a abajo
            b = 128                         # Azul: constante

            # Establecer el color del píxel en la posición calculada
            py5.pixels[index] = py5.color(r, g, b)

    py5.update_pixels()  # Guardar cambios a la pantalla


if __name__ == "__main__":
    py5.run_sketch()

