from tkinter import messagebox
import PIL.Image
from PIL import ImageTk

from topLevel import *

import threading
import keyboard
import time
import pyautogui


window = Tk()
window.title("MouseAutoclick")
window.geometry("340x260")
window.config(bg='#f2f2f2')

window.resizable(False, False)
icone = tk.PhotoImage(file="./assets/mouse.png")
window.iconphoto(False, icone)

frame_body = Frame(window, width=340, height=260)
frame_body.grid(row=0, column=0)

# Definindo a variável para armazenar o texto do botão
key = StringVar()
key.set(load_key())
buttonText = key

# Inserindo a imagem
image_path = "./assets/mouse.png"
images = PIL.Image.open(image_path)  # Abre a imagem com Pillow
photo = ImageTk.PhotoImage(images)
origin_width, origin_height = images.size

# Definir a nova largura e altura mantendo a proporção
new_width = 72
new_height = int((new_width / origin_width) * origin_height)

resized_image = images.resize((new_width, new_height), PIL.Image.LANCZOS)
icon_logo = ImageTk.PhotoImage(resized_image)

icon = Label(frame_body, image=icon_logo)
icon.pack()
icon.place(relx=.5, rely=.1, anchor='n')

# Criar o Canvas e desenhar o botão personalizado
canvas = tk.Canvas(frame_body, width=200, height=50, bg="#f2f2f2", highlightthickness=0)
canvas.place(relx=0.5, rely=0.5, anchor="center")

radius = 20
x0, y0, x1, y1 = 10, 10, 190, 40
canvas.create_arc((x0, y0, x0 + radius, y0 + radius), start=90, extent=90, fill=color, outline=color)
canvas.create_arc((x1 - radius, y0, x1, y0 + radius), start=0, extent=90, fill=color, outline=color)
canvas.create_arc((x0, y1 - radius, x0 + radius, y1), start=180, extent=90, fill=color, outline=color)
canvas.create_arc((x1 - radius, y1 - radius, x1, y1), start=270, extent=90, fill=color, outline=color)
canvas.create_rectangle((x0 + radius / 2, y0, x1 - radius / 2, y1), fill=color, outline=color)
canvas.create_rectangle((x0, y0 + radius / 2, x1, y1 - radius / 2), fill=color, outline=color)

canvatext = canvas.create_text(100, 25, text=buttonText.get(), fill="#f2f2f2", font=("Arial", 12, "bold"))

# Atualizando o texto do canvas ao alterar a keypress
def update_text(*args):
    canvas.itemconfig(canvatext, text=buttonText.get())

canvas.bind("<Button-1>", lambda event: on_button_click(event, key, window, Toplevel, Label, Frame, tk))
buttonText.trace_add("write", update_text)

text = Label(frame_body, text='Mude o botão de ativação do autoclick\npressionando o botão laranja com\no ponteiro do mouse.')
text.place(relx=.5, rely=.7, anchor='n')


# inserindo a engrenagem para abrir a janela de configuração
# Inserindo a imagem
image_gear = PIL.Image.open("./assets/gear.png")
origin_width_gear, origin_height_gear = image_gear.size

# Definir a nova largura e altura mantendo a proporção
new_width_gear = 28
new_height_gear = int((new_width_gear / origin_width_gear) * origin_height_gear)

resized_image_gear = image_gear.resize((new_width_gear, new_height_gear), PIL.Image.LANCZOS)
icon_gear = ImageTk.PhotoImage(resized_image_gear)

gear = Button(frame_body, image=icon_gear, command = lambda: settingsWindow(window, tk), relief=FLAT, highlightthickness=0, overrelief=FLAT, borderwidth=0, background='#f2f2f2')
gear.pack()
gear.place(relx=.93, rely=.08, anchor='center')

# Variável global para controlar o estado do autoclicker
autoclick_enabled = False
autoclick_thread_started = False  # Sinalizador para iniciar a thread de autoclicker

def toggle_autoclick():
    global autoclick_enabled, autoclick_thread_started
    autoclick_enabled = not autoclick_enabled

    if autoclick_enabled and not autoclick_thread_started:
        # Inicia a função de autoclicker em uma thread separada
        autoclick_thread = threading.Thread(target=autoclick, daemon=True)
        autoclick_thread.start()
        autoclick_thread_started = True

def autoclick():
    while True:
        if autoclick_enabled:
            button_load = load('button')
            clicks_load = load('clicks')
            pyautogui.click(button=button_load, clicks=clicks_load)  # Executa o clique do mouse
        time_interval = float(load("interval")) / 1000.0
        time.sleep(time_interval)  # Intervalo entre cliques

def on_key_event(event):
    toggle_key = load_key()
    if str(event.name).lower() == toggle_key.lower():
        toggle_autoclick()

def run_keyboard_listener():
    keyboard.on_press(on_key_event)
    keyboard.wait()

# Criar e iniciar a thread para o listener de teclado
global listener_thread
listener_thread = threading.Thread(target=run_keyboard_listener, daemon=True)
listener_thread.start()

window.mainloop()
