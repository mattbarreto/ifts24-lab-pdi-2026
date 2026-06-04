"""
PASO 7: Filtros - Aplicar efectos a imágenes
Utilizar py5.tint() para filtrar canales RGB
"""

import py5


img = None


def setup():
    """Crear imagen procedimental con colores aleatorios."""
    global img
    py5.size(600, 200)
    
    # Crear imagen de prueba: 200x200 píxeles en modo RGB
    img = py5.create_image(200, 200, py5.RGB)

    # Llenar la imagen con colores aleatorios
    img.load_pixels()  # Cargar píxeles de la imagen
    
    for i in range(len(img.pixels)):
        # Asignar color aleatorio a cada píxel
        img.pixels[i] = py5.color(py5.random_int(255), 
                                   py5.random_int(255), 
                                   py5.random_int(255))
    
    img.update_pixels()  # Guardar cambios


def draw():
    """Mostrar imagen con diferentes filtros de color."""
    if img:
        # IMAGEN ORIGINAL (sin filtro)
        py5.image(img, 0, 0)

        # FILTRO: SOLO CANAL ROJO
        # py5.tint(255, 0, 0) aisla el canal rojo
        py5.tint(255, 0, 0)
        py5.image(img, 200, 0)

        # FILTRO: SOLO CANAL VERDE
        # py5.tint(0, 255, 0) aisla el canal verde
        py5.tint(0, 255, 0)
        py5.image(img, 400, 0)

        # Desactivar filtro
        py5.no_tint()


if __name__ == "__main__":
    py5.run_sketch()

