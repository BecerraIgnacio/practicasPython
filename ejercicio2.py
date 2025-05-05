"""
Generar numero aleatorio
Usuario adivina, devuelve si mayor o menor, hasta que usuario acierta
"""
import random

def main():
    while True:
        jugar_adivinar()
        if input("¿Otra partida? (s/n): ").lower() != 's':
            break

def jugar_adivinar():
    print("- - - ADIVINE EL NUMERO - - -\n\n"
          "Genere un numero aleatorio entre 1 intento 100 (inclusive)\n"
          "Debes adivinarlo!\n"
          "Dime un numero, si no adivinas te dire si mi numero es mayor o menor\n\n")
    secreto = random.randint(1,100)
    intento = 0
    while True:
        numero = ingresar_numero()
        intento = intento+1
        if secreto == numero:
            print("Acertaste!")
            print(f"El numero era {secreto}, te tomo {intento} oportunidades acertar!")
            break
        elif numero > secreto:
            print(f"No acertaste! Mi numero es menor a {numero}")
        elif numero < secreto:
            print(f"No acertaste! Mi numero es mayor a {numero}")


def ingresar_numero():
    entrada = input("\nIngrese un numero: ")
    try:
        x = int(entrada)
        if 1 <= x <= 100:
            return x
        else:
            print("El numero tiene que ser un numero entre 1 y 100")
            return ingresar_numero()
    except ValueError:
        print("El numero ingresado no valido")
        return ingresar_numero()



if __name__ == "__main__":
    main()