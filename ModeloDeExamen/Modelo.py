# Una empresa se dedica al almacenamiento y posterior distribución de cereales en el interior del país. 
# Para ello cuentan con 20 depósitos en CABA, que generalmente se encuentran en las inmediaciones de las 
# estaciones del ferrocarril. 
# Los depósitos pueden almacenar 4 tipos diferentes de cereales: maíz, trigo, cebada y centeno. 
# La oficina central, recibe mensualmente una planilla de existencias donde se indican las existencias de 
# cada cereal para cada depósito. 
# Realizar un menú de opciones: while - match case
# 1. Obtener existencias: para ello deberá crear una función que cargue la existencia de cada grano(input) 
# en todos los depósitos. Los valores estarán comprendidos entre 5000 Kg y 20000 Kg. 
# (validar, que sea número) deposito_1 =  depositos[0] = 500
# 2. Calcular por cada depósito la cantidad total de kilos almacenados entre todos los cereales. 
# 3. Nombre del cereal que almaceno menos kilos en cada depósito. 
# 4. Máxima cantidad de kilos almacenados de cada cereal. 
# 5. Depósito con mayor recaudación, teniendo en cuenta que disponemos de un vector con los valores por 
# kilo de cada tipo de cereal. 
# 6. Cantidad de depósitos que hayan almacenado más de 50000 kilos entre los 4 cereales. 
# 7. Porcentaje de kilos de cada cereal sobre el total de kilos almacenados. Además mostrar el nombre 
# del cereal con el máximo porcentaje. 
# 8. Generar un informe con la recaudación de cada depósito, ordenada de mayor a menor.

### Que debo usar?: while, match case, input(validar que es num),def,min,max,if, porcentaje, ordenamiento
### array, matriz, acumulador y quiza contador

### consejo del gordo gordo: "hacer un def que sume uno solo (que sume 1 deposito) y usarlo en todo lo 
### demas acumulado"
from repetitivos import *

depositos = []
depositos_cargados = 0
valor = [10, 20, 50, 25]
cereales = ["Maiz", "Trigo", "Cebada", "Centeno"]

for i in range(20):
    deposito = [0,0,0,0]
    depositos.append(deposito)

def menu():
    while True:
        print("-----¡BIENVENIDO!-----")
        print("[0] Cargar Existencias") 
        print("[1] Suma TOTAL de kilos x Deposito")
        print("[2] Min cant de kilos de cereal x Deposito")
        print("[3] Max cant de kilos de cereal x Deposito")
        print("[4] Deposito con mayor ingreso total")
        print("[5] Mostrar depositos con ingreso mayor a 50000 totales")
        print("[6] Mostrar porcentajes de cereal en el total del deposito")
        print("[7] Generar informe con la recaudacion de cada deposito")
        print("[8] Para salir")

        while True:
            opcion = input("\nPorfavor ingrese una opcion [0-8]: ")
            if opcion.isdigit():
                opcion = int(opcion)
                if 0 <= opcion <= 8:
                    break
                else:
                    print("\nERROR: ELIJE UNA OPCION CORRECTA")
            else:
                print("\nERROR: INGRESA UN NUMERO VALIDO")
   
        match opcion:

            case 0:
                caso0()
            case 1:
                caso1()
            case 2:
                caso2()
            case 8:
                print("\nChauchi!\n")
                break

def caso0():
    global depositos_cargados
    num_deposito = Deposit()
#MAIZ
    while True: 
                maiz = input("Ingresa los kilos de maiz: ")
                if maiz.isdigit():
                    maiz = int(maiz)
                    if maiz < 5000:
                            print("ERROR: El ingreso minimo es de [5000]")
                    elif maiz > 20000:
                        print("ERROR: El ingreso maximo es de [20000]")
                    else:
                        depositos[num_deposito][0] += maiz
                        break
                else:
                    print("\nERROR: INGRESA UN NUMERO VALIDO")
