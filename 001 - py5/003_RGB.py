"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║        PASO 3: Modelo RGB - Entender cómo se crean los colores                ║
╚═══════════════════════════════════════════════════════════════════════════════╝

¿QUÉ APRENDERÁS?
════════════════════════════════════════════════════════════════════════════════
- MODELO RGB: Red, Green, Blue (Rojo, Verde, Azul)
- Cómo se CREAN los colores sumando luz
- Los 3 CANALES de color
- py5.color_mode(): cambiar sistema de color
- FUNDAMENTAL para Procesamiento Digital de Imágenes

PRÁCTICA ANTERIOR
════════════════════════════════════════════════════════════════════════════════
En 002_info.py aprendiste:
- py5.width y py5.height
- Resoluciones de pantalla
- Cálculos con propiedades

NOVEDAD: LOS COLORES
════════════════════════════════════════════════════════════════════════════════
- Cada píxel en la pantalla tiene 3 componentes: R, G, B
- Cada componente es un número del 0 al 255
- 0 = sin luz | 255 = máxima luz
- Combinando estos 3 canales se forman ~16.7 millones de colores
"""

import py5


# ════════════════════════════════════════════════════════════════════════════
# CONFIGURACIÓN INICIAL
# ════════════════════════════════════════════════════════════════════════════

def setup():
    """
    Crear ventana y configurar el modo de color RGB.
    """
    # Ventana ancha para mostrar los 3 canales lado a lado
    py5.size(600, 200)
    
    # IMPORTANTE: Configurar modo de color a RGB
    # Parámetro: (modo, valor_máximo_por_componente)
    # RGB, 255 significa: (Red, Green, Blue) cada uno 0-255
    py5.color_mode(py5.RGB, 255)
    
    # Sin contorno para ver mejor los colores
    py5.no_stroke()


# ════════════════════════════════════════════════════════════════════════════
# LOOP DE DIBUJO
# ════════════════════════════════════════════════════════════════════════════

def draw():
    """
    Dibujar los 3 canales RGB por separado.
    """
    
    # ────────────────────────────────────────────────────────────────────────
    # CANAL ROJO
    # ────────────────────────────────────────────────────────────────────────
    # py5.fill(R, G, B)
    # Rojo puro: máxima luz roja, sin verde, sin azul
    py5.fill(200, 0, 0)
    py5.rect(0, 0, 200, 200)
    
    # ────────────────────────────────────────────────────────────────────────
    # CANAL VERDE
    # ────────────────────────────────────────────────────────────────────────
    # Verde puro: sin rojo, máxima luz verde, sin azul
    py5.fill(0, 200, 0)
    py5.rect(200, 0, 200, 200)
    
    # ────────────────────────────────────────────────────────────────────────
    # CANAL AZUL
    # ────────────────────────────────────────────────────────────────────────
    # Azul puro: sin rojo, sin verde, máxima luz azul
    py5.fill(0, 0, 200)
    py5.rect(400, 0, 200, 200)


if __name__ == "__main__":
    py5.run_sketch()


# ════════════════════════════════════════════════════════════════════════════
# CONCEPTOS: MODELO RGB
# ════════════════════════════════════════════════════════════════════════════

"""
MODELO RGB - ADITIVO (suma luz):

En una pantalla, cada píxel contiene 3 luces:
  • Luz ROJA (R)
  • Luz VERDE (G)
  • Luz AZUL (B)

Cada luz puede tener intensidad 0-255:
  • 0 = apagada (no hay luz)
  • 255 = máxima intensidad

Combinando 3 canales × 256 valores = 16,777,216 colores posibles


EJEMPLOS DE COLORES RGB:

  NEGRO:      (0, 0, 0)           - Sin luz en ningún canal
  BLANCO:     (255, 255, 255)     - Máxima luz en todos
  ROJO:       (255, 0, 0)         - Solo rojo
  VERDE:      (0, 255, 0)         - Solo verde
  AZUL:       (0, 0, 255)         - Solo azul
  AMARILLO:   (255, 255, 0)       - Rojo + Verde
  CIAN:       (0, 255, 255)       - Verde + Azul
  MAGENTA:    (255, 0, 255)       - Rojo + Azul
  GRIS:       (128, 128, 128)     - Igual en todos


POR QUÉ RGB?

Las pantallas modernas (TV, monitor, celular) usan RGB porque:
  • Nuestros ojos tienen 3 tipos de células sensibles:
    - Conos sensibles al ROJO
    - Conos sensibles al VERDE
    - Conos sensibles al AZUL
  • Combinando estos 3 podemos ver prácticamente cualquier color


CONTRASTE CON HSV:

RGB describe COLOR como: componentes de LUZ (técnico)
HSV describe COLOR como: lo que EL OJO percibe (intuitivo)
  • H (Hue) = Matiz: qué color "es" (rojo, verde, azul, etc.)
  • S (Saturation) = Saturación: qué tan vívido es el color
  • V (Value) = Brillo: qué tan claro/oscuro es

Vamos a ver HSV en el siguiente paso (004_HSV.py)


EXPERIMENTA:
- Cambia los valores: py5.fill(100, 150, 200)
- Intenta crear colores: cian (0, 255, 255), magenta (255, 0, 255)
- Crea gradientes: variar valores progresivamente


SIGUIENTE PASO: Ver 004_HSV.py
Aprenderás el modelo HSV (más intuitivo)
"""
