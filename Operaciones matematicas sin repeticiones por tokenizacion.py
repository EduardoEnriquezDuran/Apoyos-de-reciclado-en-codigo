print("Programa que analiza tus solicitudes matemáticas sin repetición de la operación")

conteo_suma = 0
conteo_resta = 0
conteo_multiplicacion = 0
conteo_division = 0

for _ in range(4):
    solicitud = input("Ingrese la operación que desea realizar (sin espacios, p. ej., 2+2): ")
    print("Por favor, usa +, -, *, / para las operaciones")
    
    if '+' in solicitud:
        conteo_suma += 1
        if conteo_suma > 1:
            print("Has repetido la operación de suma. Por favor, reinicia el programa.")
            break
        numeros = solicitud.split('+')
        resultado = int(numeros[0]) + int(numeros[1])
        print(f"Resultado: {solicitud} = {resultado}")
    
    elif '-' in solicitud:
        conteo_resta += 1
        if conteo_resta > 1:
            print("Has repetido la operación de resta. Por favor, reinicia el programa.")
            break
        numeros = solicitud.split('-')
        resultado = int(numeros[0]) - int(numeros[1])
        print(f"Resultado: {solicitud} = {resultado}")
    
    elif '*' in solicitud:
        conteo_multiplicacion += 1
        if conteo_multiplicacion > 1:
            print("Has repetido la operación de multiplicación. Por favor, reinicia el programa.")
            break
        numeros = solicitud.split('*')
        resultado = int(numeros[0]) * int(numeros[1])
        print(f"Resultado: {solicitud} = {resultado}")
    
    elif '/' in solicitud:
        conteo_division += 1
        if conteo_division > 1:
            print("Has repetido la operación de división. Por favor, reinicia el programa.")
            break
        numeros = solicitud.split('/')
        if int(numeros[1]) == 0:
            print("Error: División por cero.")
        else:
            resultado = int(numeros[0]) / int(numeros[1])
            print(f"Resultado: {solicitud} = {resultado}")
    
    else:
        print("La operación no ha sido detectada. Por favor, usa +, -, *, /.")
