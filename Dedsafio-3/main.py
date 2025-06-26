def cargar_matriz_aleatoriamente(matriz: list):
    seguir = "S"
    while seguir == "S":
        filas = int(input("Cuantas filas desea ingresar: "))
        columnas = int(input("Cuantas columnas desea ingresar: "))
        if len(filas) != len(columnas):
            print("\nPorfavor, introduzca una matriz cuadrada [n x n]")
        else:
            fila = int(input("\nIndice de fila: "))
            columna = int(input("Indice de columna: "))
            for i in range(filas):
                matriz.append([0] * (columnas))
            for i in matriz:
                print(i)
            print("")
            dato = int(input("Ingrese el numero a cargar: "))
            matriz[fila - 1][columna - 1] = dato
            seguir = input("Desea seguir cargando? S/N: ").lower()
    
mi_matriz = []
cargar_matriz_aleatoriamente(mi_matriz)

for i in mi_matriz:
    print(i)