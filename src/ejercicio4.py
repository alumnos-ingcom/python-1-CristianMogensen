################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
4. Suma lenta
Escribir una función que haga la suma entre dos números enteros sin hacer
la operación de manera directa. Esto quiere decir que para hacer la suma entre
4 y 3, las operaciones resultantes deberán ser 4+1+1+1.

La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.

def suma_lenta(numero, otro_numero):
"""


# Reutilizo la funcion signo del ejercicio 2:
try:
    from ejercicio2 import signo
except ImportError as exc:
    from src.ejercicio2 import signo


def suma_lenta(numero: int, otro_numero: int) -> int:
    """
    Esta función realiza la suma de numero y otro_numero en pasos de 1 unidad.
    Ejemplo: 4+3 = 4+1+1+1 = 7
    PRECONDICIONES: Ingreso de números enteros (numero y otro_numero).
    POSCONDICIONES: Retorna un número entero (resultado de la suma).
    """

    # Se declaran y definen las variables que representan el contador del
    # bucle while a utilizar, y el resultado final.
    contador: int = abs(otro_numero)
    resultado: int = numero

    # Determina si la unidad a sumar es positiva o negativa:
    unidad: int = signo(otro_numero)

    # Suma o resta de a 1 unidad:
    while (contador > 0):

        resultado += unidad

        contador -= 1

    return resultado


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    # Se imprime el título del ejercicio:
    print("\nEjercicio 4: Suma lenta\n")

    # Se declara y define una variable en la que el usuario ingresará el
    # primer número a sumar.
    numero_1: int = None

    # Se define un ciclo while para asegurar que el primer número ingresado
    # sea un entero válido.
    while numero_1 is None:

        # Se realiza el input del usuario y se ataja el error si no se ingresa
        # un valor válido. (se repite el input hasta que sea correcto).
        try:

            numero_1 = int(input("Ingrese primer número a sumar: "))

        except ValueError as exc:

            # Se ataja error, en caso de que no se haya ingresado un valor
            # válido, y se imprime mensaje de error.
            print("Error: El valor ingresado debe ser un número entero.\n")

            # Se reinicia la variable para que se repita el ciclo while.
            numero_1 = None

    # Se declara y define una variable en la que el usuario ingresará el
    # segundo número a sumar.
    numero_2: int = None

    # Se define un ciclo while para asegurar que el segundo número ingresado
    # sea un entero válido.
    while numero_2 is None:

        # Se realiza el input del usuario y se ataja el error si no se ingresa
        # un valor válido. (se repite el input hasta que sea correcto).
        try:

            numero_2 = int(input("Ingrese segundo número a sumar: "))

        except ValueError as exc:

            # Se ataja error, en caso de que no se haya ingresado un valor
            # válido, y se imprime mensaje de error.
            print("Error: El valor ingresado debe ser un número entero.\n")

            # Se reinicia la variable para que se repita el ciclo while.
            numero_2 = None

    # Se realiza la suma lenta.
    resultado_suma_lenta: int = suma_lenta(numero_1, numero_2)

    # Se imprime el resultado final.
    print("El resultado de la suma lenta entre los números es:")
    print(f"({numero_1}) + ({numero_2}) = {resultado_suma_lenta}")


if __name__ == "__main__":
    principal()
