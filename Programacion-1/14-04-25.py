#A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el
#programa deberá determinar la posición del jugador en la cancha, considerando los
#siguientes parámetros:
#● Menos de 160 cm: Base
#● Entre 160 cm y 179 cm: Escolta
#● Entre 180 cm y 199 cm: Alero
#● 200 cm o más: Ala-Pívot o Pívot
#2. Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un
#mensaje según el valor:
#● 6, 7, 8, 9 y 10 ---> Promoción directa, la nota es ...
#● 4 y 5 ---> Aprobado, la nota es ...
#● 1, 2 y 3 ---> Desaprobado, la nota es ...


# EJERCICIO 1
altura = int(input("Ingresa tu altura: "))
if altura <= 159:
    print("Su posicion es: BASE")
elif altura >= 160 and altura <= 179:
    print("Su posicon es: ESCOLTA")
elif altura >= 180 and altura <= 199:
    print("Su posicon es: ALERO")
elif altura >= 200:
    print("Su posicion es: ALA-PIVOT")

# EJERCICIO 2 
nota = int(input("Ingresa tu nota: "))

if nota >= 6 and nota <= 10:
    print(f"Promocionaste, tu nota es: {nota}")
elif nota >= 4 and nota < 6:
    print(f"Aprobaste, tu nota es: {nota}")
elif nota >= 1 and nota < 4:
    print(f"Desaprobaste, tu nota es: {nota}")

