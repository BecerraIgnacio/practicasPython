"""
Generar numero aleatorio
Usuario adivina, devuelve si mayor o menor, hasta que usuario acierta
"""
import random

def main():
    print("- - - ADIVINE EL NUMERO - - -\n\n"
          "Genere un numero aleatorio entre 1 y 100 (inclusive)\n"
          "Debes adivinarlo!\n"
          "Dime un numero, si no adivinas te dire si mi numero es mayor o menor\n\n")
    n = random.randint(1,100)
    y = 0
    while True:
        x = ingresar_numero()
        if n == x:
            print("Acertaste!")
            print(f"El numero era {n}, te tomo {y} oportunidades acertar!")
            break
        elif x > n:
            print(f"No acertaste! Mi numero es menor a {x}")
        elif x < n:
            print(f"No acertaste! Mi numero es mayor a {x}")
        y = y+1

    print("\n\nVolver a jugar? (1) Si, (2) No")
    if int(input("Ingrese numero: ")) == 1:
        main()
    else:
        exit()

def ingresar_numero():
    entrada = input("\nIngrese un numero: ")
    try:
        x = int(entrada)
        if x > 0 or x < 101:
            return x
        else:
            print("El numero tiene que ser un numero entre 1 y 100")
            return ingresar_numero()
    except ValueError:
        print("El numero ingresado no valido")



if __name__ == "__main__":
    main()