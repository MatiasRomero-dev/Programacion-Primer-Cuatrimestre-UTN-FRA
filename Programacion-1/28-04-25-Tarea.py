# 1 Solicitar al usuario que ingrese como mínimo 5 números. 
# Calcular la suma de los números ingresados y el promedio de los mismos.
# (while, acumulador, contador, promedio)
acumulador = 0
contador = 0
print("Binvenido si desea salir ingrese FIN")
while True:
    numero = input("Por favor ingrese sus numeros (Minimo 5): ")
    if numero.lower() == "fin":
        break
    try:
        numero_int = int(numero)
        acumulador += numero_int
        contador += 1
    except ValueError:
        print("Numero Invalido, Por favor inserte un numero valido o Fin")
if contador < 5:
    print("Usted salio de la cuenta por insuficientes numeros")
else:
    promedio = acumulador / contador
    print(f"La suma de sus numeros es {acumulador}")
    print(f"El promedio de sus numeros es {promedio:.2f}")

# 2 Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10.
# Calcular la suma de los números ingresados y el promedio de los mismos.
# (for y while, acumulador, contador, promedio)
while True:
    acumulador = 0
    contador = 0
    print("Binvenido si desea salir ingrese FIN")

    for i in range(10):
        numero = input("Por favor ingrese sus numeros (Minimo 5 y Maximo 10): ")
        if numero.lower() == "fin":
            break
        try:
            numero_int = int(numero)
            acumulador += numero_int
            contador += 1
        except ValueError:
            print("Numero Invalido, Por favor inserte un numero valido o Fin")
    if contador < 5 or contador > 10:
        print("Usted salio de la cuenta por insuficientes/demasiados numeros")
    else:
        promedio = acumulador / contador
        print(f"La suma de sus numeros es {acumulador}")
        print(f"El promedio de sus numeros es {promedio:.2f}")