lista = [64, 34, 25, 12, 22, 11, 90]

n = len(lista)
i = 0

lista = [64, 34, 25, 12, 22, 11, 90]

n = len(lista)
i = 0
for a in range(len(lista) - 1):
    intercambiado = False  # Bandera para saber si hubo intercambio
    j = 0
    # Recorremos la lista desde el inicio hasta el penúltimo elemento no ordenado
    # (n - 1 - i) porque cada pasada coloca el mayor elemento al final
    # y no es necesario volver a revisarlo
    for b in range(len(lista) - 1 - i):
        if lista[j] > lista[j + 1]:  # Si los elementos están fuera de orden
            temp = lista[j]
            lista[j] = lista[j + 1]  # Intercambiamos
            lista[j + 1] = temp
            intercambiado = True  # Marcamos que hubo intercambio
        j = j + 1
    if not intercambiado:  # Si no hubo ningún intercambio, la lista ya está ordenada
        break
    i = i + 1
print(lista)
#Encontre la forma de hacerlo reemplazando los while por for y habia que reemplazar ej:[n - 1 - i]
#por un len(lista), porque len(lista) porque usamos for cuando ya sabemos la cantidad de vueltas
#que queremos dar y len(lista) es el tamaño de la lista principal que usamos como cantidad.