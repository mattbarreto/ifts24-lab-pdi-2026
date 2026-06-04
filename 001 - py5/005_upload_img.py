"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║        PASO 5: Cargar y mostrar imágenes - Primeros pasos en PDI              ║
╚═══════════════════════════════════════════════════════════════════════════════╝

¿QUÉ APRENDERÁS?
════════════════════════════════════════════════════════════════════════════════
- Cargar imágenes desde archivos (JPG, PNG, etc.)
- Mostrar imágenes en la ventana
- Redimensionar imágenes
- Acceder a propiedades de imagen (width, height)
- Variables globales (global img)
- FUNDAMENTOS del procesamiento digital de imágenes

PRÁCTICA ANTERIOR
════════════════════════════════════════════════════════════════════════════════
En 004_HSV.py aprendiste:
- Modelo HSB para colores
- Loops: for i in range()
- Cómo generar espectros de color

NOVEDAD: IMÁGENES
════════════════════════════════════════════════════════════════════════════════
- Una imagen es una MATRIZ de píxeles
- Cada píxel tiene propiedades (R, G, B, A)
- py5.load_image() carga imagen desde archivo
- py5.image() muestra imagen en canvas
- Las imágenes tienen propiedades: width, height
"""

import py5


# ════════════════════════════════════════════════════════════════════════════
# VARIABLES GLOBALES
# ════════════════════════════════════════════════════════════════════════════

# Variable para almacenar la imagen
# Se inicializa en None (vacía) hasta cargarla
img = None


# ════════════════════════════════════════════════════════════════════════════
# CONFIGURACIÓN INICIAL
# ════════════════════════════════════════════════════════════════════════════

def setup():
    """
    Cargar imagen en setup() (solo una vez).
    """
    # Necesitamos acceder a la variable global img
    global img
    
    # Crear ventana
    py5.size(800, 450)

    # Cargar imagen desde archivo
    # py5.load_image("ruta/imagen.jpg")
    # IMPORTANTE: La imagen debe existir en la ruta especificada
    # Rutas relativas: "img/imagen.jpg" busca en carpeta "img"
    # NOTA: Si la imagen no existe, img será None
    img = py5.load_image("img/imagen.jpg")  # Cambiar por imagen disponible
    
    if img is None:
        print("⚠️  Imagen no encontrada. Verifica la ruta.")
    else:
        print(f"✓ Imagen cargada: {img.width} × {img.height}")


# ════════════════════════════════════════════════════════════════════════════
# LOOP DE DIBUJO
# ════════════════════════════════════════════════════════════════════════════

def draw():
    """
    Mostrar imagen si fue cargada correctamente.
    """
    # Verificar que la imagen se cargó correctamente
    if img:
        
        # ────────────────────────────────────────────────────────────────────
        # MOSTRAR IMAGEN ORIGINAL
        # ────────────────────────────────────────────────────────────────────
        # py5.image(imagen, x, y, ancho, alto)
        # Si no especificas ancho y alto, usa tamaño original
        # Si especificas, py5 redimensiona automáticamente
        py5.image(img, 0, 0, 400, 400)
        
        # ────────────────────────────────────────────────────────────────────
        # MOSTRAR IMAGEN REDIMENSIONADA
        # ────────────────────────────────────────────────────────────────────
        # Posición: x=400 (al lado de la anterior)
        # Tamaño: 300×300 (redimensionada)
        py5.image(img, 400, 0, 300, 300)

        # ────────────────────────────────────────────────────────────────────
        # MOSTRAR INFORMACIÓN DE LA IMAGEN
        # ────────────────────────────────────────────────────────────────────
        # img.width: ancho original en píxeles
        # img.height: alto original en píxeles
        py5.fill(0)
        py5.text(f"Original: {img.width} x {img.height} píxeles", 10, 420)
        py5.text(f"Mostrada: 400 x 400 y 300 x 300", 10, 440)


if __name__ == "__main__":
    py5.run_sketch()


# ════════════════════════════════════════════════════════════════════════════
# CONCEPTOS: IMÁGENES EN PROCESAMIENTO DIGITAL
# ════════════════════════════════════════════════════════════════════════════

"""
QUÉ ES UNA IMAGEN DIGITAL:

Una imagen es una MATRIZ (grid) de píxeles:

┌─────────────────────────────────────────┐
│ ■ ■ ■ ■ ■ ■ ■ ■ │ 8 píxeles de ancho
│ ■ ■ ■ ■ ■ ■ ■ ■ │
│ ■ ■ ■ ■ ■ ■ ■ ■ │ 3 píxeles de alto
└─────────────────────────────────────────┘

Esta imagen es 8×3 = 24 píxeles totales
Cada píxel contiene: R, G, B, (A)
  • R = Rojo (0-255)
  • G = Verde (0-255)
  • B = Azul (0-255)
  • A = Alfa/Transparencia (opcional)


PROPIEDADES DE UNA IMAGEN:

img.width  → Ancho en píxeles
img.height → Alto en píxeles
img.pixels → Array con todos los píxeles (veremos después)


FORMATOS DE IMAGEN COMUNES:

• JPG (JPEG)
  ├─ Compresión con pérdida
  ├─ Tamaño pequeño
  ├─ Bueno para fotos
  └─ No soporta transparencia

• PNG
  ├─ Compresión sin pérdida
  ├─ Tamaño mediano
  ├─ Preserva toda la información
  └─ Soporta transparencia

• GIF
  ├─ Animado (múltiples frames)
  └─ Antiguo, colores limitados

• TIFF
  ├─ Sin compresión o compresión lossless
  ├─ Muy grande
  └─ Para edición profesional


VARIABLE GLOBAL:

¿Por qué "global img"?

Sin global:
  def setup():
      img = py5.load_image(...)  # crea variable LOCAL
      # img desaparece al salir de setup()

Con global:
  img = None  # variable GLOBAL (nivel del módulo)
  def setup():
      global img  # declara que usaremos la global
      img = py5.load_image(...)  # modifica la GLOBAL
      # img persiste para ser usada en draw()


ERROR COMÚN:

Si la imagen no existe, py5.load_image() devuelve None
  img = None → if img: será False
  No dibujará nada, no habrá error

Por eso verificamos: if img: antes de usarla


EXPERIMENTA:
- Carga una imagen diferente
- Redimensiona a otros tamaños
- Muestra la imagen en múltiples posiciones
- Agrega más información: img.width, img.height


SIGUIENTE PASO: Ver 006_pixeles.py
Aprenderás a MANIPULAR píxeles individuales (core de PDI)
"""
