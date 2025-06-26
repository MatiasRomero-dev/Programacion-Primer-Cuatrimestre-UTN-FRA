print("MENU DE OPCIONES")
print("[1] Ventas")
print("[2] Soporte")
print("[3] Administracion")
opcion = int(input("elegir opcion:"))

match opcion:
    case 1:
        print("VENTAS")
    case 2:
        print("SOPORTE")
    case 3:
        print("ADMINISTRACION")
    case _: #Case comodin para evitar cualquier otra opcion
        print("Opcion inexistente")


#SIN EL MATCH-CASE
#if opcion == 1:
    #print("VENTAS")
#elif opcion == 2:
    #print("SOPORTE")
#elif opcion == 3:
    #print("ADMINISTRACION")