"""
╔════════════════════════════════════════════════════════════════════════════╗
║ PIZARRA PASO 4: Interfaz gráfica con botones clickeables                   ║
╚════════════════════════════════════════════════════════════════════════════╝

¿QUÉ APRENDEREMOS?
──────────────────────────────────────────────────────────────────────────────
En este paso creamos una interfaz gráfica más profesional:

1. Estructuras de datos avanzadas:
   - Listas de diccionarios para almacenar botones
   - Cada botón contiene propiedades (posición, tamaño, etiqueta, etc.)

2. Detección de colisiones (hit detection):
   - Verificar si el click del mouse está dentro de un rectángulo
   - Fundamento de todas las interfaces gráficas

3. Retroalimentación visual:
   - Cambiar el color del botón activo (verde)
   - Usuario sabe qué opción está seleccionada

4. Separación de áreas:
   - Área de controles (botones): y < 120
   - Área de dibujo: y > 120
   - mouse_dragged solo funciona en área de dibujo

¿CÓMO FUNCIONA?
──────────────────────────────────────────────────────────────────────────────
1. Almacenamos cada botón como un diccionario con sus propiedades
2. En draw(), iteramos sobre la lista y dibujamos cada botón
3. Si el botón está activo, se ilumina en verde
4. En mouse_pressed(), verificamos si el click está dentro de un botón
5. Si sí, ejecutamos la acción correspondiente

Este patrón es la base de casi todas las interfaces gráficas modernas.
"""

import py5

# ════════════════════════════════════════════════════════════════════════════
# VARIABLES DE ESTADO
# ════════════════════════════════════════════════════════════════════════════

current_color = (0, 0, 0)           # Color actual de dibujo
previous_color = current_color      # Guarda el último color de dibujo
eraser_mode = False                 # ¿Modo borrador activo?

# ════════════════════════════════════════════════════════════════════════════
# DEFINICIÓN DE BOTONES (Estructura de datos)
# ════════════════════════════════════════════════════════════════════════════
# Cada botón es un diccionario con sus propiedades:
#   "x", "y": posición (esquina superior izquierda)
#   "w", "h": ancho y alto
#   "label": texto a mostrar
#   "color": color de fondo (RGB)
#   "key": identificador único del botón

buttons = [
    {"x": 10,  "y": 60, "w": 70, "h": 40, "label": "NEGRO",    "color": (200, 200, 200), "key": "negro"},
    {"x": 90,  "y": 60, "w": 70, "h": 40, "label": "ROJO",     "color": (255, 150, 150), "key": "rojo"},
    {"x": 170, "y": 60, "w": 70, "h": 40, "label": "BORRADOR", "color": (200, 200, 200), "key": "eraser"},
    {"x": 250, "y": 60, "w": 70, "h": 40, "label": "LIMPIAR",  "color": (150, 200, 255), "key": "limpiar"},
]


def setup():
    """
    Configuración inicial
    """
    py5.size(700, 500)
    py5.background(255)        # Fondo blanco
    py5.stroke_weight(12)      # Grosor para dibujar


def draw():
    """
    Loop de dibujo principal.
    Dibuja: panel de instrucciones, botones y estado actual.
    """
    # Panel de instrucciones en la parte superior
    py5.fill(240)
    py5.no_stroke()
    py5.rect(0, 0, py5.width, 50)
    
    py5.fill(0)
    py5.text_size(14)
    py5.text("PASO 4: Interfaz gráfica con botones", 10, 20)
    py5.text("Haz clic en los botones para cambiar opciones", 10, 40)
    
    # Dibujar todos los botones
    draw_buttons()
    
    # Mostrar estado actual
    estado = "🗑️ BORRADOR" if eraser_mode else f"✏️ RGB{current_color}"
    py5.fill(0)
    py5.text_size(12)
    py5.text(f"Estado: {estado}", 10, 120)


