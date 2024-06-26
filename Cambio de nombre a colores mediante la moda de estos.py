import openpyxl


doc = openpyxl.load_workbook("faltantes.xlsx")
hoja = doc["Hoja1"]

posicion=[]
color=[]
for row in hoja.iter_rows():
    d=row[0].value
    e=row[1].value
    posicion.append(d)
    color.append(e)
print (posicion)
print(color)

colores=len(color)
conteo_rojo=0
conteo_azul=0
conteo_amarillo=0
conteo_verde=0
for a in range (colores):
    if color[a]=="rojo":
        conteo_rojo=conteo_rojo+1
    elif color[a]=="azul":
        conteo_azul=conteo_azul+1
    elif color[a]=="amarillo":
        conteo_amarillo=conteo_amarillo+1
    elif color[a]=="verde":
        conteo_verde=conteo_verde+1
clasificacion=[]
clasificacion.append(conteo_rojo)
clasificacion.append(conteo_azul)
clasificacion.append(conteo_amarillo)
clasificacion.append(conteo_verde)
clasificacion=sorted(clasificacion)
for b in range(colores):
    if color[b] is None:
        color[b]=("rojo")

print(color)

        
