#1
nombre_de_usuario = input("tu nombre es: ")
print("Hola",nombre_de_usuario,"!!")
#2
numero1 = int(input("tu primer numero es: "))
numero2 = int(input("tu segundo numero es: "))
numerofinal = numero1 + numero2
print("la suma de tus numeros es:",numerofinal)
#3
nombre_de_usuario = input("nombre: ")
apellido_de_usuario = input("apellido: ")
edad_de_usuario = int(input("edad: "))
print("Tu nombre es:",nombre_de_usuario)
print("Tu apellido es:",apellido_de_usuario)
print("Tu edad es: ",edad_de_usuario)
#4
nombre = input("nombre: ")
num_comision = int(input("numero de comision: "))
asignatura = input("asignatura:")
docente = input("docente:")
presente = input("Fuiste a clase: ")
print("Tu nombre es:",nombre)
print("Tu numero de comision es:",num_comision)
print("la asignatura es:",asignatura)
print("Tu docente es:",docente)
print("asististe a clases: ",presente)
#5
lado = float(input("Ingrese el lado del cuadrado: "))
superficie_cuadrado = lado ** 2
print(f"La superficie del cuadrado es: {superficie_cuadrado}")
#6
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))
superficie_rectangulo = base * altura
print(f"La superficie del rectángulo es: {superficie_rectangulo}")
#7
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
superficie_triangulo = (base * altura) / 2
print(f"La superficie del triángulo es: {superficie_triangulo}")
#8
producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
iva = precio * 0.21
precio_con_iva = precio + iva
print(f"El producto {producto} tiene un precio final de {precio_con_iva} con IVA incluido (IVA: {iva})")
#9
nombre = input("Ingrese el nombre del alumno: ")
apellido = input("Ingrese el apellido del alumno: ")
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
promedio = (nota1 + nota2 + nota3) / 3
print(f"El alumno {nombre} {apellido} tiene un promedio de {promedio:.2f}")
#10
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
edad_futura = edad + 10
print(f"{nombre}, dentro de 10 años tendrás {edad_futura} años.")

