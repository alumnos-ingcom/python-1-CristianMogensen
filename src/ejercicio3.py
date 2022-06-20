################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
3. Comparación de números
Escribir una función que utilizando sumas y restas, reciba dos valores y
retorne:

Retornar -1 si el primero es menor que el segundo
Retornar 0 si son iguales
Retornar 1 si el primero es mayor que el segundo

def compara(numero, otro_numero):
"""


# Reutilizo la funcion signo del ejercicio 2:
from ejercicio2 import signo


def compara(numero: int, otro_numero: int) -> int:
    """
    Esta función compara dos numeros, retornando:
    - (-1) si el primero es menor que el segundo
    - (0) si son iguales
    - (1) si el primero es mayor que el segundo
    PRECONDICIONES: Recibe dos números enteros a comparar.
    POSCONDICIONES: Retorna un número entero (1, -1 o 0).
    """

    # Comparo ambos números y determino cuál es mayor
    # observando el signo final de la comparación.
    comparacion = numero - otro_numero

    return signo(comparacion)


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    # Se imprime el título del ejercicio:
    print("\nEjercicio 3: Comparación de números\n")

    # Se declara y define una variable en la que el usuario ingresará el
    # primer número a comparar.
    numero_1: int = None

    # Se define un ciclo while para asegurar que el primer número ingresado
    # sea un entero válido.
    while numero_1 is None:

        # Se realiza el input del usuario y se ataja el error si no se ingresa
        # un valor válido. (se repite el input hasta que sea correcto).
        try:

            numero_1 = int(input("Ingrese primer número: "))

        except ValueError as exc:

            # Se ataja error, en caso de que no se haya ingresado un valor
            # válido, y se imprime mensaje de error.
            print("Error: El valor ingresado debe ser un número entero.\n")

            # Se reinicia la variable para que se repita el ciclo while.
            numero_1 = None

    # Se declara y define una variable en la que el usuario ingresará el
    # segundo número a comparar.
    numero_2: int = None

    # Se define un ciclo while para asegurar que el segundo número ingresado
    # sea un entero válido.
    while numero_2 is None:

        # Se realiza el input del usuario y se ataja el error si no se ingresa
        # un valor válido. (se repite el input hasta que sea correcto).
        try:

            numero_2 = int(input("Ingrese segundo número: "))

        except ValueError as exc:

            # Se ataja error, en caso de que no se haya ingresado un valor
            # válido, y se imprime mensaje de error.
            print("Error: El valor ingresado debe ser un número entero.\n")

            # Se reinicia la variable para que se repita el ciclo while.
            numero_2 = None

    # Se analiza el resultado.
    comparacion: int = compara(numero_1, numero_2)

    if (comparacion == 1):  # numero_1 > numero_2

        resultado: str = f"{numero_1} es mayor a {numero_2}"

    elif (comparacion == -1):  # numero_1 < numero_2

        resultado: str = f"{numero_1} es menor a {numero_2}"

    else:  # numero_1 = numero_2

        resultado: str = f"{numero_1} es igual a {numero_2}"

    # Se imprime el resultado final.
    print(f"El resultado de la comparación es: {resultado}.")


if __name__ == "__main__":
    principal()
