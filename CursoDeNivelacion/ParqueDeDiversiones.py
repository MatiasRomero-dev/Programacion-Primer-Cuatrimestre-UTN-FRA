print("50$ la entrada!")
entradas = (int(input("Cuantas entradas desea comprar?: ")))
cliente = (input("Usted es Socio vip, regular o general?: ")).lower()
descuento = 0
impuesto = 0
precio_x_entrada = 50

if entradas >= 6:
    print("Recibira un descuento del 50% por comprar 6 o mas entradas")
    precio_x_entrada = precio_x_entrada * entradas
    descuento = 0.50
elif entradas == 5 and cliente == "vip":
    print("usted compro 5 entradas y es "+ cliente + " por ende recibira 40% de descuento")
    precio_x_entrada = precio_x_entrada * 5
    descuento = 0.40
elif entradas == 5 and cliente != "vip":
    print("usted compro 5 entradas y es "+ cliente + " por ende recibira 30% de descuento")
    precio_x_entrada = precio_x_entrada * 5
    descuento = 0.30
elif entradas == 4 and cliente == "vip" or cliente == "regular":
    print("usted compro 4 entradas y es "+ cliente + " por ende recibira 25% de descuento")
    precio_x_entrada = precio_x_entrada * 4
    descuento = 0.25
elif entradas == 4 and cliente == "general":
    print("usted compro 4 entradas y es "+ cliente + " por ende recibira 20% de descuento")
    precio_x_entrada = precio_x_entrada * 4
    descuento = 0.20
elif entradas == 3 and cliente == "vip":
    print("usted compro 3 entradas y es "+ cliente + " por ende recibira 15% de descuento")
    precio_x_entrada = precio_x_entrada * 3
    descuento = 0.15
elif entradas == 3 and cliente == "regular":
    print("usted compro 3 entradas y es "+ cliente + " por ende recibira 10% de descuento")
    precio_x_entrada = precio_x_entrada * 3
    descuento = 0.10
elif entradas == 3 and cliente == "general":
    print("usted compro 3 entradas y es "+ cliente + " por ende recibira 5% de descuento")
    precio_x_entrada = precio_x_entrada * 3
    descuento = 0.05
elif entradas == 2:
    print("usted compro 2 entradas, recibira 5% de descuento")
    precio_x_entrada = precio_x_entrada * 2
    descuento = 0.05
elif entradas == 1:
    print("usted compro 2 entradas, no recibe descuento")
    precio_x_entrada = precio_x_entrada * 1

if precio_x_entrada > 180:
    print("El precio paso de 180$ se agrega 10% de impuestos")
    impuesto = 0.10

descuento_agregado = precio_x_entrada * descuento
precio_con_descuento = precio_x_entrada - descuento_agregado
impuesto_agregado = precio_x_entrada * impuesto
precio_con_impuesto = precio_con_descuento + impuesto_agregado

print("Precio sin descuentos: $",precio_x_entrada)
print("Descuento agregado: %",descuento)
print("Precio con descuentos: $",precio_con_descuento)
print("impuesto agregado: %",impuesto)
print("precio con impuesto agregado: $",precio_con_impuesto)
