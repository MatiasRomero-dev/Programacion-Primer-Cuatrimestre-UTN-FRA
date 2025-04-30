#TAREA: realizar un algoritmo donde se le pida al user que elija entre un producto u otro, pero 
# que decida cuantas encuentas desea contestar (cada iteracion es un user)

lista_productos = ["Manteca", "queso", "bondiola", "destornillador"]
print(f"Productos en stock {lista_productos}")
producto = input("Bienvenido a Josimar, que producto quieres elegir?: ")

while producto == "":
    print("Producto no valido, pruebe denuevo")
    producto = input("Que producto quieres elegir?: ")

print(f"Usted eligio {producto} desea agregar algo mas?")
