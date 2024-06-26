import openpyxl
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

# Declarar variables globales
x = 0
df = None
horas = []  # Declarar 'horas' como una lista global

# Función para cargar los datos desde el archivo Excel
def cargar_datos():
    global x
    global df
    global horas
    doc = openpyxl.load_workbook("Gasto.xlsx")
    hoja = doc["Hoja1"]

    Gasto = []
    Horas = []

    for row in hoja.iter_rows():
        d = row[0].value
        e = row[1].value
        Horas.append(d)
        Gasto.append(e)

    gasto = []
    horas = []
    x = len(Gasto)

    for y in range(1, x, 1):
        gasto.append(Gasto[y])
        horas.append(Horas[y])

    horas = sorted(horas)
    gasto = sorted(gasto)

    data = {'Horas': horas, 'Gasto': gasto}
    df = pd.DataFrame(data)

# Función para realizar la predicción y mostrar el resultado
def calcular_prediccion():
    global x
    global df
    global horas
    prediccion = int(entry_horas.get())

    if prediccion > 0:
        comparacion = int(entry_comparacion.get())
        ordenamiento = []
        ord_gasto = []

        for x in range(comparacion):
            a = 0
            a = prediccion - horas[x]
            a = abs(a)
            ordenamiento.append(a)

        ordenamiento = sorted(ordenamiento)
        y = len(ordenamiento)
        resultado = sum(ordenamiento) / y * 3

        result_label.config(text=f"El gasto por {prediccion} horas de uso es de: {resultado:.2f} pesos respecto al promedio de las comparaciones hechas")

        # Graficar
        plt.figure(figsize=(10, 6))
        plt.scatter(df['Horas'], df['Gasto'], label='Gasto vs Horas', color='blue')
        plt.plot([prediccion], [resultado], 'ro', label='Predicción', markersize=10, markeredgecolor='red')
        plt.xlabel('Horas de Uso')
        plt.ylabel('Gasto en Pesos')
        plt.title ('Gasto en función de las Horas de Uso')
        plt.legend()
        plt.grid(True)

        plt.show()

    else:
        result_label.config(text="Debe tener al menos una hora registrada")

# Crear una ventana
root = tk.Tk()
root.title("Predicción de Gasto de Energía")
root.geometry("800x600")  # Tamaño de la ventana
root.configure(bg='blue')  # Fondo azul

# Cargar datos desde el archivo Excel
cargar_datos()

# Crear etiquetas y campos de entrada
label_horas = ttk.Label(root, text="Horas de uso de luz en la semana:")
label_horas.pack(pady=10)
entry_horas = ttk.Entry(root)
entry_horas.pack()

label_comparacion = ttk.Label(root, text="Número de recibos cercanos para la comparación:")
label_comparacion.pack(pady=10)
entry_comparacion = ttk.Entry(root)
entry_comparacion.pack()

calcular_button = ttk.Button(root, text="Calcular Predicción", command=calcular_prediccion)
calcular_button.pack(pady=20)

result_label = ttk.Label(root, text="", foreground='white', background='blue')
result_label.pack()

root.mainloop()
