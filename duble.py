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

    return resultado

class ConversorTemp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.valor_inicial = tk.Entry(self)
        self.valor_inicial.pack(side="left")

        self.unidade_inicial = tk.StringVar(self)
        self.unidade_inicial.set("Celsius")
        self.menu_inicial = tk.OptionMenu(self, self.unidade_inicial, "Celsius", "Fahrenheit", "Kelvin")
        self.menu_inicial.pack(side="left")

        self.botao_converter = tk.Button(self)
        self.botao_converter["text"] = "->"
        self.botao_converter["command"] = self.converter_temperatura
        self.botao_converter.pack(side="left")

        self.valor_convertido = tk.Label(self)
        self.valor_convertido.pack(side="left")

        self.unidade_convertida = tk.StringVar(self)
        self.unidade_convertida.set("Fahrenheit")
        self.menu_convertido = tk.OptionMenu(self, self.unidade_convertida, "Celsius", "Fahrenheit", "Kelvin")
        self.menu_convertido.pack(side="left")

    def converter_temperatura(self):
        valor = float(self.valor_inicial.get())
        inicial = self.unidade_inicial.get()
        convertido = self.unidade_convertida.get()
        resultado = conversor(inicial, valor, convertido)
        self.valor_convertido.configure(text=resultado)

root = tk.Tk()
app = ConversorTemp(master=root)
app.mainloop()