def draw_buttons():
    """
    Dibuja todos los botones de la interfaz.
    Cada botón se ilumina en verde si está activo.
    
    Este es un ejemplo de iteración sobre una estructura de datos
    para renderizar componentes de UI.
    """
    for button in buttons:
        # ────────────────────────────────────────────────────────────
        # PASO 1: Determinar si este botón está activo
        # ────────────────────────────────────────────────────────────
        is_active = False
        
        if button["key"] == "negro" and current_color == (0, 0, 0) and not eraser_mode:
            is_active = True
        elif button["key"] == "rojo" and current_color == (255, 0, 0) and not eraser_mode:
            is_active = True
        elif button["key"] == "eraser" and eraser_mode:
            is_active = True
        
        # ────────────────────────────────────────────────────────────
        # PASO 2: Dibujar el rectángulo del botón
        # ────────────────────────────────────────────────────────────
        # Color verde si está activo, su color predefinido si no
        if is_active:
            py5.fill(100, 200, 100)  # Verde claro para botón activo
        else:
            py5.fill(*button["color"])  # Color normal del botón
        
        py5.stroke(0)              # Contorno negro
        py5.stroke_weight(2)
        py5.rect(button["x"], button["y"], button["w"], button["h"])
        
        # ────────────────────────────────────────────────────────────
        # PASO 3: Dibujar el texto del botón
        # ────────────────────────────────────────────────────────────
        py5.fill(0)                # Texto negro
        py5.text_size(11)
        
        # Centrar el texto horizontalmente en el botón
        text_x = button["x"] + button["w"] // 2 - len(button["label"]) * 3
        text_y = button["y"] + button["h"] // 2 + 5
        py5.text(button["label"], text_x, text_y)


def mouse_pressed():
    """
    Se ejecuta cuando presionas un botón del mouse.
    
    Implementa DETECCIÓN DE COLISIONES (hit detection):
    Verificamos si las coordenadas del click están dentro de algún botón.
    Esta es la técnica fundamental para toda interfaz gráfica.
    
    Fórmula:
    punto_dentro_rect = (x_min <= x_punto <= x_max) AND (y_min <= y_punto <= y_max)
    """
    global current_color, previous_color, eraser_mode
    
    # Iterar sobre todos los botones
    for button in buttons:
        # Verificar si el click está dentro del botón
        # (usando la fórmula de colisión punto-rectángulo)
        x_dentro = button["x"] <= py5.mouse_x <= button["x"] + button["w"]
        y_dentro = button["y"] <= py5.mouse_y <= button["y"] + button["h"]
        
        if x_dentro and y_dentro:
            # ¡El click está dentro de este botón!
            # Ejecutar la acción correspondiente
            
            if button["key"] == "negro":
                eraser_mode = False
                current_color = (0, 0, 0)
                previous_color = current_color
                print("✓ Botón presionado: NEGRO")
                
            elif button["key"] == "rojo":
                eraser_mode = False
                current_color = (255, 0, 0)
                previous_color = current_color
                print("✓ Botón presionado: ROJO")
                
            elif button["key"] == "eraser":
                eraser_mode = not eraser_mode
                current_color = (255, 255, 255) if eraser_mode else previous_color
                modo = "ACTIVADO" if eraser_mode else "DESACTIVADO"
                print(f"✓ Botón presionado: BORRADOR {modo}")
                
            elif button["key"] == "limpiar":
                py5.background(255)
                print("✓ Botón presionado: LIMPIAR")
            
            return  # Importante: salir del bucle para evitar procesar múltiples botones


def mouse_dragged():
    """
    Dibuja mientras arrastras el mouse.
    Solo funciona en el área de dibujo (por debajo de los botones).
    
    Esto evita que accidentalmente dibujes cuando intentas hacer clic en botones.
    """
    # Área de seguridad: solo dibujar si estamos por debajo de y=120
    if py5.mouse_y > 120:
        py5.stroke(*current_color)
        py5.stroke_weight(12)
        py5.point(py5.mouse_x, py5.mouse_y)


if __name__ == '__main__':
    py5.run_sketch()
