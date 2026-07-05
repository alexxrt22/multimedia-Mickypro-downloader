import os
from pytubefix import YouTube  # Tu librería de confianza que sí te funciona
import streamlit as st

# 1. Configuración visual de la ventana del navegador
st.set_page_config(
    page_title="YouTube Pro Downloader",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. Inyección de CSS para diseño Premium moderno (Modo Oscuro)
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .stApp {
        background: linear-gradient(135deg, #0f0f11 0%, #1a1a24 100%);
        font-family: 'Inter', sans-serif;
    }
    
    .main-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 40px 30px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.5);
        backdrop-filter: blur(10px);
        margin-top: 20px;
        text-align: center;
    }
    
    .main-title {
        font-size: 42px !important;
        font-weight: 800 !important;
        background: linear-gradient(90deg, #FF0000 0%, #FF4D4D 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
        letter-spacing: -1px;
    }
    
    .subtitle { font-size: 16px; color: #b3b3b3; margin-bottom: 35px; }
    
    .info-box {
        background: rgba(255, 255, 255, 0.02);
        border-left: 4px solid #FF0000;
        padding: 15px;
        border-radius: 8px;
        margin: 20px 0;
        text-align: left;
    }
    
    div.stButton > button {
        background: linear-gradient(90deg, #FF0000 0%, #CC0000 100%) !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
        padding: 12px 24px !important;
        border-radius: 10px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(255,0,0,0.2) !important;
    }
    div.stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(255,0,0,0.4) !important;
    }
    
    div.stDownloadButton > button {
        background: linear-gradient(90deg, #28a745 0%, #218838 100%) !important;
        color: white !important;
        font-weight: bold !important;
        border: none !important;
        padding: 12px 24px !important;
        border-radius: 10px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(40,167,69,0.2) !important;
    }
    div.stDownloadButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(40,167,69,0.4) !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 3. Encabezado de la página web
st.markdown(
    """
    <div class="main-card">
        <div class="main-title">🚀 PRO DOWNLOADER</div>
        <div class="subtitle">Descarga contenido multimedia en la máxima calidad original disponible</div>
    </div>
    """,
    unsafe_allow_html=True,
)
st.write("")

# Entrada de datos directo en la ventana de Chrome
enlace = st.text_input(
    "Pega el enlace multimedia aquí:",
    placeholder="https://youtube.com...",
)

# Selector elegante para elegir el formato antes de descargar
tipo_descarga = st.selectbox(
    "¿Qué formato deseas obtener?",
    ["Video en Alta Calidad (MP4)", "Solo Audio (MP3)"],
)


# 4. Función de descarga exacta basada en tu lógica original de pytubefix
def procesar_descarga(url_link, es_audio):
    yt = YouTube(url_link)

    if es_audio:
        # Extrae solo la pista de sonido más alta
        stream = yt.streams.get_audio_only()
        nombre_archivo = "audio_descargado.mp3"
    else:
        # Tu comando original exacto para máxima calidad
        stream = yt.streams.get_highest_resolution()
        nombre_archivo = "video_descargado.mp4"

    # Descarga el archivo de forma local temporal
    stream.download(filename=nombre_archivo)

    metadata = {
        "title": yt.title,
        "author": yt.author,
        "length": yt.length,
        "filename": nombre_archivo,
    }
    return nombre_archivo, metadata


# 5. Ejecución e interfaz de respuesta
if enlace:
    if st.button("🔥 PROCESAR ENLACE", use_container_width=True):
        es_audio = tipo_descarga == "Solo Audio (MP3)"
        ext_final = "mp3" if es_audio else "mp4"
        tipo_mime = "audio/mpeg" if es_audio else "video/mp4"

        with st.spinner("Conectando con YouTube de forma segura..."):
            try:
                archivo_local, meta = procesar_descarga(enlace, es_audio)

                # Calcular la duración del video
                minutos = meta["length"] // 60
                segundos = meta["length"] % 60

                # Mostrar tarjeta informativa elegante
                st.markdown(
                    f"""
                    <div class="info-box">
                        <b style="color:#FF4D4D;">📌 Contenido Listo:</b> {meta['title']}<br>
                        <b>👤 Canal/Autor:</b> {meta['author']}<br>
                        <b>⏱️ Duración:</b> {minutos}:{segundos:02d} minutos<br>
                        <b>💎 Formato elegido:</b> {tipo_descarga}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                # 💡 RESPUESTA A TU DUDA: En las aplicaciones de navegador, Chrome decide dónde guardarlo.
                # Al hacer clic en este botón verde, se abrirá la ventana normal de tu PC para que elijas
                # en qué carpeta exacta deseas salvar el video o canción.
                with open(archivo_local, "rb") as file:
                    st.download_button(
                        label=f"📥 CLIC AQUÍ PARA GUARDAR EN TU PC (Elegir Carpeta)",
                        data=file,
                        file_name=f"{meta['title']}.{ext_final}",
                        mime=tipo_mime,
                        use_container_width=True,
                    )

                # Limpieza de temporales
                if os.path.exists(archivo_local):
                    os.remove(archivo_local)

            except Exception as error_det:
                st.error(
                    f"Hubo un problema al procesar con tu librería. Detalle: {error_det}"
                )
