import tkinter as tk
from tkinter import messagebox
import enchant

class CorreccionOrtograficaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Corrección Ortográfica")
        
        self.label = tk.Label(root, text="Ingrese una oración:")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=5)
        
        self.button = tk.Button(root, text="Corregir", command=self.corregir)
        self.button.pack(pady=10)
        
    def corregir(self):
        oracion = self.entry.get()
        oracion_corregida = self.corregir_oracion(oracion)
        messagebox.showinfo("Oración corregida", f"Oración original:\n{oracion}\n\nOración corregida:\n{oracion_corregida}")
        
    def corregir_oracion(self, oracion):
        # Especificamos la ruta del diccionario de Enchant
        d = enchant.DictWithPWL("es_ES", "enchant_dicts/es_ES.dic")  # Cambia "enchant_dicts/es_ES.dic" por la ruta correcta en tu sistema
        
        # Dividimos la oración en palabras
        palabras = oracion.split()
        
        # Corregimos cada palabra si es necesario
        palabras_corregidas = []
        for palabra in palabras:
            if not d.check(palabra):
                sugerencias = d.suggest(palabra)
                if sugerencias:
                    palabra_corregida = sugerencias[0]  # Tomamos la primera sugerencia
                else:
                    palabra_corregida = palabra  # Si no hay sugerencias, dejamos la palabra como está
            else:
                palabra_corregida = palabra  # La palabra está correcta
            palabras_corregidas.append(palabra_corregida)
        
        # Reconstruimos la oración corregida
        oracion_corregida = ' '.join(palabras_corregidas)
        
        return oracion_corregida

if __name__ == "__main__":
    root = tk.Tk()
    app = CorreccionOrtograficaApp(root)
    root.mainloop()
