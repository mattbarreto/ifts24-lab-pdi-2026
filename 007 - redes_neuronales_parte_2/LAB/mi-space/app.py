# Ejemplo conceptual de app.py

import gradio as gr
from transformers import pipeline
from PIL import Image

print('✦ Inicializando la aplicación y cargando recursos de Deep Learning...')

# 1. CARGA DEL MODELO: Se ejecuta una única vez al levantar el contenedor para evitar sobrecostos en cada consulta
clasificador = pipeline(
    'image-classification',
    model='google/vit-base-patch16-224'
)
print('✓ Modelo Vision Transformer cargado y listo.')

# 2. FUNCIÓN DE NEGOCIO: Procesa la entrada recibida desde el frontend interactivo
def clasificar_imagen(imagen):
    """
    Procesa la imagen provista por el usuario y estima las categorías.
    """
    if imagen is None:
        return {'Error': 'No se cargó ninguna imagen'}
        
    try:
        # Inferencia con ViT
        resultados = clasificador(imagen)
        
        # Formateamos los resultados en el diccionario que espera gr.Label {etiqueta: score}
        predicciones_formateadas = {}
        for res in resultados[:5]:
            predicciones_formateadas[res['label']] = float(res['score'])
            
        return predicciones_formateadas
    except Exception as e:
        return {'Error en inferencia': str(e)}

# 3. INTERFAZ GRADIO: Definimos el diseño de la UI
demo = gr.Interface(
    fn=clasificar_imagen,
    inputs=gr.Image(type='pil', label='Suban una imagen'),
    outputs=gr.Label(num_top_classes=5, label='Predicciones de ImageNet'),
    title='Clasificador de Imágenes con ViT',
    description='Carguen una imagen para que el modelo estime su categoría conceptual de ImageNet.',
)

# 4. LANZAMIENTO DE LA APLICACIÓN
if __name__ == '__main__':
    print('✦ Iniciando el servidor local de Gradio...')
    demo.launch()
