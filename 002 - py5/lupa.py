## 2. Actividad 1: La lupa de píxeles

### ¿Qué vamos a hacer?
'''
Vamos a construir un inspector visual: al mover el mouse sobre una imagen, el programa va a leer el color exacto del píxel que está bajo el cursor, mostrarlo ampliado en un cuadrado a la derecha y desplegar sus valores R, G y B en pantalla.

El concepto clave es que cada coordenada `(x, y)` de la imagen corresponde a un píxel que almacena tres números. Ese es el fundamento de toda operación de procesamiento digital de imágenes.
'''
### Referencia a sketches anteriores
'''
Este ejercicio combina lo que ya hicieron en:
- `005_upload_img.py`: carga de una imagen desde archivo.
- `006_pixeles.py`: acceso a la matriz de píxeles.
- `009_mouse.py`: uso de las coordenadas del mouse.
'''
### Código
'''
Creá un archivo llamado `lupa.py` y copiá este bloque completo:
'''

import py5

img = None
mx=0
my=0
color_del_pixel = None
color_pixel=None    

def setup():
    global img
    py5.size(800, 400)
    img = py5.load_image("img/imagen.jpg")  # Usá una imagen disponible en tu carpeta img/
    img.resize(400, 400)

def draw():
    py5.background(255)

    #Mostrar la imagen en la mitad izquierda
    py5.image(img, 0, 0)

    # Limitar las coordenadas del mouse al área de la imagen
    # Esto evita errores si el cursor sale de la imagen
    mx = py5.constrain(py5.mouse_x, 0, 399)
    my = py5.constrain(py5.mouse_y, 0, 399)

    #obtener color en esa posición
    color_pixel = py5.get_pixels(mx, my)
    
    # # Separar el color en sus tres canales
    r = py5.red(color_pixel)
    g = py5.green(color_pixel)
    b = py5.blue(color_pixel)

    # # Mostrar el color como un cuadrado en la mitad derecha (la "lupa")
    py5.fill(color_pixel)
    py5.stroke(0)
    py5.rect(450, 50, 300, 300)

    # # Mostrar los valores numéricos
    py5.fill(0)
    py5.text_size(18)
    py5.text(f"Posición: ({mx}, {my})", 450, 30)
    py5.text(f"R: {r:.0f}   G: {g:.0f}   B: {b:.0f}", 450, 380)

def color_del_pixel():
    color_pixel = py5.color(mx, my)
    print(color_pixel)
    
py5.run_sketch()


### ¿Qué hace cada parte?
'''
| Línea / función | Explicación |
|---|---|
| `img.resize(400, 400)` | Ajusta la imagen a un tamaño fijo para que las coordenadas sean predecibles. |
| `py5.constrain(valor, min, max)` | Limita un número dentro de un rango. Acá asegura que el mouse no acceda a posiciones fuera de la imagen, lo que causaría un error. |
| `py5.get(x, y)` | Lee el color del píxel en la posición `(x, y)`. Devuelve un valor compacto que contiene R, G y B juntos. |
| `py5.red()`, `py5.green()`, `py5.blue()` | Extraen cada canal de color por separado a partir del color compacto. |
| `py5.fill(color_pixel)` | Establece el color de relleno para las figuras que se dibujen a continuación. |
'''
### Para experimentar
'''
Una vez que el sketch funcione, probá estas variaciones. Modificá una cosa a la vez y observá el resultado:

1. **Color negativo:** Reemplazá `py5.fill(color_pixel)` por `py5.fill(255 - r, 255 - g, 255 - b)`. El color del cuadrado debería ser el complementario del píxel original. ¿Qué color aparece sobre un rojo puro? ¿Y sobre el blanco?

2. **Aislamiento de canal:** Ahora usá `py5.fill(r, 0, 0)`. Esto elimina verde y azul y muestra solo la contribución del canal rojo. Pasá el cursor por zonas azules o verdes de la imagen y observá cuánto rojo tienen en realidad.

3. **Sin protección:** Comentá la línea con `py5.constrain()` reemplazándola por `mx = py5.mouse_x` y `my = py5.mouse_y`. Mové el mouse fuera de la imagen rápidamente. ¿Qué mensaje de error aparece en la terminal? ¿Qué tipo de error es?
'''
