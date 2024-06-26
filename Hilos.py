import openpyxl, threading, time

doc = openpyxl.load_workbook("Agua_Calidad.xlsx")
hoja = doc["Hoja1"]
Estados = []
poblacion = []
eficiencia = []
norma = []
i=0
for row in hoja.iter_rows(min_row=2):
    a = row[0].value
    b = row[1].value
    c = row[2].value
    d = row[3].value
    Estados.append(a)
    poblacion.append(b)
    eficiencia.append(c)
    norma.append(d)

n = len(poblacion)


def solicitud(i):
    if i ==1:
        solicitudes = input("Ingrese el estado que desea BUSCAR: ")
        solicitudes = solicitudes.upper()
        Poblacion_total = 0
        promedio_eficiencia=0
        promedio_norma=0
        conteo=0
        for e in range(n):
            if solicitudes == Estados[e]:
                Poblacion_total += poblacion[e]
                conteo+=1
                promedio_eficiencia+=eficiencia[e]
                promedio_eficiencia/=conteo
        Peticion=input("ingrese que decea saber recuerde que hay poblacion y promedio de eficiencia: ")
        Peticion=Peticion.upper()
        if Peticion=="POBLACION":
            print("La poblacion total de ", solicitudes, "es: ",Poblacion_total)
        if Peticion=="PROMEDIO DE EFICIENCIA":
            print(" El promedio de la eficiencia en el estado de ", Peticion, "es: ", (promedio_eficiencia*10))
t1 = threading.Thread(target=solicitud, args=(1,))
t1.start()
time.sleep(0.1)



