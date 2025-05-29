def cargar_matriz_notas():
    #Utilizo [WHILE] para pedir el ingreso de alumnos[N] y verificar que sea
    #un [INT] valido con un [IF/ELSE]
    while True:
        n = input("Ingrese cantidad de alumnos: ")
        if n.isdigit():
            n = int(n)
            break
        else:
            print("\n[ERROR]-Ingrese una cantidad valida!.")
#-------------------------------------------------------------------------            
    #Utilizo [WHILE] para pedir el ingreso de notas[m] y verificar que sea
    #un [INT] valido con un [IF/ELSE]
    while True:
        m = input("Ingrese las notas: ")
        if m.isdigit():
            m = int(m)
            break
        else:
            print("\n[ERROR]-Ingrese una cantidad valida!.")
#------------------------------------------------------------------------- 
#Aca procedo a crear una matriz vacia para asignarle el m x n ingresado.
    matriz = []
#Aca le asigno a la matriz vacia la cantidad de alumnos y notas con un for
#El for funciona con un rango de N (alumnos)
#El append agrega contenido a partir de la posicion 0 y lo que agrega
#Es M(osea Notas).
#Esto me crea la matriz con todo valor 0
    for i in range(n):
        matriz.append([0] * (m))
#Aca cree otro for para printearlo, solo para probar que funcione antes
#De asignarle notas.
    # for i in matriz:
    #     print(i)

    while True:
        #Este while abarca toda la seleccion del alumno y notas, para que utilizando
        #un [INPUT] el usuario pueda volver a cargar ya sea el mismo o diferente
        #alumno y cambiar su nota o poner una nota distinta!
        #Aca agregue una opcion de salida para ir al siguiente [DEF]
        salida = input("Si desea salir inserte [N] o [S] si desea continuar: ").lower()
        if salida == "n":
            break
        elif salida == "s":
            while True:
            #El primer alumno es 0 ya que la matriz o las listas empienzan del 0 y no del 1
            #No se como hacer para que sea del 1 al [Numero ingresado] jeje
                print("\nEl primer alumno es [0] no [1]")
                alumno = input(f"La cantidad de alumnos van del [0 al {n - 1}], a cual quiere asignar sus notas?: ")
            #Aca le pregunto en que alumno se quiere posicionar y valido que lo ingresado
            #sea un [INT] en el rango de [n] (que serian los alumnos existentes)
                if alumno.isdigit():
                    alumno = int(alumno)
                    if alumno <= n or alumno < 0:
                        break
                    else:
                        print(f"\n[ERROR]-Alumno no encontrado, pruebe del 0 al {n - 1}")
                else:
                    print("\n[ERROR]-Ingrese un alumno valido!.")

            #Ahora voy a crear otro [WHILE] para preguntar cual de las notas quiere cambiar
            #Pero basicamente copie y pegue el codigo de arriba y le hice unos cambios jiji
            while True:
            #La primera nota es 0 ya que la matriz o las listas empienzan del 0 y no del 1
            #No se como hacer para que sea del 1 al [Numero ingresado] jeje
                print("\nLa primera nota es [0] no [1]")
                nota_p = input(f"Las notas van del [0 al {m - 1}], que nota desea cambiar?: ")
            #Nota_P = se refiere a (Posicion de la nota)
            #Aca le pregunto en que nota se quiere posicionar y valido que lo ingresado
            #sea un [INT] en el rango de [m] (que serian las notas existentes)
                if nota_p.isdigit():
                    nota_p = int(nota_p)
                    if nota_p <= m or nota_p < 0:
                        break
                    else:
                        print(f"\n[ERROR]-Nota no encontrada, pruebe del 0 al {m - 1}")
                else:
                    print("\n[ERROR]-Ingrese una nota valida!.")
            #Ahora voy a crear un ultimo while para que ingrese la nota correspondiente
            while True:
            #Nota se refiere a (cuanto saco del 1 al 10)
                nota = input(f"\nIngrese la nota [{nota_p}] del alumno [{alumno}]: ")
                if nota.isdigit():
                    nota = int(nota)
            #Aca se valida si la nota es menor a 0 o mayor a 10, lo cual estaria mal.
                    if nota < 0 or nota > 10:
                        print("\n[ERROR]-Las notas van del 1 al 10")
                    else:
            #Si la nota va del 1 al 10 osea correcto, en el rango Matriz(estamos hablando
            # de la lista de alumnos y notas) pero le pongo que solo en [alumno] (alumno
            # ingresado por el usuario) y nota_p (la posicion de la nota ingresada por
            # el usuario, cambie esa nota) y luego lo printeo
                        matriz[alumno][nota_p] = nota
                        print(f"\nLa notas actuales del alumno serian [{matriz[alumno]}]")
                        break
                else:
                    print("\n[ERROR]-Ingrese un valor valido.")
            #Puse esta opcion para que el usuario pueda volver a ingresar otro o el mismo
            #alumno o otra o la misma nota.
            print("\nPara volver a poner otra nota al mismo alumno o distinto, inserte [ENTER]")
            input()
        else:
            print("Ingresa S o F")

    return matriz

#PUNTO 2
#cree una funcion nueva con (matriz)
def porcentaje_aprobados(matriz):

    print("\nPorcentaje de examenes aprobados por alumno: ")
#Aca cree un for que busca en el rango matriz y puse un contador y acumulador
    for i in range(len(matriz)):
#Contador_aprobados(contador) y total_notas(acumulador)
        contador_aprobados = 0
        total_notas = 0
#Aca hice que busque las notas en el rango matriz agarra las notas y las cuenta
#y si encuentra una con mayor o igual que 6, lo suma al contador
        for j in range(len(matriz[i])):
            nota = matriz[i][j]
#Si la nota no fue colocada y sigue en 0 lo toma como "no hay nota registrada"
            if nota != 0:
                total_notas += 1
                if nota >= 6:
                    contador_aprobados += 1
#Si el total de las notas es mayor a 0 (osea que si se introdujieron)
        if total_notas > 0:
#saca el procentaje y lo muestra por pantalla
            porcentaje = (contador_aprobados * 100) / total_notas
#Perdon por este print y el [.2f] es para que el porcentaje no saque
#porcentajes como 56.5555555555% y solo 56.55%
            print(f"El alumno [{i}] tiene {contador_aprobados} notas aprobadas de {total_notas} y su porcentaje es de {porcentaje:.2f}% notas aprobados")
        else:
#Si no tiene nota, tira un print diciendo "no hay nota"
            print(f"El alumno [{i}] no tiene nota registrada")

#Aca las llamo para mostrarlas
matriz = cargar_matriz_notas()
porcentaje_aprobados(matriz)

    
