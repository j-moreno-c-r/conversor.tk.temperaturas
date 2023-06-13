#chat gpt
import tkinter as tk

def convert_temp():
    try:
        temp = float(entry.get())
        if var.get() == 1:
            result = (temp - 273.15) * 9/5 + 32
            output_label.config(text=f"{result:.2f} °F")
        elif var.get() == 2:
            result = (temp * 9/5) + 32
            output_label.config(text=f"{result:.2f} °F")
        elif var.get() == 3:
            result = temp + 273.15
            output_label.config(text=f"{result:.2f} K")
        elif var.get() == 4:
            result = (temp - 32) * 5/9
            output_label.config(text=f"{result:.2f} °C")
        elif var.get() == 5:
            result = (temp - 32) * 5/9 + 273.15
            output_label.config(text=f"{result:.2f} K")
        elif var.get() == 6:
            result = (temp - 273.15)
            output_label.config(text=f"{result:.2f} °C")
    except ValueError:
        output_label.config(text="Digite um valor válido.")

root = tk.Tk()
root.title("Conversor de Temperaturas")

# entrada de dados
entry = tk.Entry(root, width=20)
entry.pack()

# botões de opção para escolher as unidades de temperatura
var = tk.IntVar()
kelvin_to_fahrenheit = tk.Radiobutton(root, text="Kelvin para Fahrenheit", variable=var, value=1)
kelvin_to_fahrenheit.pack()
celsius_to_fahrenheit = tk.Radiobutton(root, text="Celsius para Fahrenheit", variable=var, value=2)
celsius_to_fahrenheit.pack()
celsius_to_kelvin = tk.Radiobutton(root, text="Celsius para Kelvin", variable=var, value=3)
celsius_to_kelvin.pack()
fahrenheit_to_celsius = tk.Radiobutton(root, text="Fahrenheit para Celsius", variable=var, value=4)
fahrenheit_to_celsius.pack()
fahrenheit_to_kelvin = tk.Radiobutton(root, text="Fahrenheit para Kelvin", variable=var, value=5)
fahrenheit_to_kelvin.pack()
kelvin_to_celsius = tk.Radiobutton(root, text="Kelvin para Celsius", variable=var, value=6)
kelvin_to_celsius.pack()

# botão para iniciar a conversão
convert_button = tk.Button(root, text="Converter", command=convert_temp)
convert_button.pack()

# rótulo para exibir o resultado da conversão
output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()
