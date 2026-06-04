"""
PASO 13: Filtro BLUR - Desenfoque gaussiano
Suavizar imagen usando promedio de vecinos
"""

import py5


def setup():
    """Configuración."""
    py5.size(400, 400)
    print("✓ Cargando imagen...")


def draw():
    """
    Mostrar imagen desenfocada.
    BLUR: promedia cada píxel con sus vecinos
    Parámetro: radio del desenfoque (en píxeles)
    """
    # Cargar imagen
    try:
        img = py5.load_image("img/imagen.jpg")
    except:
        print("⚠️  Error: Coloca imagen en img/imagen.jpg")
        return
    
    # Mostrar imagen escalada a 400x400
    py5.image(img, 0, 0, 400, 400)
    
    # Aplicar BLUR con radio 5
    # Radio: tamaño del área a promediar
    # Mayor radio = más desenfoque = más lento
    py5.apply_filter(py5.BLUR, 5)


if __name__ == "__main__":
    py5.run_sketch()


# CONCEPTOS: DESENFOQUE (BLUR)
"""
QUÉ ES BLUR:

Para cada píxel:
  1. Mirar todos los píxeles en un radio (ej: 5px)
  2. Calcular promedio de valores
  3. Establecer píxel a ese promedio

Resultado: imagen suave, detalles borrosos


RADIO VS EFECTO:

BLUR con radio 1:
  • Desenfoque ligero
  • Reduce ruido mínimamente
  • Rápido

BLUR con radio 5:
  • Desenfoque notable
  • Reduce ruido mucho
  • Más lento

BLUR con radio 20:
  • Desenfoque fuerte
  • Imagen casi irreconocible
  • Muy lento


MATEMÁTICA: CONVOLUCIÓN

BLUR es una CONVOLUCIÓN con kernel (matriz)

Ejemplo: kernel 3x3 para promedio
  1/9   1/9   1/9
  1/9   1/9   1/9
  1/9   1/9   1/9

Para cada píxel (x, y):
  valor_nuevo = suma( vecinos * kernel ) / suma(kernel)

Kernels más complejos:
  • Gaussiano: pesa más al centro
  • Box: promedio simple
  • Mediano: toma valor medio (no promedio)


USOS:

1. PREPROCESAMIENTO
   • Reducir ruido antes de análisis
   • Preparar para detección de bordes
   • Suavizar antes de thresholding

2. ARTÍSTICO
   • Efecto movimiento
   • Fondo borroso (portrait mode)
   • Motion blur

3. SEGURIDAD
   • Pixelar caras (blur fuerte)
   • Difuminar información sensible

4. COMPRESIÓN
   • Reducir detalles para archivo más pequeño


OPERACIONES RELACIONADAS:

1. BLUR (desenfoque gaussiano)
   Promedia con pesos gaussianos
   
2. BOX BLUR (promedio simple)
   Promedio de todos los vecinos
   
3. MEDIAN BLUR
   Toma mediana (mejor para ruido)
   
4. BILATERAL BLUR
   Preserva bordes mientras desenfoca


PERFORMANCE:

BLUR es COSTOSO:
  • Radio 5: ~25 píxeles por píxel
  • 400x400 imagen: ~4 millones de operaciones
  • En py5: lento en Python
  • En OpenCV: muy rápido (optimizado)

Para mejorar:
  • Reducir tamaño de imagen primero
  • Usar OpenCV en vez de py5
  • Aumentar frame_rate() para menos fps


EXPERIMENTA:
1. Cambia radio 5 a 1, 10, 20
   ¿Cómo cambia el efecto?

2. Combina con otros filtros:
   apply_filter(BLUR, 5)
   apply_filter(GRAY)
   apply_filter(INVERT)
   
   ¿Qué orden da mejor resultado?

3. Usa BLUR para preparar imagen
   Luego aplica THRESHOLD
   ¿Mejora la detección de objetos?
"""
