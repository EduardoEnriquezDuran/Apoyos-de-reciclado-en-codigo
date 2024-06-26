import tkinter as tk
from tkinter import messagebox
import requests
import json

def corregir_texto():
    texto = text_input.get("1.0", "end-1c")
    if not texto.strip():
        messagebox.showerror("Error", "Por favor, ingrese una oración.")
        return

    url = "https://api.languagetool.org/v2/check"
    data = {
        'text': texto,
        'language': 'es'
    }
    response = requests.post(url, data=data)
    result = response.json()

    matches = result.get('matches', [])
    texto_corregido = texto
    for match in reversed(matches):
        offset = match['offset']
        length = match['length']
        replacement = match['replacements'][0]['value'] if match['replacements'] else ''
        texto_corregido = texto_corregido[:offset] + replacement + texto_corregido[offset+length:]

    text_output.delete("1.0", "end")
    text_output.insert("1.0", texto_corregido)
    messagebox.showinfo("Corrección completa", "La oración ha sido corregida.")


root = tk.Tk()
root.title("Corrector Ortográfico")
root.geometry("1000x800")
root.configure(bg="blue")


label = tk.Label(root, text="Ingrese una oración:", bg="blue", fg="white", font=("Helvetica", 14))
label.pack(pady=10)


text_input = tk.Text(root, height=5, width=50, font=("Helvetica", 12))
text_input.pack(pady=10)


corregir_btn = tk.Button(root, text="Corregir", command=corregir_texto, font=("Helvetica", 12))
corregir_btn.pack(pady=10)


text_output = tk.Text(root, height=5, width=50, font=("Helvetica", 12))
text_output.pack(pady=10)

root.mainloop()
