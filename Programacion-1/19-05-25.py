# matriz = [[10,20,30],
#          [40,50,60]]

# # for i in range(len(matriz)):
# #     print(matriz[i])
# matriz[0][0] = 15
# print(matriz[0][0])
# for i in range(len(matriz)):
#     for j in range(len(matriz[i])):
#         print(matriz[i][j], end=" ")
#     print("")
    
# filas = 3
# columnas = 4
# matriz = [[0 for c in range(columnas)] for f in range(filas)]
# for i in range(len(matriz)):
    #     for j in range(len(matriz[i])):
    #          print(matriz[i][j], end=" ")
    #     print("")

def cargar_matriz_aleatoriamente(matriz: list):
    seguir = "S"
    while seguir == "S":
        filas = int(input("Cuantas filas desea ingresar: "))
        columnas = int(input("Cuantas columnas desea ingresar: "))
        fila = int(input("Indice de fila: "))
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


 