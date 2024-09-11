from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from tkinter import *
import json
import os

color = "#FF7300"
font = ("Helvetica 18 bold")


# Funções responsáveis por recuperar a chave de ativação definida
def save_key(key):
    try:
        # Carregar dados existentes
        with open("settings.json", "r") as config_file:
            dados_existentes = json.load(config_file)
    except FileNotFoundError:
        dados_existentes = {}

    # Atualizar dados com a nova chave
    dados_existentes["key"] = key

    # Salvar dados atualizados
    with open("settings.json", "w") as config_file:
        json.dump(dados_existentes, config_file, indent=4)


def save(screen, prop, value):
    global valor
    valor = None  # Inicializa 'valor' com None

    try:
        # Verificar se 'value' é um StringVar
        if isinstance(value, tk.StringVar):
            valor = value.get()
            if valor == "esquerdo":
                valor = "left"
            else:
                valor = "right"

        # Verificar se 'value' é um IntVar
        elif isinstance(value, tk.IntVar):
            valor = value.get()

        # Verificar se 'value' é um Entry
        elif isinstance(value, tk.Entry):
            valor = value.get()

            # Se 'valor' for uma string que precisa ser convertida para 'left' ou 'right', faça isso
            if valor == "esquerdo":
                valor = "left"
            elif valor == "direito":
                valor = "right"
            # Se 'valor' for um número, pode ser convertido para int, se necessário
            try:
                valor = int(valor)
            except ValueError:
                pass  # Mantém 'valor' como string, se não puder ser convertido para int

        # Verificar se 'valor' é um inteiro ou string
        if isinstance(valor, (int, str)):
            try:
                # Carregar dados existentes
                with open("settings.json", "r") as config_file:
                    dados_existentes = json.load(config_file)
            except FileNotFoundError:
                dados_existentes = {}

            # Atualizar dados com o novo valor
            if prop == "interval":
                if valor < 1:
                    raise ValueError("Intervalo de clicks não pode ser menor que 1.")
                else:
                    dados_existentes["interval"] = valor
            elif prop == "clicks":
                if valor > 5:
                    raise ValueError("Número de clicks não pode ser maior que 5.")
                else:
                    dados_existentes["clicks"] = valor
            elif prop == "button":
                dados_existentes["button"] = valor

            # Salvar dados atualizados
            with open("settings.json", "w") as config_file:
                json.dump(dados_existentes, config_file, indent=4)

            return True
        else:
            raise ValueError("Tipo de valor inesperado.")

    except ValueError as ve:
        messagebox.showerror("Aviso", str(ve))
        screen.focus_set()


def load_key():
    if os.path.exists("settings.json") and os.path.getsize("settings.json") > 0:
        with open("settings.json", "r") as config_file:
            config = json.load(config_file)
            return config.get("key", "f12")  # Valor padrão é "F12"
    else:
        return "f12"


def load(properties):
    if os.path.exists("settings.json") and os.path.getsize("settings.json") > 0:
        with open("settings.json", "r") as config_file:
            config = json.load(config_file)

            if properties == "interval":
                return config.get("interval", 12)  # Valor padrão é 12 (12 segundos para uma chamada)
            elif properties == "clicks":
                return config.get("clicks", 1)  # Valor padrão é 1 (1 clique por intervalo)
            elif properties == "button":
                return config.get("button", "left")
    else:
        default_config = {
            "interval": 1000,  # Milissegundos
            "clicks": 1,
            "button": "left"
        }

        # Retorna o valor padrão de acordo com a propriedade
        return default_config.get(properties)


def on_key_press(event, key, label):
    if event.keysym.isalpha() or event.keysym.isdigit():
        result = messagebox.showerror("Tecla inválida!", "Use uma tecla não alfanumérica.")
        if result:
            screen_select.focus_set()
    else:
        messagebox.showinfo("Salvo.", "Nova chave salva com sucesso!")
        key.set(event.keysym)
        save_key(event.keysym)
        screen_select.destroy()


def on_button_click(event=None, key=None, window=None, Toplevel=None, Label=None, Frame=None, tk=None):
    global screen_select
    screen_select = Toplevel(window)
    screen_select.title("Seleção de chave")
    screen_select.geometry("320x200")
    screen_select.config(bg='#f2f2f2')

    screen_select.resizable(False, False)
    icone = tk.PhotoImage(file="./assets/mouse.png")
    screen_select.iconphoto(False, icone)

    frame_select_body = Frame(screen_select, width=320, height=200)
    frame_select_body.grid(row=0, column=0)

    key_text = Label(frame_select_body, textvariable=key, font=font, bg=color)
    key_text.place(relx=.5, rely=.4, anchor='center')

    text = Label(frame_select_body, text='Pressione o novo\nbotão de ativação.')
    text.place(relx=.5, rely=.7, anchor='center')

    screen_select.focus_set()
    screen_select.bind("<KeyPress>", lambda event: on_key_press(event, key, Label))


def settingsWindow(window=None, tk=None):
    global config_window

    # Cria uma nova janela para configurações
    config_window = tk.Toplevel(window)
    config_window.title("Configurações")
    config_window.geometry("300x220")

    config_window.resizable(False, False)
    icone = tk.PhotoImage(file="./assets/mouse.png")
    config_window.iconphoto(False, icone)

    # Adiciona um rótulo e um campo de entrada
    global interval
    interval = StringVar(value=load("interval"))

    global clicks
    clicks = StringVar(value=load("clicks"))

    style = ttk.Style()
    style.configure("Custom.TEntry",
                    foreground="black",
                    background=color,
                    font=("Helvetica", 14))

    style.map("Custom.TEntry",
              fieldbackground=[('active', color), ('!disabled', 'black')],
              background=[('active', color), ('!disabled', 'black')],
              bordercolor=[('focus', color), ('!focus', color)])

    label_interval = ttk.Label(config_window, text="Intervalo entre cliques (em milissegundos):")
    label_interval.pack(pady=1)
    entry_interval = ttk.Entry(config_window, width=30, textvariable=interval, style="Custom.TEntry")
    entry_interval.pack(pady=1)

    label_clicks = ttk.Label(config_window, text="Quantidade de clicks seguidos:")
    label_clicks.pack(pady=1)
    entry_clicks = ttk.Entry(config_window, width=30, textvariable=clicks, style="Custom.TEntry")
    entry_clicks.pack(pady=1)

    label_optionmenu = ttk.Label(config_window, text="Selecione o tipo de clique")
    label_optionmenu.pack(pady=1)

    load_button = load("button")

    if load_button == "left":
        load_button = "esquerdo"
    elif load_button == "right":
        load_button = "direito"

    options = [f"{load_button}", "esquerdo", "direito"]
    # Variável que armazenará a opção selecionada
    selected_option = StringVar()
    selected_option.set(options[0])  # Define a opção padrão
    # Criar a caixa de opções
    option_menu = ttk.OptionMenu(config_window, selected_option, *options)
    option_menu.config(width=26)
    option_menu.pack()

    # Adiciona um botão para salvar o valor
    def multiples(window, interval_value, clicks_value, selected_option):
        log1 = save(window, "interval", interval_value)
        log2 = save(window, "clicks", clicks_value)
        log3 = save(window, "button", selected_option)

        if log1 == True and log2 == True and log3 == True:
            messagebox.showinfo("Salvo.", "Todas as configurações foram salvas com sucesso!")
            window.destroy()

    save_button = tk.Button(config_window, text="Salvar", command=lambda: multiples(config_window, entry_interval, entry_clicks, selected_option))

    save_button.pack(pady=16)
    config_window.focus_set()