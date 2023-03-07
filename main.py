import customtkinter
from tkinter import *
from moviepy.video.io.VideoFileClip import VideoFileClip

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("1920x1080")
janela.title("Playstation 5")
janela.iconbitmap("img//ico.ico")
janela.resizable(False, False)

img = PhotoImage(file="img//fundo2.png")
label_img = customtkinter.CTkLabel(master=janela,image=img)
label_img.place(x=0, y=0)

aumentado = False
imagem = PhotoImage(file='img//fundo.png',width=150, height=150)
imagem_aumentada = PhotoImage(file='img//fundo.png',width=300, height=300)

def aumentar(event):
    global aumentado
    if not aumentado:
        aumentado = True
        if isinstance(event.widget, customtkinter.CTkLabel):
            video = VideoFileClip("video//thelast.mp4")
            event.widget.video_label = customtkinter.CTkLabel(master=janela, video=video)
            event.widget.video_label.place(x=event.widget.winfo_x(), y=event.widget.winfo_y())
            event.widget.config(image=imagem_aumentada)

def diminuir(event):
    global aumentado
    if aumentado:
        aumentado = False
        if isinstance(event.widget, customtkinter.CTkLabel):
            if hasattr(event.widget, "video_label"):
                event.widget.video_label.destroy()
                del event.widget.video_label
            event.widget.config(image=imagem)

label = customtkinter.CTkLabel(master=janela, text="Games",font=("Arial", 15),text_color="white")
label.place(x=40 ,y=20)

imagem = PhotoImage(file='img//fundo.png',width=150, height=150)

jogo1 = customtkinter.CTkLabel(master=janela,image=imagem,bg_color="transparent" ,cursor="hand2")
jogo1.place(x=40,y=60)

jogo1.bind("<Enter>", aumentar)
jogo1.bind("<Leave>", diminuir)

janela.mainloop()

