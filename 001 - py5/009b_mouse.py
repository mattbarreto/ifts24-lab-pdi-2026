"""
PASO 8B: Mouse con detección de límites
Dibujar círculo solo cuando el mouse está DENTRO de la ventana
"""

import py5


def setup():
    """Configuración inicial."""
    py5.size(400, 300)
    py5.background(255)
    print("✓ py5 funcionando correctamente")


def draw():
    """
    Dibujar círculo que sigue al mouse.
    NOVEDAD: Verificar que mouse está dentro de la ventana
    """
    py5.background(255)  # Limpiar en cada frame

    # DETECCIÓN DE LÍMITES
    # Verificar que coordenadas están dentro del rectángulo [0, width] x [0, height]
    if 0 <= py5.mouse_x <= py5.width and 0 <= py5.mouse_y <= py5.height:
        # Solo dibujar si está dentro
        py5.fill(255, 0, 0)
        py5.circle(py5.mouse_x, py5.mouse_y, 20)  # Radio 20


if __name__ == "__main__":
    py5.run_sketch()


# CONCEPTOS: DETECCIÓN DE LÍMITES
"""
DETECCIÓN: ¿El mouse está dentro de la ventana?

Condición:
  if 0 <= py5.mouse_x <= py5.width and 0 <= py5.mouse_y <= py5.height:
      # Está dentro
  else:
      # Está fuera

Rango válido:
  X: 0 a width
  Y: 0 a height

Ejemplo 400x300:
  X válido: 0-399
  Y válido: 0-299


CUANDO ES ÚTIL:
  • Evitar bugs cuando el mouse sale de la ventana
  • Solo procesar cuando estés en ventana activa
  • Juegos: no disparar fuera de la zona
  • Interfaces: botones responden solo cuando están encima


OTRAS DETECCIONES DE ÁREA:

Rectángulo:
  x1 <= py5.mouse_x <= x2 and y1 <= py5.mouse_y <= y2

Círculo:
  dist = py5.dist(py5.mouse_x, py5.mouse_y, cx, cy)
  if dist < radius:
      # Dentro del círculo

Triángulo: (más complejo, requiere matemática)


USO: BOTONES CLICKEABLES

Viste esto en pizarra_paso4_botones.py:
  for button in buttons:
      if (button['x'] <= py5.mouse_x <= button['x'] + button['w'] and
          button['y'] <= py5.mouse_y <= button['y'] + button['h']):
          # Click en botón
"""
