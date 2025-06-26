monto_productos = int(input("Ingrese el monto de los productos: "))
cantidad_productos = int(input("Ingrese la cantidad de los productos: "))
cliente = input("Eres VIP, REGULAR o EMPLEADO: ").lower()
print("\n")

descuento = 0
iva = 0.21

if cliente == "vip":
   if monto_productos >= 80000:
        descuento = 0.15
        if cantidad_productos >= 20:
            descuento += 0.05
elif cliente == "regular":
    if monto_productos >= 100000 or cantidad_productos >= 25:
        descuento = 0.10
elif cliente == "empleado":
    descuento = 0.20

if monto_productos <= 50000 and cantidad_productos >= 15:
    descuento = 0.05
 
descuento_agregado = monto_productos * descuento
monto_con_descuento = monto_productos - descuento_agregado

iva_agregado = monto_productos * iva
monto_total = monto_con_descuento + iva_agregado


print("El precio antes de los descuento es de: $", monto_productos)
print("El descuento es de: %", descuento)
print("El precio con descuento incluido es de: $", monto_con_descuento)
print("El iva es de: %", iva)
print("El precio final es de: $", monto_total)