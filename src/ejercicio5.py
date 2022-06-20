################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
5. Divisiones
Escribir una función que mediante restas sucesivas, obtenga el valor del
cociente y resto de dos números enteros.

def division_lenta(dividendo, divisor):
"""

from typing import Union, Tuple

# Se importa la función signo del ejercicio 2, para verificar que los signos
# del divisor y dividendo sean iguales.
try:
    from ejercicio2 import signo
except ImportError as exc:
    from src.ejercicio2 import signo

# Se importa la función de suma_lenta para reemplazar a la suma común.
try:
    from ejercicio4 import suma_lenta
except ImportError as exc:
    from src.ejercicio4 import suma_lenta


def division_lenta(dividendo: Union[int, float],
                   divisor: Union[int, float]) -> Tuple[Union[int, float]]:
    """
    Esta función realiza la division entre dos numeros (dividendo, divisor)
    mediante restas sucesivas y devuelve una tupla con (cociente, resto)
    PRECONDICIONES: Recibe números enteros o decimales (dividendo y divisor).
    POSCONDICIONES: Devuelve una tupla con números enteros o decimales
                    (resultado de la división).
    """

    # Se verifica que no se ingrese el 0/0 (resultado indefinido).
    assert (dividendo != 0 and divisor != 0), "Error en la division: 0/0"

    # Se declara y define la variable que cuenta las veces que el divisor
    # "entra" en el dividendo, para luego determinar el cociente final.
    cociente: Union[int, float] = 0

    # Se declara y define la variable que determina el resto de la división.
    resto: Union[int, float] = dividendo

    if (signo(dividendo) == signo(divisor)):

        while (abs(resto) >= abs(divisor)):
            # cociente += 1
            # resto -= divisor

            cociente = suma_lenta(cociente, 1)

            resto = suma_lenta(resto, -divisor)

    else:

        while (abs(resto) >= abs(divisor)):
            # cociente -= 1
            # resto += divisor

            cociente = suma_lenta(cociente, -1)
            resto = suma_lenta(resto, divisor)

    # Defino la tupla a retornar por la función:
    resultado: Tuple[Union[int, float]] = (cociente, resto)

    return resultado


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    # Se imprime el título del ejercicio:
    print("\nEjercicio 5: Divisiones\n")

    # Se declara y define una variable en la que el usuario ingresará el
    # dividendo.
    dividendo: float = None

    # Se define un ciclo while para asegurar que el primer número ingresado
    # sea un decimal válido.
    while dividendo is None:

        # Se realiza el input del usuario y se ataja el error si no se ingresa
        # un valor válido. (se repite el input hasta que sea correcto).
        try:

            dividendo = float(input("Ingrese el dividendo: "))

        except ValueError as exc:

            # Se ataja error, en caso de que no se haya ingresado un valor
            # válido, y se imprime mensaje de error.
            print("Error: El valor ingresado debe ser un número decimal.\n")

            # Se reinicia la variable para que se repita el ciclo while.
            dividendo = None

    # Se declara y define una variable en la que el usuario ingresará el
    # divisor.
    divisor: float = None

    # Se define un ciclo while para asegurar que el primer número ingresado
    # sea un decimal válido.
    while divisor is None:

        # Se realiza el input del usuario y se ataja el error si no se ingresa
        # un valor válido. (se repite el input hasta que sea correcto).
        try:

            divisor = float(input("Ingrese el divisor: "))

        except ValueError as exc:

            # Se ataja error, en caso de que no se haya ingresado un valor
            # válido, y se imprime mensaje de error.
            print("Error: El valor ingresado debe ser un número decimal.\n")

            # Se reinicia la variable para que se repita el ciclo while.
            divisor = None

    # Se calcula el resultado.
    resultado: float = division_lenta(dividendo, divisor)

    # Se imprime el resultado final.
    print("El resultado de la division es:")
    print(f"{dividendo}/{divisor} = {resultado}")


if __name__ == "__main__":
    principal()
