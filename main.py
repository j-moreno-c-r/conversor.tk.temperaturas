import tkinter as tk

def conversor(inicial, valor, convertido):
    f = "Fahrenheit"
    c = "Celsius"
    k = "Kelvin"
    resultado = valor

    if inicial == c and convertido == f:
        resultado = valor * 9 / 5 + 32
    elif inicial == f and convertido == c:
        resultado = (valor - 32) * 5 / 9
    elif inicial == c and convertido == k:
        resultado = valor + 273.15
    elif inicial == k and convertido == c:
        resultado = valor - 273.15
    elif inicial == f and convertido == k:
        resultado = (valor - 32) * 5 / 9 + 273.15
    elif inicial == k and convertido == f:
        resultado = (valor - 273.15) * 9 / 5 + 32

    return resultado

def converter_temperatura():
    valor_inicial = float(entry_valor_inicial.get())
    inicial = opcoes_inicial.get()
    convertido = opcoes_convertido.get()

    resultado = conversor(inicial, valor_inicial, convertido)

    label_resultado["text"] = f"{resultado:.2f}"
    label_resultado["fg"] = "red"

root = tk.Tk()
root.geometry("300x300")
root.config(bg="#a5ffa5")

opcoes_temperatura = [ "Celsius", "Fahrenheit", "Kelvin" ]

opcoes_inicial = tk.StringVar(value=opcoes_temperatura[0])
opcoes_convertido = tk.StringVar(value=opcoes_temperatura[0])

entry_valor_inicial = tk.Entry(root, font=("Arial", 14))
entry_valor_inicial.pack(pady=10)

frame_opcoes = tk.Frame(root, bg="#a5ffa5")
frame_opcoes.pack(pady=5)

label_inicial = tk.Label(frame_opcoes, text="De:", font=("Arial", 14), bg="#a5ffa5")
label_inicial.pack(side=tk.LEFT)

opcoes_bolinhas_inicial = []
for opcao in opcoes_temperatura:
    opcao_bolinha = tk.Radiobutton(frame_opcoes, text=opcao, variable=opcoes_inicial, value=opcao, font=("Arial", 12), bg="#a5ffa5")
    opcao_bolinha.pack(side=tk.LEFT, padx=5)
    opcoes_bolinhas_inicial.append(opcao_bolinha)

label_convertido = tk.Label(frame_opcoes, text="Para:", font=("Arial", 14), bg="#a5ffa5")
label_convertido.pack(side=tk.LEFT)

opcoes_bolinhas_convertido = []
for opcao in opcoes_temperatura:
    opcao_bolinha = tk.Radiobutton(frame_opcoes, text=opcao, variable=opcoes_convertido, value=opcao, font=("Arial", 12), bg="#a5ffa5")
    opcao_bolinha.pack(side=tk.LEFT, padx=5)
    opcoes_bolinhas_convertido.append(opcao_bolinha)

botao_converter = tk.Button(root, text="Converter", command=converter_temperatura, font=("Arial", 14))
botao_converter.pack(pady=10)

label_resultado = tk.Label(root, font=("Arial", 24), bg="#a5ffa5")
label_resultado.pack()

root.mainloop()
