"""
╔════════════════════════════════════════════════════════════════════════════╗
║ PIZARRA PASO 3: Modo borrador - Estados y toggles                          ║
╚════════════════════════════════════════════════════════════════════════════╝

¿QUÉ APRENDEREMOS?
──────────────────────────────────────────────────────────────────────────────
En este paso introducimos el concepto de "estado booleano" (true/false):

1. Variables booleanas para control:
   - eraser_mode: verdadero/falso indica si estamos en modo borrador
   - Toggle: cambiar entre dos estados con la misma tecla

2. Lógica condicional más compleja:
   - Guardar el color anterior (previous_color)
   - Usar operador ternario: valor_si_true if condicion else valor_si_false

3. Concepto de modo borrador:
   - El borrador es simplemente dibujar con color blanco (255, 255, 255)
   - Cuando presionas E, cambias entre borrador y el color anterior

¿CÓMO FUNCIONA?
──────────────────────────────────────────────────────────────────────────────
- eraser_mode almacena si estamos borrando o no
- previous_color guarda el último color de dibujo (no borrador)
- Presionar E activa/desactiva el borrador
- Si estamos borrando: current_color = (255, 255, 255) [blanco = invisible]
- Si desactivamos: volvemos a previous_color

Truco: Borrar es solo dibujar con el color del fondo (blanco)
"""

import py5

# ════════════════════════════════════════════════════════════════════════════
# VARIABLES DE ESTADO
# ════════════════════════════════════════════════════════════════════════════

current_color = (0, 0, 0)           # Color actual de dibujo
previous_color = current_color      # Guarda el último color de dibujo (antes de borrador)
eraser_mode = False                 # ¿Estamos en modo borrador?


def setup():
    """
    Configuración inicial
    """
    py5.size(700, 500)
    py5.background(255)        # Fondo blanco
    py5.stroke_weight(12)


def draw():
    """
    Loop de dibujo: muestra instrucciones y estado actual
    """
    # Panel de instrucciones
    py5.fill(240)
    py5.no_stroke()
    py5.rect(0, 0, py5.width, 75)
    
    py5.fill(0)
    py5.text_size(14)
    py5.text("PASO 3: Modo borrador (toggle)", 10, 20)
    py5.text("Presiona: 1=NEGRO | 2=ROJO | E=BORRADOR | C=LIMPIAR", 10, 40)
    
    # Mostrar estado actual
    if eraser_mode:
        estado = "🗑️ BORRADOR ACTIVO"
        py5.fill(255, 100, 100)  # Rojo suave para indicar borrador
    else:
        estado = f"✏️  RGB{current_color}"
        py5.fill(100, 200, 100)  # Verde suave para indicar dibujo normal
    
    py5.text(f"Modo: {estado}", 10, 65)


def mouse_dragged():
    """
    Dibuja mientras arrastras el mouse.
    En modo borrador: dibuja blanco (que borra)
    En modo normal: dibuja con current_color
    """
    py5.stroke(*current_color)
    py5.stroke_weight(12)
    py5.point(py5.mouse_x, py5.mouse_y)


def key_pressed():
    """
    Maneja la interacción por teclado.
    Introduce el concepto de "toggle": cambiar entre dos estados
    """
    global current_color, previous_color, eraser_mode
    
    key = py5.key
    
    if key == '1':
        # Cambiar a color negro
        eraser_mode = False
        current_color = (0, 0, 0)
        previous_color = current_color
        print("✓ Color: NEGRO")
        
    elif key == '2':
        # Cambiar a color rojo
        eraser_mode = False
        current_color = (255, 0, 0)
        previous_color = current_color
        print("✓ Color: ROJO")
        
    elif key.lower() == 'e':
        # TOGGLE: cambiar el modo borrador
        eraser_mode = not eraser_mode  # Invierte el valor booleano
        
        # Si activamos borrador: usar blanco
        # Si desactivamos: usar previous_color
        current_color = (255, 255, 255) if eraser_mode else previous_color
        
        modo = "ACTIVADO" if eraser_mode else "DESACTIVADO"
        print(f"✓ Borrador {modo}")
        
    elif key.lower() == 'c':
        # Limpiar canvas
        py5.background(255)
        print("✓ Pizarra limpiada")


if __name__ == '__main__':
    py5.run_sketch()
