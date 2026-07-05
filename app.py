import os
import streamlit as st
import yt_dlp

# 1. Configuración de la página
st.set_page_config(
    page_title="YouTube Pro Downloader",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# 2. Inyección de CSS Avanzado para diseño Premium (Modo Oscuro)
st.markdown(
    """
    <style>
    /* Ocultar elementos por defecto de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Configuración del fondo global */
    .stApp {
        background: linear-gradient(135deg, #0f0f11 0%, #1a1a24 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Contenedor principal tipo Tarjeta Flotante */
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
    
    /* Título principal con degradado encendido */
    .main-title {
        font-size: 42px !important;
        font-weight: 800 !important;
        background: linear-gradient(90deg, #FF0000 0%, #FF4D4D 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
        letter-spacing: -1px;
    }
    
    /* Subtítulo elegante */
    .subtitle {
        font-size: 16px;
        color: #b3b3b3;
        margin-bottom: 35px;
    }
    
    /* Caja de información del video */
    .info-box {
        background: rgba(255, 255, 255, 0.02);
        border-left: 4px solid #FF0000;
        padding: 15px;
        border-radius: 8px;
        margin: 20px 0;
        text-align: left;
    }
    
    /* Personalización del botón de Streamlit vía CSS */
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
    
    /* Botón secundario para descargar archivo */
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

# 3. Renderizado de la Interfaz Estilizada
st.markdown(
    """
    <div class="main-card">
        <div class="main-title">🚀 PRO DOWNLOADER</div>
        <div class="subtitle">Descarga contenido multimedia en la máxima calidad original disponible</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")  # Espaciador técnico

# Contenedor de entrada de datos
url_video = st.text_input(
    "Pega el enlace multimedia aquí:",
    placeholder="https://www.youtube.com/watch?v=...",
)

# Selector de formato elegante integrado en la interfaz
tipo_descarga = st.selectbox(
    "¿Qué formato deseas obtener?",
    ["Video en Alta Calidad (MP4)", "Solo Audio (MP3)"],
)


# 4. Motor de descarga optimizado con simulación de usuario seguro
def procesar_video(url, es_audio):
    # Parámetros para engañar al servidor de YouTube haciéndonos pasar por Chrome
    opciones_seguras = {
        "quiet": True,
        "no_warnings": True,
        "nocheckcertificate": True,
        "ignoreerrors": False,
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "referer": "https://www.youtube.com/",
    }

    if es_audio:
        ydl_opts = {
            **opciones_seguras,
            "format": "bestaudio/best",
            "outtmpl": "audio_descargado.mp3",
        }
    else:
        ydl_opts = {
            **opciones_seguras,
            "format": "best",
            "outtmpl": "video_descargado.mp4",
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        metadata = {
            "title": info.get("title", "Contenido de YouTube"),
            "duration": info.get("duration", 0),
            "uploader": info.get("uploader", "Desconocido"),
            "filename": filename,
        }
        return filename, metadata


# 5. Lógica de ejecución e interfaz de respuesta
if url_video:
    if st.button("🔥 PROCESAR ENLACE", use_container_width=True):
        es_audio = tipo_descarga == "Solo Audio (MP3)"
        ext = "mp3" if es_audio else "mp4"
        mime_type = "audio/mpeg" if es_audio else "video/mp4"

        with st.spinner("Analizando y procesando flujos multimedia..."):
            try:
                archivo_salida, meta = procesar_video(url_video, es_audio)

                # Convertir segundos a formato mm:ss
                minutos = meta["duration"] // 60
                segundos = meta["duration"] % 60

                # Mostrar tarjeta informativa del contenido listo
                st.markdown(
                    f"""
                    <div class="info-box">
                        <b style="color:#FF4D4D;">📌 Contenido Listo:</b> {meta['title']}<br>
                        <b>👤 Canal/Autor:</b> {meta['uploader']}<br>
                        <b>⏱️ Duración:</b> {minutos}:{segundos:02d} minutos<br>
                        <b>💎 Formato:</b> {tipo_descarga}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                # Botón elegante para salvar localmente en el ordenador del usuario
                with open(meta["filename"], "rb") as file:
                    st.download_button(
                        label=f"📥 CLIC AQUÍ PARA GUARDAR .{ext.upper()}",
                        data=file,
                        file_name=f"{meta['title']}.{ext}",
                        mime=mime_type,
                        use_container_width=True,
                    )

                # Eliminar el archivo del servidor web inmediatamente para mantenerlo rápido
                if os.path.exists(meta["filename"]):
                    os.remove(meta["filename"])

            except Exception as e:
                st.error(f"Error técnico en el procesamiento del enlace: {e}")
