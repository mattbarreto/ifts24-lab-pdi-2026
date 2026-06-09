import streamlit as st
from PIL import Image
from transformers import pipeline

@st.cache_resource
def cargar_modelo():
    return pipeline(
        task="image-classification",
        model="julien-c/hotdog-not-hotdog"
    )
clasificador = cargar_modelo()
st.title("Clasificador básico de imágenes")
st.write("Demo simple con Streamlit + Transformers + Hugging Face Spaces.")
archivo = st.file_uploader(
    "Subí una imagen",
    type=["jpg", "jpeg", "png"]
)
if archivo is not None:
    imagen = Image.open(archivo).convert("RGB")
    st.image(imagen, caption="Imagen cargada", use_container_width=True)
    predicciones = clasificador(imagen)
    st.subheader("Resultado")
    for prediccion in predicciones:
        etiqueta = prediccion["label"]
        puntaje = prediccion["score"]
        st.write(f"{etiqueta}: {puntaje:.2%}")
        st.progress(float(puntaje))