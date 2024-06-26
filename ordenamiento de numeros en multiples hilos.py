import threading, time
i=1
numeros = []
def ordenamiento(numeros, clasificacion):
    if clasificacion == "mayor a menor":
        resultado = sorted(numeros)
        print("El ordenamiento de menor a mayor es:", resultado)
    elif clasificacion == "menor a mayor":
        resultado = sorted(numeros, reverse=True)
        print("El ordenamiento de mayor a menor es: ", resultado)



while i<11:
    solicitud = int(input("Ingrese el número: "))
    numeros.append(solicitud)

    t1 = threading.Thread(target=ordenamiento, args=(numeros, "mayor a menor"))
    t2 = threading.Thread(target=ordenamiento, args=(numeros, "menor a mayor"))

    t1.start()
    time.sleep(0.1)
    t2.start()
    time.sleep(0.1)
    i+=1
