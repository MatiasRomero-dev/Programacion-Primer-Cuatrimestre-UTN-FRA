#def dividir(a: int, b: int) -> int:
    #return int (a / b)

#resultado = dividir(3.20, 2.10)
#print(resultado)

# # 1 Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.
# def ingrese_int():
#     numero = input("Ingrese un numero: ")
#     if numero.isdigit():
#         print("Numero Valido")
#     else:
#         print("Error, ingrese un numero entero")
#     return numero
# mi_numero = ingrese_int()
# if mi_numero.isdigit():
#     print(f"El numero ingresado fue: {mi_numero}")


# 2 Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.
# def ingrese_float():
#     numero = input("Ingrese un numero decimal: ")
#     partes = numero.split(".")
#     if len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit():
#         return float(numero)
#     else:
#             print("Flotante invalido")
# mi_numero = ingrese_float()
# print(f"Tu numero es flotante [{mi_numero}]")




# # 3 Crear una función que le solicite al usuario el ingreso de una cadena y la retorne.
# def ingrese_str():
#     cadena = input("Ingrese alguna palabra: ")
#     if cadena.isalpha():
#         print("Cadena Valida")
#     else:
#         print("Error, ingrese una cadena")
#     return cadena
# mi_cadena = ingrese_str()
# print(f"La cadena ingresada fue: {mi_cadena}")


# # 4 Escribir una función que calcule el área de un rectángulo.
# La función recibe la base y la altura y retorna el área. 
# def calculo_de_area_rectangulo():
#     while True:
#         base = input("Ingrese la base: ")
#         if base.isdigit():
#             base = int(base)
#             break
#         else:
#             print("Invalido")
#     while True:
#         altura = input("Ingrese la altura: ")
#         if altura.isdigit():
#             altura = int(altura)
#             break
#         else:
#             print("Invalido")
#     area = base * altura
#     return area

# resultado = calculo_de_area_rectangulo()
# print(f"El area del cuadrado es de {resultado}")


# 5 Escribe una función que calcule el área de un círculo. 
# La función debe recibir el radio como parámetro y devolver el área.
# def calculo_de_area_circulo():
#     while True:
#         radio = input("Ingrese el radio: ")
#         if radio.isdigit():
#             radio = int(radio)
#             break
#         else:
#             print("Ingresa un digito")
#     area = radio ** 2
#     return area
# resultado = calculo_de_area_circulo()
# print(f"El area del circulo es de {resultado}")


# 6 Crea una función que verifique si un número dado es par o impar. 
# La función debe imprimir un mensaje indicando si el número es par o impar.
# def par_o_impar():
#     while True:
#         numero = input("Ingrese un numero: ")
#         if numero.isdigit():
#             numero = int(numero)
#             break
#         else:
#             print("Ingrese un numero valido")
#     if numero % 2 == 0:
#         par = numero
#         print(f"es par")
#         return par
#     else:
#         impar = numero
#         print(f"es impar")
#         return impar
# resultado = par_o_impar()
# 7 Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.
# def par_o_impar():
#     numero = input("Ingrese un numero: ")
#     par = False
#     while True:
#         if numero.isdigit():
#             numero = int(numero)
#             break
#         else:
#             print("Ingrese un numero valido")
#     if numero % 2 == 0:
#         par = True
#         return par
#     else:
#         return par
# resultado = par_o_impar()
# print(resultado)

# 8 Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
# def max():
#     max = float("-inf")
#     for i in range(3):
#         while True:
#             i = input("Ingrese su numero: ")
#             if i.isdigit():
#                 i = int(i)
#                 break
#             else:
#                 print("numero invalido")
#         if i > max:
#             max = i
#     return max

# print(f"El numero mayor es: {max()}")

# 9 Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.
# def potencia():
#     while True:
#         while True:
#             base = input("Ingrese el numero base: ")
#             if base.isdigit():
#                 base = int(base)
#                 break
#             else:
#                 print("Base invalida")
#         while True:
#             potencia = input("Ingrese el numero potenciador: ")
#             if potencia.isdigit():
#                 potencia = int(potencia)
#                 break
#             else:
#                 print("potenciador invalido")
#         break
#     resultado = base ** potencia
#     return resultado
# print(f"La potencia dio como resultado {potencia()}")

# 10 Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.
# def primo():
#     while True:
#         numero = input("Ingrese un numero: ")
#         if numero.isdigit():
#             numero = int(numero)
#             break
#         else:
#             print("Ingrese un numero valido")
#     if numero <= 1:
#         print("No es primo")
#         return False
#     for i in range(2, numero):
#         if numero % i == 0:
#             print("No es primo")
#             return False
#     print("Es primo")
#     return True
# resultado = primo()
# print(resultado)


        
     



