"""
PASO 14: Filtro DILATE - Morfología: expansión
Expandir áreas blancas en imagen binaria
"""

import py5


def setup():
    """Configuración."""
    py5.size(400, 400)
    print("✓ Cargando imagen...")


def draw():
    """
    Mostrar imagen con filtro DILATE.
    DILATE: expande áreas blancas (píxeles claros)
    Operación morfológica fundamental en visión por computadora
    """
    # Cargar imagen
    try:
        img = py5.load_image("img/imagen.jpg")
    except:
        print("⚠️  Error: Coloca imagen en img/imagen.jpg")
        return
    
    # Mostrar imagen escalada a 400x400
    py5.image(img, 0, 0, 400, 400)
    
    # Aplicar DILATE
    # Expande áreas blancas (>128 en escala de grises)
    # O áreas de 255 en imagen binaria
    py5.apply_filter(py5.DILATE)


if __name__ == "__main__":
    py5.run_sketch()


# CONCEPTOS: MORFOLOGÍA MATEMÁTICA
"""
OPERACIONES MORFOLÓGICAS:

1. DILATE (Expansión)
   • Agranda áreas blancas
   • Llena pequeños huecos
   • Conecta objetos cercanos

2. ERODE (Erosión) [no en py5]
   • Reduce áreas blancas
   • Separa objetos pegados
   • Elimina detalles pequeños

3. OPENING (Apertura) [erosión + dilatación]
   • Elimina ruido pequeño
   • Suaviza bordes

4. CLOSING (Cierre) [dilatación + erosión]
   • Llena huecos
   • Conecta objetos


CÓMO FUNCIONA DILATE:

Para cada píxel:
  1. Mirar píxel y sus 8 vecinos
  2. Si ALGUNO es blanco (255)
  3. Entonces hacer este píxel blanco

Resultado: áreas blancas crecen ~1 píxel en todas direcciones


EJEMPLO VISUAL:

Antes (binaria):
  █ . . █
  . . . .
  . . . .
  █ . . █

Después de DILATE:
  █ █ █ █
  █ █ █ █
  █ █ █ █
  █ █ █ █


USOS PRÁCTICOS:

1. LLENAR HUECOS
   Imagen binaria con agujeros
   apply_filter(THRESHOLD, 0.5)
   apply_filter(DILATE)
   → Agujeros desaparecen

2. CONECTAR OBJETOS CERCANOS
   Múltiples componentes separados
   DILATE hasta que se toquen
   Luego contar componentes conectados

3. SUAVIZAR BORDES
   Imagen ruidosa
   apply_filter(DILATE)
   apply_filter(BLUR)
   → Bordes más suaves

4. PREPARACIÓN PARA OCR
   DILATE para llenar letras rotas
   → Mejor reconocimiento de caracteres


COMBINACIONES:

DILATE + ERODE = OPEN
  Limpia ruido pequeño
  Abre conexiones espurias

ERO DE + DILATE = CLOSE
  Llena huecos
  Cierra grietas


ESTRUCTURA (Kernel):

La estructura define vecinos a considerar:

Cross (4-vecinos):
    .
  . █ .
    .

Square (8-vecinos): [por defecto]
  . . .
  . █ .
  . . .

Diamond:
    .
  . █ .
    .


COMPARATIVA: BLUR vs DILATE

BLUR:
  • Promedia todos los vecinos
  • Suaviza gradualmente
  • Mantiene escala de grises
  • Resultado: bordes difusos

DILATE:
  • "Máximo" de los vecinos (cualquiera blanco?)
  • Expansión binaria
  • Mejor para imagen binaria
  • Resultado: bordes afilados pero expandidos


EXPERIMENTA:

1. Compara 013 (BLUR) vs 014 (DILATE)
   ¿Qué ves diferente?

2. Primero THRESHOLD, luego DILATE:
   apply_filter(THRESHOLD, 0.5)
   apply_filter(DILATE)
   Observa: pequeños detalles desaparecen

3. Combina operaciones:
   apply_filter(THRESHOLD, 0.5)  # Binaria
   apply_filter(DILATE)           # Crece
   apply_filter(BLUR, 3)          # Suaviza
   
   ¿Cómo se ve?

4. Múltiples DILATE:
   for i in range(3):
       apply_filter(DILATE)
   
   Cada DILATE expande más
"""
