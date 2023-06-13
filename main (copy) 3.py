import tkinter as tk

def convert_temp():
    try:
        temp = float(entry.get())
        initial_unit = initial_var.get()
        final_unit = final_var.get()
        
        if initial_unit == "Kelvin":
            if final_unit == "Fahrenheit":
                result = (temp - 273.15) * 9/5 + 32
                output_label.config(text=f"{result:.2f} °F")
            elif final_unit == "Celsius":
                result = temp - 273.15
                output_label.config(text=f"{result:.2f} °C")
            else:
                output_label.config(text="Escolha uma unidade final.")
        elif initial_unit == "Celsius":
            if final_unit == "Fahrenheit":
                result = (temp * 9/5) + 32
                output_label.config(text=f"{result:.2f} °F")
            elif final_unit == "Kelvin":
                result = temp + 273.15
                output_label.config(text=f"{result:.2f} K")
            else:
                output_label.config(text="Escolha uma unidade final.")
        elif initial_unit == "Fahrenheit":
            if final_unit == "Celsius":
                result = (temp - 32) * 5/9
                output_label.config(text=f"{result:.2f} °C")
            elif final_unit == "Kelvin":
                result = (temp - 32) * 5/9 + 273.15
                output_label.config(text=f"{result:.2f} K")
            else:
                output_label.config(text="Escolha uma unidade final.")
        else:
            output_label.config(text="Escolha uma unidade inicial.")
    except ValueError:
        output_label.config(text="Digite um valor válido.")

root = tk.Tk()
root.title("Conversor de Temperaturas")

# entrada de dados
entry = tk.Entry(root, width=20)
entry.pack()

# opções para a unidade inicial da temperatura
initial_var = tk.StringVar()
initial_var.set("Celsius")

initial_frame = tk.LabelFrame(root, text="Unidade inicial:")
initial_frame.pack()

initial_radios = [
    ("Celsius", "Celsius"),
    ("Fahrenheit", "Fahrenheit"),
    ("Kelvin", "Kelvin")
]

for text, value in initial_radios:
    initial_radio = tk.Radiobutton(initial_frame, text=text, variable=initial_var, value=value)
    initial_radio.pack(anchor="w")

# opções para a unidade final da temperatura
final_var = tk.StringVar()
final_var.set("Fahrenheit")

final_frame = tk.LabelFrame(root, text="Unidade final:")
final_frame.pack()

final_radios = [
    ("Celsius", "Celsius"),
    ("Fahrenheit", "Fahrenheit"),
    ("Kelvin", "Kelvin")
]

for text, value in final_radios:
    final_radio = tk.Radiobutton(final_frame, text=text, variable=final_var, value=value)
    final_radio.pack(anchor="w")

# botão para iniciar a conversão
convert_button = tk.Button(root, text="Converter", command=convert_temp)
convert_button.pack()

# rótulo para exibir o resultado da conversão
output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()