#TRIGO
    while True: 
        trigo = input("Ingresa los kilos de trigo: ")
        if trigo.isdigit():
            trigo = int(trigo)
            if trigo < 5000:
                print("ERROR: El ingreso minimo es de [5000]")
            elif trigo > 20000:
                print("ERROR: El ingreso maximo es de [20000]")
            else:
                depositos[num_deposito][1] += trigo
                break
        else:
            print("\nERROR: INGRESA UN NUMERO VALIDO")
#CEBADA
    while True: 
        cebada = input("Ingresa los kilos de cebada: ")
        if cebada.isdigit():
            cebada = int(cebada)
            if cebada < 5000:
                print("ERROR: El ingreso minimo es de [5000]")
            elif cebada > 20000:
                print("ERROR: El ingreso maximo es de [20000]")
            else:
                depositos[num_deposito][2] += cebada
                break
        else:
            print("\nERROR: INGRESA UN NUMERO VALIDO")
#CENTENO
    while True:
        centeno = input("Ingresa los kilos de centeno: ")
        if centeno.isdigit():
            centeno = int(centeno)
            if centeno < 5000:
                print("ERROR: El ingreso minimo es de [5000]")
            elif centeno > 20000:
                print("ERROR: El ingreso maximo es de [20000]")
            else:
                depositos[num_deposito][3] += centeno
                break
        else:
            print("\nERROR: INGRESA UN NUMERO VALIDO")
    print("\nLos datos ingresados son: ")
    print(f"-----Deposito [{num_deposito}]-----")
    print(f"Cant. Maiz: {depositos[num_deposito][0]}")
    print(f"Cant. Trigo: {depositos[num_deposito][1]}")
    print(f"Cant. Cebada: {depositos[num_deposito][2]}")
    print(f"Cant. Centeno: {depositos[num_deposito][3]}")
    depositos_cargados += 1
    print("\nPresione [Enter] Para volver al menu")
    input()

def caso1():
    global depositos_cargados
    if depositos_cargados == 0:
        print("\nERROR: Cargue minimo 1 deposito primero antes")
        print("\nPresione [Enter] Para volver al menu")
        input()
    else:
        num_deposito = Deposit()
        if depositos[num_deposito] == [0,0,0,0]:
            print("\nERROR: Cargue las existencias del deposito primero!")
            print("\nPresione [Enter] Para volver al menu")
            input()                
        else:
            sumaTotal = depositos[num_deposito][0] + depositos[num_deposito][1] + depositos[num_deposito][2] + depositos[num_deposito][3]
            print(f"\nLa suma total de los cereales del deposito {num_deposito} es de: {sumaTotal}")
            print("\nPresione [Enter] Para volver al menu")
            input()

def caso2():
    global depositos_cargados
    if depositos_cargados == 0:
        print("\nERROR: Cargue minimo 1 deposito primero antes")
        print("\nPresione [Enter] Para volver al menu")
        input()
    else:
        num_deposito = Deposit()
        n = len(deposito)
        i = 0
        for a in range(len(deposito) - 1):
            intercambiado = False
            j = 0
            for b in range(len(depositos[num_deposito]) - 1 - i):
                if depositos[num_deposito][j] > depositos[num_deposito][j + 1]: 
                    temp = depositos[num_deposito][j]
                    nombre_cereal_temp = cereales[j]
                    depositos[num_deposito][j] = depositos[num_deposito][j + 1]
                    cereales[j] = cereales[j + 1] 
                    depositos[num_deposito][j + 1] = temp
                    cereales[j + 1] = nombre_cereal_temp 
                    intercambiado = True  
                j = j + 1 
            if not intercambiado:
                break 
            i = i + 1 
        print(f"El cereal con la minima cantidad es [{cereales[0]}] con {depositos[num_deposito][0]}")
        print("\nPresione [Enter] Para volver al menu")
        input()

menu()