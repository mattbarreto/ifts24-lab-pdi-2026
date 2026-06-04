"""
PASO 6B: Manipulación de píxeles de imagen - PRÁCTICO

Carga imagen REAL y aplica algoritmo: INVERTIR COLORES
Este es el primer ejemplo aplicado a fotos reales
"""

import py5


img = None


def setup():
    """
    Cargar y procesar imagen en setup.
    """
    global img
    
    py5.size(400, 400)
    py5.background(255)

    # Intentar cargar imagen
    try:
        img = py5.load_image("img/imagen.jpg")
        print("✓ Imagen cargada")
    except Exception as e:
        print(f"⚠️  Error: {e}")
        print("   Coloca una imagen en: img/imagen.jpg")
        return

    # Procesar imagen después de configurar contexto py5
    if img is not None:
        procesar_imagen()


def procesar_imagen():
    """
    ALGORITMO: Invertir colores de la imagen.
    Para cada píxel: new_color = (255-r, 255-g, 255-b)
    """
    global img

    print("Procesando imagen...")

    # Cargar array de píxeles de la imagen
    img.load_pixels()

    # Iterar sobre CADA píxel
    for i in range(len(img.pixels)):
        # Obtener color actual del píxel
        c = img.pixels[i]

        # Extraer componentes RGB usando funciones py5
        r = py5.red(c)     # Canal rojo
        g = py5.green(c)   # Canal verde
        b = py5.blue(c)    # Canal azul

        # Invertir: 255 - valor
        # Esto crea el efecto de negativo fotográfico
        img.pixels[i] = py5.color(255 - r, 255 - g, 255 - b)

    # Guardar cambios a la imagen
    img.update_pixels()
    print("✓ Imagen procesada (invertida)")


def draw():
    """Mostrar imagen procesada."""
    py5.background(255)

    if img is not None:
        # Mostrar imagen escalada a ventana
        py5.image(img, 0, 0, py5.width, py5.height)
    else:
        # Mostrar error si no cargó
        py5.fill(255, 0, 0)
        py5.text("Error: Imagen no encontrada", 50, 200)


def key_pressed():
    """
    Presionar 's' para guardar imagen procesada.
    """
    if py5.key == "s" and img is not None:
        img.save("imagen_invertida.jpg")
        print("💾 Imagen guardada: imagen_invertida.jpg")
    elif py5.key == "s":
        print("⚠️  Primero carga una imagen")


if __name__ == "__main__":
    py5.run_sketch()


# CONCEPTOS: MANIPULACIÓN DE IMAGEN REAL
"""
DIFERENCIA 006 vs 007:

006_pixeles.py:
  • Crea imagen PROCEDIMENTAL (desde código)
  • Pixeles de 0-399, 0-399
  • Patrón simple

007_pixeles.py:
  • Carga imagen REAL (archivo)
  • Manipula según contenido real
  • Algoritmo: invertir colores


EXTRAER CANALES:

py5.red(c)    →  componente R (0-255)
py5.green(c)  →  componente G (0-255)
py5.blue(c)   →  componente B (0-255)
py5.alpha(c)  →  transparencia (0-255)

Ejemplo:
  c = py5.color(200, 100, 50)
  r = py5.red(c)    # 200
  g = py5.green(c)  # 100
  b = py5.blue(c)   # 50


ALGORITMO: NEGATIVO

Foto normal:     pixel = (R, G, B)
Negativo:        pixel = (255-R, 255-G, 255-B)

Ejemplo:
  Blanco (255, 255, 255) → (0, 0, 0) Negro
  Negro (0, 0, 0) → (255, 255, 255) Blanco
  Rojo (255, 0, 0) → (0, 255, 255) Cian


GUARDAR IMAGEN:

img.save("nombre.jpg")
  • Guarda en carpeta del proyecto
  • Formatos: JPG, PNG, TIFF
  • Presiona 's' en el script


PRUEBAS:
1. Cambia "imagen_invertida.jpg" a otro nombre
2. Intenta otros efectos:
   - Escala de grises: gray = (r+g+b)/3
   - Solo rojo: (r, 0, 0)
   - Brillo: (r*1.5, g*1.5, b*1.5)
3. Abre la imagen resultante
"""
