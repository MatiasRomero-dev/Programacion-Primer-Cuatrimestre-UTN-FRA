def Deposit():
        while True:
            num = input("\nEn cual deposito deseas ingresar? [0-19]: ")
            if num.isdigit():
                num = int(num)
                if 0 <= num <= 19:
                    return num
                else:
                    print("\nERROR: ESCOJA UN DEPOSITO VALIDO [0-19]")
            else:
                print("\nERROR: INGRESA UN NUMERO VALIDO")