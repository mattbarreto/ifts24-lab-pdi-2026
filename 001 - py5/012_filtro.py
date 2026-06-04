"""
PASO 12: Filtro INVERT - Negativo fotográfico
Invertir todos los valores RGB: 255-valor
"""

import py5


def setup():
    """Configuración."""
    py5.size(400, 400)
    print("✓ Cargando imagen...")


def draw():
    """
    Mostrar imagen invertida (negativo).
    INVERT: para cada píxel (r,g,b) → (255-r, 255-g, 255-b)
    """
    # Cargar imagen
    try:
        img = py5.load_image("img/imagen.jpg")
    except:
        print("⚠️  Error: Coloca imagen en img/imagen.jpg")
        return
    
    # Mostrar imagen escalada a 400x400
    py5.image(img, 0, 0, 400, 400)
    
    # Aplicar INVERT
    # Convierte colores al negativo (como en fotografía analógica)
    # Blanco (255,255,255) → Negro (0,0,0)
    # Negro (0,0,0) → Blanco (255,255,255)
    py5.apply_filter(py5.INVERT)


if __name__ == "__main__":
    py5.run_sketch()


# CONCEPTOS: INVERSIÓN DE COLORES
"""
FÓRMULA INVERT:

para cada píxel:
  r_new = 255 - r_old
  g_new = 255 - g_old
  b_new = 255 - b_old

Ejemplos:
  (255, 0, 0)   rojo puro        → (0, 255, 255)  cian
  (0, 255, 0)   verde puro       → (255, 0, 255)  magenta
  (0, 0, 255)   azul puro        → (255, 255, 0)  amarillo
  (255, 255, 255) blanco         → (0, 0, 0)      negro
  (128, 128, 128) gris neutro    → (127, 127, 127) gris neutro
  (200, 100, 50) naranja         → (55, 155, 205)  cian oscuro


HISTÓRICA: NEGATIVOS FOTOGRÁFICOS

En fotografía analógica:
  1. Se expone película a luz
  2. Se obtiene NEGATIVO (invertido)
  3. Se imprime sobre papel (invierte de nuevo)
  4. Resultado: imagen normal

En digital:
  • Usamos INVERT para simular negativo
  • Análisis de diferencias
  • Efecto artístico


VSUS GRAY (011 vs 012):

011_filtro.py (GRAY):
  Pierde color, mantiene luminosidad
  (255, 0, 0) rojo puro → ~76 gris oscuro
  (0, 255, 0) verde puro → ~182 gris claro

012_filtro.py (INVERT):
  Invierte color y luminosidad
  (255, 0, 0) rojo puro → (0, 255, 255) cian brillante
  (0, 255, 0) verde puro → (255, 0, 255) magenta brillante


USOS PRÁCTICOS:

1. ANÁLISIS
   • Resaltar detalles oscuros (brillo)  
   • Comparación visual

2. ARTÍSTICO
   • Efecto surrealista
   • Negativo intencional

3. DIAGNÓSTICO
   • Radiografías médicas
   • Inspección de defectos

4. COMPARACIÓN
   Abrir imagen + negativo lado a lado
   Ver qué detalles se pierden/ganan


MATEMÁTICA:

Inversión es una TRANSFORMACIÓN AFÍN:
  f(x) = 255 - x

Propiedades:
  • Aplicar dos veces = imagen original
    255 - (255 - x) = x
  • Es reversible
  • Preserva estructura (píxeles conectados siguen conectados)


EXPERIMENTA:
1. Compara 011 (GRAY) vs 012 (INVERT)
   ¿Qué ves diferente?

2. Guarda ambas imágenes
   Abre en editor (mantén lado a lado)

3. ¿Qué es más fácil de ver?
   ¿Original?
   ¿GRAY?
   ¿INVERT?
"""
