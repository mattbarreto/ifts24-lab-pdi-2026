"""
PASO 10: Filtro THRESHOLD - Umbralización binaria
Convertir imagen a blanco y negro según umbral
"""

import py5


def setup():
    """Configuración."""
    py5.size(400, 400)
    print("✓ Cargando imagen...")


def draw():
    """
    Mostrar imagen con filtro THRESHOLD.
    THRESHOLD = umbralización: píxeles > umbral → blanco, < umbral → negro
    """
    # Cargar imagen
    try:
        img = py5.load_image("img/imagen.jpg")
    except:
        print("⚠️  Error: Coloca imagen en img/imagen.jpg")
        return
    
    # Mostrar imagen escalada a 400x400
    py5.image(img, 0, 0, 400, 400)
    
    # Aplicar THRESHOLD
    # Parámetro: umbral entre 0-1 (0.5 = 50% del brillo)
    # Píxeles brillosos (>0.5) → blanco (255, 255, 255)
    # Píxeles oscuros (<0.5) → negro (0, 0, 0)
    py5.apply_filter(py5.THRESHOLD, 0.5)


if __name__ == "__main__":
    py5.run_sketch()


# CONCEPTOS: FILTROS BÁSICOS
"""
py5.apply_filter(tipo, parámetro):

Aplica filtro a TODO lo que se dibujó en draw()

FILTROS DISPONIBLES:

1. THRESHOLD
   py5.apply_filter(py5.THRESHOLD, valor)
   valor: 0-1 (threshold de brillo)
   Resultado: imagen binaria (solo blanco y negro)
   Uso: OCR, detección de objetos, segmentación

2. GRAY
   py5.apply_filter(py5.GRAY)
   Resultado: escala de grises
   Fórmula: gray = 0.299*R + 0.587*G + 0.114*B

3. BLUR
   py5.apply_filter(py5.BLUR, radio)
   Resultado: imagen desenfocada
   radio: tamaño del desenfoque (1-100)

4. INVERT
   py5.apply_filter(py5.INVERT)
   Resultado: negativo (255-valor)
   Similar a lo que hicimos en 007_pixeles.py

5. DILATE
   py5.apply_filter(py5.DILATE)
   Resultado: expande áreas blancas
   Morfología matemática: crece 1 píxel


THRESHOLD EXPLICADO:

Umbral = 0.5 (50% del brillo máximo)

  Pixel original: (100, 150, 80)   → brillo ≈ 0.5
  Comparar con umbral 0.5
  brillo ≥ 0.5 → blanco (255, 255, 255)

  Pixel original: (200, 200, 200)  → brillo ≈ 0.78
  brillo ≥ 0.5 → blanco (255, 255, 255)

  Pixel original: (50, 40, 30)     → brillo ≈ 0.14
  brillo < 0.5 → negro (0, 0, 0)


USOS PRÁCTICOS:

• THRESHOLD: Separar objeto de fondo
  - Documentos escaneados
  - QR codes
  - Detección de objetos

• GRAY: Reducir info (1 canal vs 3)
  - Preprocesamiento
  - Análisis de borde
  - Histogramas

• BLUR: Suavizar ruido
  - Preprocesamiento para detección
  - Efecto artístico

• INVERT: Negativo
  - Efecto artístico
  - Análisis de contraste

• DILATE: Expandir objetos
  - Llenar huecos
  - Morfología


LIMITACIONES:

py5.apply_filter() es LENTO para:
  • Imágenes grandes (>1000x1000)
  • Múltiples filtros en secuencia
  • Tiempo real (30+ fps)

Para velocidad: usar OpenCV (en notebooks)


PRUEBAS:
• Cambia 0.5 a 0.3, 0.7, 0.9
¿Qué cambia? (más/menos píxeles blancos)

• Combina con otros scripts
"""
