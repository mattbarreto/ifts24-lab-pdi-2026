"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║        PASO 4: Modelo HSV (HSB) - Colores intuitivos                          ║
╚═══════════════════════════════════════════════════════════════════════════════╝

¿QUÉ APRENDERÁS?
════════════════════════════════════════════════════════════════════════════════
- MODELO HSV/HSB: Hue, Saturation, Value (Brightness)
- Diferencia entre RGB (técnico) vs HSV (intuitivo)
- Cómo generar TODOS los colores del espectro
- LOOPS: for i in range() para repetir código
- Crear GRADIENTES de color

PRÁCTICA ANTERIOR
════════════════════════════════════════════════════════════════════════════════
En 003_RGB.py aprendiste:
- RGB: Rojo, Verde, Azul (aditivo)
- 3 canales × 256 valores = 16.7 millones de colores
- RGB es técnico, basado en LUZ

NOVEDAD: MODELO HSV
════════════════════════════════════════════════════════════════════════════════
- HSV describe COLOR como lo percibe EL OJO
- H (Hue/Matiz) = El "color" en sí (0-360°, como rueda de colores)
- S (Saturation) = Qué tan vívido (0-100%)
- V (Value/Brillo) = Qué tan claro (0-100%)
- MÁS INTUITIVO que RGB
"""

import py5


# ════════════════════════════════════════════════════════════════════════════
# CONFIGURACIÓN INICIAL
# ════════════════════════════════════════════════════════════════════════════

def setup():
    """
    Crear ventana y configurar modo HSB (HSV).
    """
    py5.size(400, 400)
    
    # Cambiar a modo HSB (Hue, Saturation, Brightness)
    # HSB es lo mismo que HSV, solo nombres diferentes
    # Parámetros: (modo, rango_H, rango_S, rango_B)
    # 360 grados para Hue (rueda de colores)
    # 100 para Saturation (0-100%)
    # 100 para Brightness (0-100%)
    py5.color_mode(py5.HSB, 360, 100, 100)
    
    # Sin contorno
    py5.no_stroke()


# ════════════════════════════════════════════════════════════════════════════
# LOOP DE DIBUJO
# ════════════════════════════════════════════════════════════════════════════

def draw():
    """
    Dibujar TODOS los colores del espectro en líneas verticales.
    """
    
    # LOOP: Repetir 360 veces (para cada grado del espectro)
    # i va de 0 a 359
    for i in range(360):
        
        # Establecer color:
        # H = i (0-359): cada valor es un color diferente en la rueda
        # S = 100: saturación máxima (color muy vívido)
        # B = 100: brillo máximo (no oscurecido)
        py5.fill(i, 100, 100)
        
        # Dibujar línea vertical
        # x = i (cada línea en posición horizontal)
        # y = 0 (comienza arriba)
        # width = 1 (grosor de 1 píxel)
        # height = py5.height (llena toda la altura)
        py5.rect(i, 0, 1, py5.height)
        
        # RESULTADO: Gradiente de todos los colores
        # De izquierda a derecha: rojo→amarillo→verde→cian→azul→magenta→rojo


if __name__ == "__main__":
    py5.run_sketch()


# ════════════════════════════════════════════════════════════════════════════
# CONCEPTOS: MODELO HSV/HSB
# ════════════════════════════════════════════════════════════════════════════

"""
MODELO HSB (HSV) - PERCEPTUAL (cómo el ojo ve):

┌─────────────────────────────────────────────────────────────────────────┐
│ H - HUE (Matiz): 0-360°                                                 │
│ ├─ El "color" en la rueda cromática                                    │
│ ├─ 0° = Rojo                                                            │
│ ├─ 60° = Amarillo                                                       │
│ ├─ 120° = Verde                                                         │
│ ├─ 180° = Cian                                                          │
│ ├─ 240° = Azul                                                          │
│ └─ 300° = Magenta                                                       │
│                                                                         │
│ S - SATURATION (Saturación): 0-100%                                    │
│ ├─ 0% = Gris (sin color)                                               │
│ ├─ 50% = Color pastel (no tan vívido)                                  │
│ └─ 100% = Color puro y vívido                                          │
│                                                                         │
│ B/V - BRIGHTNESS/VALUE (Brillo): 0-100%                               │
│ ├─ 0% = Negro (completamente oscuro)                                   │
│ ├─ 50% = Color oscuro                                                  │
│ └─ 100% = Color claro y brillante                                      │
└─────────────────────────────────────────────────────────────────────────┘

RUEDA DE COLORES HSB:

          0°
         ROJO
     300°/  \60°
    MAGENTA AMARILLO
   240°      120°
     AZUL  VERDE
        180°
       CIAN


EJEMPLOS:

  Rojo vívido:       py5.fill(0, 100, 100)
  Rojo pastel:       py5.fill(0, 50, 100)
  Rojo oscuro:       py5.fill(0, 100, 50)
  Gris:              py5.fill(0, 0, 50)
  Blanco:            py5.fill(0, 0, 100)
  Negro:             py5.fill(0, 0, 0)
  Verde vibrante:    py5.fill(120, 100, 100)
  Verde agua:        py5.fill(180, 80, 90)


POR QUÉ HSB ES MÁS INTUITIVO:

Con RGB, para hacer un rojo más claro debes cambiar 3 valores:
  Rojo oscuro: (200, 0, 0)      → aumentar a rojo claro: (255, 80, 80)
  ¿Cuánto cambiar? ¡Complicado!

Con HSB, solo cambias B:
  Rojo oscuro: (0, 100, 50)     → rojo claro: (0, 100, 80)
  ¡Solo un parámetro!


CÓDIGO NUEVO: for i in range(360)

Esta es una LOOP (bucle):
  • range(360) crea números: 0, 1, 2, 3, ..., 359
  • i toma cada valor uno a uno
  • El código dentro de la loop se ejecuta 360 veces
  • Cada vez con un valor diferente de i


EXPERIMENTA:
- Cambia "360" a "180" para ver solo media rueda
- Cambia "100, 100" a "50, 100" para colores pastel
- Cambia "100, 100" a "100, 50" para colores oscuros
- Reduce a "10" para ver líneas más gruesas


SIGUIENTE PASO: Ver 005_upload_img.py
Aprenderás a CARGAR y MOSTRAR imágenes
"""
