edad = int(input("Ingrese su edad: "))

if edad < 0 or edad > 120:
    print("Edad invalida")    
elif edad < 13:
    print("Acceso denegado")
elif edad <= 17:
    print("Acceso restringido. Estas en modo adolescente")
else:
    print("Acceso completo concedido")
 
