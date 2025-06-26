#1
edad = int(input("Ingresa tu edad: "))

if edad == 18:
    print("Usted tiene 18 años")
elif edad != 18:
    print("Usted no tiene 18 años")
#2
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
   print("Mayor")
elif edad < 18:
    print("Menor")
#3
altura = float(input("Ingresa tu altura: "))

if altura >= 1.80:
    print("Usted es pivot")
elif altura <= 1.80:
    print("No es pivot")
#4
edad = int(input("Ingresa tu edad: "))
if edad >= 13 and edad <=17:
    print("Usted es adolecente")
else:
    print("Usted no es un adolecente")
#5
edad = int(input("Ingresa tu edad: "))

if edad <= 9:
    print("Usted es niño/a")
if edad >= 10 and edad <= 12:
    print("Usted es pre-adolecente")
if edad >= 13 and edad <=17:
    print("Usted es adolecente")
if edad >= 18:
    print("Usted es adulto")

