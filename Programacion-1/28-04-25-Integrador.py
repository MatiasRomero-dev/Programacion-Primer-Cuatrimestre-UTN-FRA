#Realizar un programa que permita que el usuario ingrese todos los números que desee.
#Una vez finalizada la carga determinar: (while)
#La suma acumulada de los números negativos.
#La suma acumulada de los números positivos.
#La cantidad de números negativos ingresados.
#El promedio de los números positivos.
#El número positivo más grande.
#El porcentaje de números negativos ingresados, respecto del total de ingresos.
acumulador_positivo = 0
acumulador_negativo = 0
contador_negativo = 0
contador_positivo = 0
max = float("-inf")
print("\nIngrese FIN para salir")
while True:
    numero = input("Ingrese su numero: ")
    if numero.upper() == "FIN":
        break
    try:
        numero_int = int(numero)
        if numero_int >= 0:
            acumulador_positivo += numero_int
            print(f"La suma de todos sus numeros positivos hasta ahora es de {acumulador_positivo:.2f}")
            contador_positivo += 1
            promedio = acumulador_positivo / contador_positivo
            print(f"El promedio de la suma de sus numeros positivos hasta el momento es de {promedio:.2f}")
            if numero_int > max:
                max = numero_int
            print(f"El numero positivo mas grande hasta ahora es {max}")
        else:
            acumulador_negativo += numero_int
            contador_negativo += 1
            print(f"La suma de todos sus numeros negativos hasta ahora es de {acumulador_negativo:.2f}")
            print(f"hasta ahora la cantidad de numeros negativos ingresados es de {contador_negativo}")
        total_numeros = contador_positivo + contador_negativo
        porcentaje =  (contador_negativo / total_numeros) * 100
        print(f"El porcentaje de numeros negativos hasta el momento es de {porcentaje:.2f}")

    except ValueError:
        print("Ingrese un numero valido o FIN para salir")
