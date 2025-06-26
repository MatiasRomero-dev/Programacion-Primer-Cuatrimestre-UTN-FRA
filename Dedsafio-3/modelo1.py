F = int(input("Ingrese el numero de filas: "))
C = int(input("Ingrese el numero de columnas: "))

def cargar_matriz(F,C):
    if F != C:
        print("[ERROR] Ingrese una matriz cuadrada (n x n)")
        return

    matriz = []
    print("Porfavor Ingrese los datos que desea en la matriz!")
    print("[Los datos se iran colocando Fila x Fila]: ")

    for i in range(F):  
        a =[]
        for j in range(C): 
            a.append(int(input("Dato: ")))
        matriz.append(a)
    print("\n")

    for i in range(F):
        for j in range(C):
            print(matriz[i][j], end=" ")
        print("")
    print("\n")
    
cargar_matriz(F,C)
