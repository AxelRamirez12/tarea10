import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Función para realizar la conversión de unidades
def convertir():
    try:
        valor = float(entry_valor.get())
        unidad_entrada = combo_unidad_entrada.get()
        unidad_salida = combo_unidad_salida.get()
        
        # Lógica de conversión  
        resultado = valor  # Por defecto, si las unidades son las mismas, el resultado es el mismo valor
        if unidad_entrada == unidad_salida:
            resultado = valor
        elif unidad_entrada == "m" and unidad_salida == "cm":
            resultado = valor * 100
        elif unidad_entrada == "cm" and unidad_salida == "m":
            resultado = valor / 100

        elif unidad_entrada == "kg" and unidad_salida == "lb":
            resultado = valor * 2.205
        elif unidad_entrada == "lb" and unidad_salida == "kg":
            resultado = valor / 2.205

        elif unidad_entrada == "kg" and unidad_salida == "g":
            resultado = valor * 1000
        elif unidad_entrada == "g" and unidad_salida == "kg":
            resultado = valor / 1000

        else:
            raise ValueError("No se puede realizar la conversion")

        # Agregar más conversiones según sea necesario
        
        # Mostrar el resultado
        label_resultado.config(text=f"Resultado: {resultado} {unidad_salida}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido.")

# Función para guardar el resultado en un archivo de texto
def guardar_resultado():
    try:
        resultado_texto = label_resultado.cget("text")
        with open("resultado.txt", "w") as archivo:
            archivo.write(resultado_texto)
        messagebox.showinfo("Guardado", "El resultado se ha guardado correctamente en 'resultado.txt'.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar el resultado: {e}")

# Crear la ventana principal
root = tk.Tk()
root.title("Convertidor de Unidades")

# Crear y posicionar los widgets
label_valor = ttk.Label(root, text="Valor:")
label_valor.grid(row=0, column=0, padx=5, pady=5)

entry_valor = ttk.Entry(root)
entry_valor.grid(row=0, column=1, padx=5, pady=5)

label_unidad_entrada = ttk.Label(root, text="Unidad de entrada:")
label_unidad_entrada.grid(row=1, column=0, padx=5, pady=5)

combo_unidad_entrada = ttk.Combobox(root, values=["m", "cm", "kg", "g", "lb",])
combo_unidad_entrada.grid(row=1, column=1, padx=5, pady=5)
combo_unidad_entrada.current(0)

label_unidad_salida = ttk.Label(root, text="Unidad de salida:")
label_unidad_salida.grid(row=2, column=0, padx=5, pady=5)

combo_unidad_salida = ttk.Combobox(root, values=["m", "cm", "kg", "g", "lb",])
combo_unidad_salida.grid(row=2, column=1, padx=5, pady=5)
combo_unidad_salida.current(1)

btn_convertir = ttk.Button(root, text="Convertir", command=convertir)
btn_convertir.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

label_resultado = ttk.Label(root, text="Resultado:")
label_resultado.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

btn_guardar = ttk.Button(root, text="Guardar resultado", command=guardar_resultado)
btn_guardar.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="WE")

# Ejecutar el bucle principal
root.mainloop()