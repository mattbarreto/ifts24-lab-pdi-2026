"""
PASO 8C: Mouse con detección de presión
Dibujar círculo SOLO mientras el botón esté presionado
"""

import py5


def setup():
    """Configuración inicial."""
    py5.size(400, 300)
    py5.background(255)
    print("✓ py5 funcionando correctamente")


def draw():
    """
    Dibujar círculo solo mientras se presiona el mouse.
    NOVEDAD: py5.is_mouse_pressed (variable booleana)
    """
    py5.background(255)  # Limpiar en cada frame

    # DETECCIÓN DE PRESIÓN CONTINUA
    # py5.is_mouse_pressed: True mientras botón está abajo
    # Se actualiza cada frame
    if py5.is_mouse_pressed:
        py5.fill(255, 0, 0)
        py5.circle(py5.mouse_x, py5.mouse_y, 20)


if __name__ == "__main__":
    py5.run_sketch()


# CONCEPTOS: mouse_pressed() vs is_mouse_pressed
"""
DOS FORMAS DE DETECTAR MOUSE:

1. mouse_pressed() - EVENTO (se ejecuta UNA VEZ)

   def mouse_pressed():
       # Se ejecuta UNA sola vez cuando presionas
       print("Click!")
   
   Uso: acciones puntuales (disparar, cambiar color, guardar)
   Ej: pizarra_paso4_botones.py

2. is_mouse_pressed - ESTADO (CONTINUO en cada frame)

   if py5.is_mouse_pressed:
       # Este código se ejecuta MIENTRAS está presionado
       # Cada frame (60 veces/segundo)
       py5.circle(...)
   
   Uso: acciones continuas (dibujar, mover, arrastrar)
   Ej: Este script


DIFERENCIA VISUAL:

mouse_pressed():
  Click... muestra "Click!" una vez
  Release... nada

is_mouse_pressed:
  Press....... circle aparece
  Hold....... circle sigue moviéndose
  Release... circle desaparece


COMPARATIVA:

                    mouse_pressed()    is_mouse_pressed
Tiempo              Puntual (1x)       Continuo (60x/s)
En eventos          Sí                 No
En draw()           No                 Sí
Uso                 Acciones puntuales Acciones continuas

Ejemplos:
  • Presionar: mouse_pressed()
  • Arrastrar: is_mouse_pressed
  • Click botón: mouse_pressed()
  • Dibujar: is_mouse_pressed


EVENTOS DEL MOUSE:

1. mouse_pressed()    → Se presiona el botón
2. mouse_released()   → Se suelta el botón
3. mouse_moved()      → Se mueve el mouse
4. mouse_dragged()    → Se mueve MIENTRAS presionas

Variables:
1. py5.mouse_x        → Posición X
2. py5.mouse_y        → Posición Y
3. py5.is_mouse_pressed → Booleano: ¿está presionado?


EXPERIMENTA:
1. Reemplaza is_mouse_pressed con mouse_pressed():
   def mouse_pressed():
       py5.circle(...)
   
   ¿Qué cambia?

2. Dibuja mientras presionas (trazo continuo):
   if py5.is_mouse_pressed:
       py5.stroke_weight(5)
       py5.line(prev_x, prev_y, py5.mouse_x, py5.mouse_y)
"""
