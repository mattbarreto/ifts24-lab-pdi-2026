"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║        PASO 1: Básico - Tu primer programa interactivo con py5               ║
╚═══════════════════════════════════════════════════════════════════════════════╝

¿QUÉ APENDERÁS?
════════════════════════════════════════════════════════════════════════════════
- Dibujar formas básicas (ellipse/círculo)
- Uso de setup() vs draw()
- Diferencia entre color de fondo y color de relleno
- Primeras variables de py5: width, height
- Conceptos: fill() y no_stroke()

PRÁCTICA ANTERIOR
════════════════════════════════════════════════════════════════════════════════
En 000_intro_py5.py aprendiste:
- py5.size(): definir tamaño de ventana
- py5.fill(): color de relleno
- py5.rect(): dibujar rectángulo
- IMPORTANTE: Solo dibujamos una vez en setup()

NOVEDAD EN ESTE SCRIPT
════════════════════════════════════════════════════════════════════════════════
- Ahora USAMOS draw() que se ejecuta en LOOP (60 veces/segundo)
- Esto permite crear animaciones interactivas
- py5.background() limpia la pantalla en cada frame
- py5.no_stroke() elimina bordes
- py5.ellipse() dibuja elipses/círculos
"""

import py5


# ════════════════════════════════════════════════════════════════════════════
# CONFIGURACIÓN INICIAL
# ════════════════════════════════════════════════════════════════════════════

def setup():
    """
    Se ejecuta UNA SOLA VEZ al iniciar.
    Aquí configuramos el tamaño y propiedades iniciales.
    """
    # Crear ventana de 400×400 píxeles
    py5.size(400, 400)
    
    # Establecer color de fondo a negro (0, 0, 0)
    # RGB: Red=0, Green=0, Blue=0 → Negro
    py5.background(0)
    
    # Mensaje de confirmación en la consola
    print("✓ py5 funcionando correctamente")


# ════════════════════════════════════════════════════════════════════════════
# LOOP DE DIBUJO
# ════════════════════════════════════════════════════════════════════════════

def draw():
    """
    Se ejecuta continuamente (~60 veces/segundo).
    Aquí dibujamos lo que queremos ver en cada frame.
    """
    # Establecer color de relleno: turquesa (rojo=90, verde=237, azul=221)
    py5.fill(90, 237, 221)
    
    # Eliminar el contorno (stroke) de las formas
    py5.no_stroke()
    
    # Dibujar una elipse/círculo
    # Parámetros: (x_centro, y_centro, ancho, alto)
    # Como ancho=alto, es un círculo perfecto
    py5.ellipse(200, 200, 100, 100)


# ════════════════════════════════════════════════════════════════════════════
# EJECUTAR
# ════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    py5.run_sketch()


# ════════════════════════════════════════════════════════════════════════════
# CONCEPTOS CLAVE
# ════════════════════════════════════════════════════════════════════════════

"""
DIFERENCIA ENTRE setup() Y draw():

┌─────────────────────────────────────────────────────────────────────────┐
│ setup()                          │ draw()                              │
├──────────────────────────────────┼─────────────────────────────────────┤
│ • Se ejecuta UNA SOLA VEZ       │ • Se ejecuta CONTINUAMENTE (~60x/s) │
│ • Al iniciar el programa        │ • En cada frame (fotograma)         │
│ • Para configuración inicial    │ • Para dibujar animaciones          │
│ • Cargar recursos, tamaño, etc. │ • Actualizar posiciones, colores    │
└──────────────────────────────────┴─────────────────────────────────────┘


EJEMPLO DE LOOP:

Frame 1: draw() ejecuta → dibuja círculo
Frame 2: draw() ejecuta → dibuja círculo
Frame 3: draw() ejecuta → dibuja círculo
...
(60 veces por segundo)


FUNCIONES NUEVAS AQUÍ:

1. py5.ellipse(x, y, ancho, alto)
   - Dibuja elipse/círculo en posición (x, y)
   - Si ancho == alto → Círculo
   - Si ancho ≠ alto → Elipse

2. py5.no_stroke()
   - Elimina el contorno (border) de formas
   - Las formas aparecen sin línea negra


EXPERIMENTA:
- Cambia el color: py5.fill(255, 0, 0) para rojo
- Mueve el círculo: py5.ellipse(100, 300, 100, 100)
- Crea un óvalo: py5.ellipse(200, 200, 150, 100)
- Agrega más formas: py5.rect(), py5.circle(), etc.


SIGUIENTE PASO: Ver 002_info.py
Aprenderás sobre las propiedades de la ventana (width, height)
"""
