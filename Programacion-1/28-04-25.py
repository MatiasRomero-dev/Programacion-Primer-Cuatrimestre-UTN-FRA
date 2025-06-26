#1 Mostrar 10 repeticiones de números ascendentes desde el 1 al 10. (for)
numeros = [1,2,3,4,5,6,7,8,9,10]
for repeticion in range(10):
    for numeros in range(1,11):
        print(numeros)
print("FIN")

#2 Mostrar 10 repeticiones de números descendentes desde el 10 al 1. (for)
numeros = [1,2,3,4,5,6,7,8,9,10]
for repeticion in range(10):
    for numeros in range(10,0, -1):
        print(numeros)
print("FIN")

#3 Mostrar la suma de los números desde el 1 hasta el 10. (for , acumulador)
acumulador = 0
for numero in range(1,11):
    acumulador += numero
    print(acumulador)
 
#4 Mostrar la suma de los números pares desde el 1 hasta el 10. (for, acumulador, 2)
acumulador = 0
for numero in range(2,11,2):
    acumulador += numero
    print(acumulador)

#5 Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. 
# Mostrar la suma y el promedio por pantalla.(for, acumulador y contador(opcional), promedio).
#(for, acumulador y contador(opcional), promedio)
acumulador = 0
for i in range(5):
    numeros = int(input("Ingrese un numero (LIMITE 5): "))
    print(f"Su numero es {numeros}, ingrese el siguiente: ")
    acumulador += numeros
print(f"La suma de sus numeros es {acumulador}")
promedio = acumulador / 5
print(f"Tu promedio es {promedio:.2f}")

# 6 Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). 
# Calcular la suma de los números ingresados y el promedio de los mismos.
#(while, acumulador y contador, promedio)
acumulador = 0
contador = 0
print("\nIngrese FIN para salir")
while True:
    numero = input("Ingrese su numero: ")
    if numero == "FIN":
        break
    try:
        numero_int = int(numero)
        acumulador += numero_int
        contador += 1
        print(f"La suma de todos sus numeros hasta ahora es de {acumulador:.2f}")
        promedio = acumulador / contador
        print(f"El promedio de todos sus numeros hasta ahora es de {promedio:.2f}")
        print(f"Puede seguir insertando numeros o poner FIN para salir")
    except ValueError:
        print("Ingrese un numero valido o FIN para salir")

#7 Solicitar al usuario que ingrese números (hasta que no quiera ingresar más).
# Calcular la suma de los números positivos y el producto de los negativos.
# (while, acumulador += acumulador *=)
acumulador_positivo = 0
acumulador_negativo = 1 #arreglar sacar TRY EXCEPT
print("\nIngrese FIN para salir")
while True:
    numero = input("Ingrese su numero: ")
    if numero == "FIN":
        break
    try:
        numero_int = int(numero)
        if numero_int >= 0:
            acumulador_positivo += numero_int
            print(f"La suma de todos sus numeros positivos hasta ahora es de {acumulador_positivo:.2f}")
        else:
            acumulador_negativo *= numero_int
            print(f"El producto de todos sus numeros negativos hasta ahora es de {acumulador_negativo:.2f}")
    except ValueError:
        print("Ingrese un numero valido o FIN para salir")

#8 Ingresar 10 números enteros. Determinar el máximo y el mínimo.(for, max , mix )
max = float("-inf")
min = float("inf")

for i in range(1,11):
    i = int(input("Ingrese su numero: "))
    if i > max:
        max = i
    if i < min:
        min = i
    print(f"El numero minimo es {min}.\nEl numero maximo es {max}")










