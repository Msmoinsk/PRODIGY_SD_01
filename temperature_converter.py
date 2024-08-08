import tkinter as tk
from tkinter import ttk

def convert_temperature(value, input_scale):
    if input_scale == 'Celsius':
        return value, value * 1.8 + 32, value + 273.15
    elif input_scale == 'Fahrenheit':
        celsius = (value - 32) / 1.8
        return celsius, value, (celsius + 273.15)
    elif input_scale == 'Kelvin':
        celsius = value - 273.15
        return celsius, (celsius * 1.8 + 32), value
    else:
        return None, None, None

def on_convert():
    try:
        value = float(entry_value.get())
        input_scale = combo_input_scale.get()

        celsius, fahrenheit, kelvin = convert_temperature(value, input_scale)

        label_result.config(text=f"Celsius: {celsius:.2f} °C\nFahrenheit: {fahrenheit:.2f} °F\nKelvin: {kelvin:.2f} K")
        label_result.after(9000, reset_result)

    except ValueError:
        label_result.config(text="Oops! Please enter a valid number.", fg="red")

def reset_result():
    label_result.config(text="", fg="black")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x300")
root.configure(bg="#87CEEB")

# Configure grid weights for responsiveness
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(3, weight=1)

# Create and place the widgets
label_value = tk.Label(root, text="Enter Temperature Value:", bg="#87CEEB", font=("Comic Sans MS", 14))
label_value.grid(column=0, row=0, padx=10, pady=10, sticky='ew')

entry_value = tk.Entry(root, font=("Comic Sans MS", 14), width=10)
entry_value.grid(column=1, row=0, padx=10, pady=10, sticky='ew')

label_scale = tk.Label(root, text="Select Scale:", bg="#87CEEB", font=("Comic Sans MS", 14))
label_scale.grid(column=0, row=1, padx=10, pady=10, sticky='ew')

combo_input_scale = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], font=("Comic Sans MS", 14))
combo_input_scale.grid(column=1, row=1, padx=10, pady=10, sticky='ew')
combo_input_scale.set("Celsius")

button_convert = tk.Button(root, text="Convert!", command=on_convert, bg="#FF6347", fg="white", font=("Comic Sans MS", 14))
button_convert.grid(column=0, row=2, columnspan=2, padx=10, pady=10, sticky='ew')

label_result = tk.Label(root, text="", justify=tk.LEFT, bg="#87CEEB", font=("Comic Sans MS", 14))
label_result.grid(column=0, row=3, columnspan=2, padx=10, pady=10, sticky='ew')

# Add some padding around the window
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()