edad = int(input("Ingrese su edad: "))

if edad < 0 or edad > 120:
    print("Edad invalida")    
elif edad < 13:
    print("Acceso denegado")
elif edad <= 17:
    print("Acceso restringido. Estas en modo adolescente")
else:
    print("Acceso completo concedido")
 
#EJERCICIO AGUA POTABLE (GOTITA S.A.)


print("\nTarifa de Agua potable Gotita S.A. \n \n -Todas las facturas incluyen un cargo fijo de $7000 además del costo por consumo. \n -El costo por metro cúbico (m³) de agua es de $200/m³. \n -se aplica el IVA del 21% sobre el precio total a pagar!. \n")

metros = int(input("Bienvenido, Porfavor ingrese los metros cubicos consumidos: "))
cliente = input("\nUsted es un cliente tipo RESIDENCIAL, COMERCIAL o INDUSTRIAL?: ").lower()

costo_x_metro = 200
cargo_fijo = 7000
iva = 0.21
descuento = 0
recargo = 0
subtotal = costo_x_metro * metros

print(f"\nBienvenido sea cliente {cliente}")
print(f"El costo de sus metros consumidos es de: ${subtotal}")

if cliente == "residencial":

    if metros < 30:
        descuento = subtotal * 0.10
        subtotal_con_descuento = subtotal - descuento
        print(f"\nSe aplico una bonificacion del 10% asi que quedaria en: ${subtotal_con_descuento}")

    elif metros > 80:
        recargo = subtotal * 0.15
        subtotal_con_recargo = subtotal - recargo
        print(f"\nSe aplico un recargo del 15% asi que quedaria en: ${subtotal_con_recargo}")

    elif subtotal < 35000:
        descuento = subtotal * 0.05
        subtotal_con_descuento = (subtotal + cargo_fijo) - descuento
        print(f"\nSe aplico un descuento del 5% asi que quedaria en: ${subtotal_con_descuento}")

elif cliente == "comercial":

    if metros < 50:
        recargo = subtotal * 0.05
        subtotal_con_recargo = subtotal - recargo
        print(f"\nSe aplico un recargo del 5% por caso especial asi que quedaria en: ${subtotal_con_recargo}")

    elif metros > 300:
        descuento = subtotal * 0.12
        subtotal_con_descuento = (subtotal + cargo_fijo) - descuento
        print(f"\nSe aplico una bonificacion del 12% asi que quedaria en: ${subtotal_con_descuento}")

    else:
        descuento = subtotal * 0.08
        subtotal_con_descuento = (subtotal + cargo_fijo) - descuento
        print(f"\nSe aplico una bonificacion del 8% asi que quedaria en: ${subtotal_con_descuento}")

elif cliente == "industrial":

    if metros < 200:
        recargo = subtotal * 0.10
        subtotal_con_recargo = subtotal - recargo
        print(f"\nSe aplico un recargo del 10% asi que quedaria en: ${subtotal_con_recargo}")

    elif metros > 500:
        descuento = subtotal * 0.20
        subtotal_con_descuento = (subtotal + cargo_fijo) - descuento
        print(f"\nSe aplico una bonificacion del 20% asi que quedaria en: ${subtotal_con_descuento}")

    elif metros > 1000:
        descuento = subtotal * 0.30
        subtotal_con_descuento = (subtotal + cargo_fijo) - descuento
        print(f"\nSe aplico una bonificacion del 30% asi que quedaria en: ${subtotal_con_descuento}")

iva_agregado = subtotal * iva
subtotal_con_iva = subtotal + iva_agregado
total = subtotal_con_iva + cargo_fijo

print(f"\nSu subtotal con IVA (21%) agregado seria: ${subtotal_con_iva}")
print(f"\nSu total a pagar con el cargo fijo seria de: ${total:.2f}")
