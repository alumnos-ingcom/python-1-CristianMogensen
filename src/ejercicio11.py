################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
11. Multiplos de
Escribir una función que indique con True si un número entero es multiplo
de otro, utilizando sumas y restas.

def es_multiplo(numero, multiplo):
"""


# Se importa la funcion division_lenta del ejercicio 5, que utiliza solamente
# sumas y restas.
try:
    from ejercicio5 import division_lenta
except ImportError as exc:
    from src.ejercicio5 import division_lenta


def es_multiplo(numero: int, multiplo: int) -> bool:
    """
    Esta función analiza si el número del segundo argumento es múltiplo del
    primero. Retorna 'True' en caso de que sí y 'False' en caso que no lo sea.
    PRECONDICIONES: Recibe 2 números enteros (numero, multiplo).
    POSCONDICIONES: Devuelve un bool.
    """

    # Se declara y define una variable en la que se opera para verificar
    # si 'multiplo' es realmente un múltiplo de 'numero'.
    division: tuple = division_lenta(numero, multiplo)

    # Se verifica entonces que, si el resto es cero, el 'multiplo' ingresado
    # es efectivamente un múltiplo del 'numero'.
    return (division[1] == 0)


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    # Se imprime el título del ejercicio:
    print("\nEjercicio 11: Multiplos de\n")

    # Se declara y define una variable en la que el usuario ingresará el
    # primer número.
    numero: int = None

    # Se define un ciclo while para asegurar que el número ingresado sea un
    # entero válido.
    while numero is None:

        # Se realiza el input del usuario y se ataja el error si no se ingresa
        # un valor válido. (se repite el input hasta que sea correcto).
        try:

            numero = int(input("Ingrese el primer número: "))

        except ValueError as exc:

            # Se ataja error, en caso de que no se haya ingresado un valor
            # válido, y se imprime mensaje de error.
            print("Error: El valor ingresado debe ser un número entero.\n")

            # Se reinicia la variable para que se repita el ciclo while.
            numero = None

    # Se declara y define una variable en la que el usuario ingresará el
    # segundo número, que se verificará si es múltiplo del otro.
    multiplo: int = None

    # Se define un ciclo while para asegurar que el número ingresado sea un
    # entero válido.
    while multiplo is None:

        # Se realiza el input del usuario y se ataja el error si no se ingresa
        # un valor válido. (se repite el input hasta que sea correcto).
        try:

            multiplo = int(input("Ingrese el primer número: "))

        except ValueError as exc:

            # Se ataja error, en caso de que no se haya ingresado un valor
            # válido, y se imprime mensaje de error.
            print("Error: El valor ingresado debe ser un número entero.\n")

            # Se reinicia la variable para que se repita el ciclo while.
            multiplo = None

    # Se verifica que sean múltiplos.
    resultado: bool = es_multiplo(numero, multiplo)

    if resultado:

        print(f"\nEl número {multiplo} es múltiplo de {numero}.")

    else:

        print(f"\nEl número {multiplo} NO es múltiplo de {numero}.")


if __name__ == "__main__":
    principal()
