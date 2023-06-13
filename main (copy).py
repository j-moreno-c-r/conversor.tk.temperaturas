import tkinter as tk


def conversor(inicial,valor, convertido):
    f = "Fahrenheit"
    c = "Celsius"
    k = "Kelvin"
    if inicial == c and convertido == f:
        resultado = valor * 9 / 5 + 32
    if inicial == f and convertido == c:
        resultado = (valor - 32) * 5 / 9
    if inicial == c and convertido == k:
        resultado = valor + 273, 15
    if inicial == k and convertido == c:
        resultado = valor - 273, 15

    print(resultado)


janela = tk.Tk()
janela.title("Conversor de escalas  termométricas ")
janela.geometry("300x300")

nome = tk.Label(text="escolha a escala inicial")
nome.pack()

label3 = tk.Label(janela, text="")
label3.pack()

label4 = tk.Label(janela, text="escala inicial")
label4.pack(anchor=tk.W)

v = tk.StringVar()

rd1 = tk.Radiobutton(janela, text="Fahrenheit", variable=v, value="Fahrenheit")
rd1.pack(anchor=tk.W)

rd2 = tk.Radiobutton(janela, text="Celsius", variable=v, value="Celsius")
rd2.pack(anchor=tk.W)

rd3 = tk.Radiobutton(janela, text="Kelvin", variable=v, value="Kelvin")
rd3.pack(anchor=tk.W)


def acaobotao3():
    escala_inicial = (v.get())


botao3 = tk.Button(janela, text="OK", command=acaobotao3)
botao3.pack()



nome = tk.Label(text="Coloque o valor")
nome.pack()


label2 = tk.Label(janela, text="")
label2.pack()

entry1 = tk.Entry(janela)
entry1.pack()


def acaobotao2():
    valor = ['text']


botao2 = tk.Button(janela, text="Aqui!", command=acaobotao2)
botao2.pack()


label4 = tk.Label(janela, text="escala a converter")
label4.pack(anchor=tk.W)

v = tk.StringVar()

rd1 = tk.Radiobutton(janela, text="Fahrenheit", variable=v, value="Fahrenheit")
rd1.pack(anchor=tk.W)

rd2 = tk.Radiobutton(janela, text="Celsius", variable=v, value="Celsius")
rd2.pack(anchor=tk.W)

rd3 = tk.Radiobutton(janela, text="Kelvin", variable=v, value="Kelvin")
rd3.pack(anchor=tk.W)


def acaobotao3():
    escala_pedida = (v.get())


botao3 = tk.Button(janela, text="OK", command=acaobotao3)
botao3.pack()




def acaobutton():
    global escala_inicial,escala_pedida,valor
    conversor(escala_inicial,valor,escala_pedida)
    
button = tk.Button(text="Conversão", command=acaobutton)
button.pack()

tk.mainloop()
