def V_int(valor):
    if type(valor) == int:
        return True
    if type(valor) == str and valor.isdigit():
        return True
    return False

def V_float(valor):
    if type(valor) == float:
        return True
    if type(valor) == str and "." in valor:
        partes = valor.split(".")
        return partes[0].isdigit() and partes[1].isdigit()  
    return False

def V_primo(valor):
    for n in range(2, valor):
        if valor % n == 0:
            print("no es primo")
            return False
    print("Numero primo")
    return True

def es_alfanumerico(valor):
    if type(valor) == str and valor.isalnum():
        return True
    return False
 


