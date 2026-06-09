mport gradio as gr
from transformers import pipeline
clasificador = pipeline(
    task="image-classification",
    model="julien-c/hotdog-not-hotdog"
)
Manual Hugging Face Spaces - Página 4
def clasificar_imagen(imagen):
    predicciones = clasificador(imagen)
    resultados = {
        prediccion["label"]: prediccion["score"]
        for prediccion in predicciones
    }
    return resultados
demo = gr.Interface(
    fn=clasificar_imagen,
    inputs=gr.Image(type="pil", label="Subí una imagen"),
    outputs=gr.Label(num_top_classes=2, label="Resultado"),
    title="Clasificador básico de imágenes",
    description="Demo simple con Gradio + Transformers + Hugging Face Spaces."
)
if __name__ == "__main__":
    demo.launch()