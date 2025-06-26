#1
suma_pares = 0
for i in range(2, 11, 2):
    suma_pares += i
print("Suma de los números pares entre 1 y 10:", suma_pares)
#2
contraseña = ""
while contraseña != "utn750":
    contraseña = input("Ingrese la contraseña: ")
print("Contraseña correcta.")
#3
numero = -1
while numero < 0 or numero > 9:
    numero = int(input("Ingrese un número entre 0 y 9: "))
print("Número válido.")
#4
letra = ""
while not (letra == "U" or letra == "T" or letra == "N"):
    letra = input("Ingrese una letra (U, T o N): ")
print("Letra válida.")
#5
suma = 0
for i in range(5):
    num = float(input(f"Ingrese el número {i+1}: "))
    suma += num
promedio = suma / 5
print("Suma acumulada:", suma)
print("Promedio:", promedio)
