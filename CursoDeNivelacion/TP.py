#Punto A

precio1 = int(input("Primer precio: "))
precio2 = int(input("Segundo precio: "))
precio3 = int(input("Tercer precio: "))

precio_total = precio1 + precio2 + precio3

print(f"La suma de los precios da un total de: {precio_total}")

#Punto B

precio1 = int(input("Primer precio: "))
precio2 = int(input("Segundo precio: "))
precio3 = int(input("Tercer precio: "))

precio_total = precio1 + precio2 + precio3
precio_total = precio_total / 3

print(f"El promedio de los precios es: {precio_total:.2f}") #el :.2f muestra solo 2 decimales

#Punto C

precio1 = int(input("Primer precio: "))
precio2 = int(input("Segundo precio: "))
precio3 = int(input("Tercer precio: "))
precio_total = precio1 + precio2 + precio3
iva = precio_total * 0.21
precio_con_iva = precio_total + iva

print(f"El precio es de: {precio_con_iva} con IVA incluido (IVA: {iva})")