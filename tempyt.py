import os
from tkinter import *
from tkinter import messagebox as MessageBox
from pytubefix import YouTube


def descargar_video():
    enlace = entrada_url.get()

    if not enlace:
        MessageBox.showwarning("Alerta", "Por favor, pega un link de YouTube.")
        return

    try:
        yt = YouTube(enlace)
        video_alta_calidad = yt.streams.get_highest_resolution()
        video_alta_calidad.download()

        MessageBox.showinfo(
            "Éxito", f"¡Descargado con éxito!\n\nTítulo: {yt.title}"
        )
        entrada_url.delete(0, END)

    except Exception as error:
        MessageBox.showerror(
            "Error", f"Hubo un problema al descargar.\nDetalle: {error}"
        )


# --- CONFIGURACIÓN DE LA VENTANA ---
root = Tk()
root.title("Descargador de YouTube Premium")
root.config(bd=20, bg="#1e1e1e")

# --- SOLUCIÓN AL ERROR DE IMAGEN ---
# Con este bloque, si el PNG da error, el programa no se rompe y sigue abriendo la ventana
try:
    imagen = PhotoImage(file="youtube.png")
    foto = Label(root, image=imagen, bd=0, bg="#1e1e1e")
    foto.pack(pady=10)
except Exception:
    # Si Tkinter no reconoce el formato PNG, simplemente muestra un aviso visual bonito en texto
    logo_alternativo = Label(
        root,
        text="▶ YouTube Downloader",
        font=("Arial", 20, "bold"),
        fg="#FF0000",
        bg="#1e1e1e",
    )
    logo_alternativo.pack(pady=15)

# Texto de instrucciones
instrucciones = Label(
    root,
    text="Pega el link de YouTube aquí abajo:",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#1e1e1e",
)
instrucciones.pack(pady=5)

# Caja de entrada
entrada_url = Entry(
    root,
    width=50,
    font=("Arial", 11),
    bd=3,
    relief="groove",
    justify="center",
)
entrada_url.pack(pady=10)
entrada_url.focus()

# Botón de descarga
boton = Button(
    root,
    text="¡DESCARGAR EN ALTA CALIDAD!",
    command=descargar_video,
    font=("Arial", 11, "bold"),
    bg="#FF0000",
    fg="white",
    padx=20,
    pady=8,
    cursor="hand2",
    activebackground="#CC0000",
    activeforeground="white",
)
boton.pack(pady=15)

root.mainloop()
