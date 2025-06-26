nombre_de_usuario = input("ingresa tu nombre: ")
print("hola", nombre_de_usuario, "!!")

#si uso (,) usara el sep original, pero si uso (+) no habran espacios
#para modificar el separador original, se usa el sep y todo lo que vaya dentro de sus "" es el separador
print("hola", nombre_de_usuario, "!!",sep="")

#concatenar utilizando variable
#si usamos la (,) se va a ver el comando entero, si usamos el (+) se vera bien
nombre_de_usuario = input("ingresa tu nombre: ")
saludo = "hola " + nombre_de_usuario + " !!"
print(saludo)

#si utilizamos un Int en un print con str, tirara error, hay que convertilo a str
edad_del_usuario = int(input("ingresa tu edad: "))
saludo2= "tenes " + str(edad_del_usuario) + " años"
print(saludo2)
#si en vez de usar (+) utilizamos (,) no vamos a tener este inconveniente
edad_del_usuario = int(input("ingresa tu edad: "))
print("tenes",edad_del_usuario,"años")
