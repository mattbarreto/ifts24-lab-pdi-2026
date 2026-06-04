"""
PASO 11: Filtro GRAY - Escala de grises
Convertir imagen de color a blanco y negro
"""

import py5


def setup():
    """Configuración."""
    py5.size(400, 400)
    print("✓ Cargando imagen...")


def draw():
    """
    Mostrar imagen convertida a escala de grises.
    GRAY = desatura color, mantiene luminosidad
    """
    # Cargar imagen
    try:
        img = py5.load_image("img/imagen.jpg")
    except:
        print("⚠️  Error: Coloca imagen en img/imagen.jpg")
        return
    
    # Mostrar imagen escalada a 400x400
    py5.image(img, 0, 0, 400, 400)
    
    # Aplicar GRAY
    # Convierte colores RGB a escala de grises
    # Usa fórmula de luminosidad percibida:
    # gray = 0.299*R + 0.587*G + 0.114*B
    # (El ojo es más sensible al verde que al rojo/azul)
    py5.apply_filter(py5.GRAY)


if __name__ == "__main__":
    py5.run_sketch()


# CONCEPTOS: ESCALA DE GRISES
"""
CONVERSIÓN A ESCALA DE GRISES:

Método 1: Promedio simple
  gray = (r + g + b) / 3
  Ej: (255, 0, 0) → (85, 85, 85)
  Problema: No coincide con percepción humana

Método 2: Pesos perceptivos (py5.GRAY)
  gray = 0.299*R + 0.587*G + 0.114*B
  El verde tiene más peso (0.587)
  El rojo tiene peso (0.299)
  El azul tiene menos peso (0.114)
  
  Ejemplo: (255, 0, 0)
  gray = 0.299*255 + 0.587*0 + 0.114*0 = 76
  
  Resultado: (76, 76, 76) - rojo se ve más oscuro


COMPARATIVA: RGB vs GRAY

RGB:
  • 3 canales: R, G, B
  • 16.7 millones de colores
  • Imagen más grande (3 bytes/píxel)
  • Más info

GRAY:
  • 1 canal: luminosidad
  • 256 niveles de gris
  • Imagen más pequeña (1 byte/píxel)
  • Menos info, pero suficiente para análisis


USOS:

1. PREPROCESAMIENTO
   Muchos algoritmos usan GRAY como entrada
   • Detección de bordes
   • Face recognition
   • OCR

2. ANÁLISIS
   • Histogramas
   • Estadísticas de brillo
   • Contraste

3. ARCHIVO
   • Imágenes más pequeñas
   • Fotos antiguas
   • Radiografías médicas

4. ARTÍSTICO
   • Efecto blanco y negro
   • Fotografía vintage


DIFERENCIA 011 vs 012:

011_filtro.py (GRAY):
  Mantiene estructura, pierde color
  Imagen oscura/clara según brillo
  Pixel: (255, 100, 50) → ~140 (medio gris)

012_filtro.py (INVERT):
  Invierte todos los valores
  Imagen se ve al revés
  Pixel: (255, 100, 50) → (0, 155, 205)


VARIACIONES:

1. Escala de grises invertida
   img.gray() luego filtro INVERT

2. Aumento de contraste
   Después de GRAY, aumentar diferencia entre claros/oscuros

3. Posterize
   Reducir cantidad de grises (8 niveles en vez de 256)


EXPERIMENTA:
• Abre la imagen original y esta versión
• ¿Qué información se mantiene?
• ¿Qué información se pierde?
"""
