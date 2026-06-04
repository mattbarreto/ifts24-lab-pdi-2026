"""
PASO 1B: Lo básico en HSV - Alternativa didáctica

Ahora mismo dibujas lo mismo que en 001_basico.py
Pero usando HSV en lugar de RGB para cambiar modos de color
"""

import py5


def setup():
    """
    Configuración inicial.
    NOVEDAD: py5.color_mode(HSB, rango_H, rango_S, rango_B)
    """
    py5.size(400, 400)
    
    # Cambiar modo de color a HSB (HSV)
    # Parámetros: (modo, max_hue, max_sat, max_bright)
    # En este caso: H de 0-360, S de 0-100, B de 0-100
    py5.color_mode(py5.HSB, 360, 100, 100)
    
    # Fondo: H=200 (cian), S=50%, B=80% (claro)
    py5.background(200)
    
    print("✓ py5 funcionando correctamente")


def draw():
    """
    Dibujar rectángulo usando HSV.
    """
    # H=235 (azul verdoso), S=40% (desaturado), B=30% (oscuro)
    py5.fill(235, 40, 30)
    py5.rect(150, 150, 100, 100)


if __name__ == "__main__":
    py5.run_sketch()


# CONCEPTO: color_mode()
"""
py5.color_mode(HSB, max_h, max_s, max_b):

Cambia cómo especificas colores en fill(), stroke(), etc.

RGB (por defecto):
  py5.color_mode(py5.RGB, 255, 255, 255)
  fill(255, 0, 0)  →  rojo

HSB (HSV):
  py5.color_mode(py5.HSB, 360, 100, 100)
  fill(0, 100, 100)  →  rojo (H=0°, saturación máxima, brillo máximo)

Ventajas de HSB en este script:
  • Más intuitivo para elegir colores
  • H=0-360: gira por la rueda de colores
  • S=0-100: qué tan puro es el color
  • B=0-100: qué tan claro u oscuro

Esta es la MISMA IMAGEN que 001_basico.py
Pero demostramos que hay múltiples maneras de especificar colores

PRUEBA:
  • Cambia fill(235, 40, 30) a:
    - fill(0, 100, 100)    →  rojo puro
    - fill(120, 100, 100)  →  verde puro
    - fill(240, 100, 100)  →  azul puro
    - fill(0, 0, 100)      →  blanco
    - fill(0, 0, 50)       →  gris
"""
