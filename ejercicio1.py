def main():
    print("- - - CALCULADORA - - -\n\n")
    while True:
        print("Operaciones disponibles:\n"
              "1) SUMA\n"
              "2) RESTA\n"
              "3) MULTIPLICACION\n"
              "4) DIVISION\n"
              "5) SALIR")
        entrada = input("Ingrese numero de operacion a realizar: ")
        if entrada == "1":
            x = suma()
        elif entrada == "2":
            x = resta()
        elif entrada == "3":
            x = multiplicacion()
        elif entrada == "4":
            x = division()
        else:
            exit()
        print("Resultado: ", x, "\n\n")


def suma():
    x,y = pedirValores()
    return x + y

def resta():
    x,y = pedirValores()
    return x - y

def multiplicacion():
    x,y = pedirValores()
    return x * y

def division():
    x,y = pedirValores()
    if y == 0:
        return "No se puede dividir por cero"
    return x / y

def pedirValores():
    x = int(input("Ingrese 1er numero: "))
    y = int(input("Ingrese 2do numero: "))
    return x,y

if __name__ == '__main__':
    main()