"""
PASO 9: AVANZADO - Dibujo generativo
Combina todos los conceptos: loops, condicionales, matemática
"""

import py5


def setup():
    """Configuración del canvas."""
    py5.size(800, 600)
    py5.background(255)  # Fondo blanco

    # Controlar velocidad de generación
    py5.frame_rate(30)


def draw():
    """Renderizar patrón generativo."""
    py5.background(255)  # Limpia el lienzo en cada frame

    # Genera valores pseudo-aleatorios suaves (ruido Perlin)
    x = py5.noise(py5.width * 0.01, py5.height * 0.01)
    y = py5.noise(py5.width * 0.01, py5.height * 0.01)
    
    # Parámetros para el cálculo
    iterations = 50
    z = complex(0, 0)
    
    # Calcular patrón fractal
    for i in range(iterations):
        # Fórmula del conjunto de Mandelbrot: z = z^2 + c
        z = z**2 + complex(x, y)
        
        # Si diverge, salir del loop
        if abs(z) > 2:
            break
        
        # Colorear basado en iteraciones
        color = int(i * 255 / iterations)
        py5.fill(color)
        py5.rect(py5.mouse_x - 50, py5.mouse_y - 50, 100, 100)


if __name__ == "__main__":
    py5.run_sketch()

