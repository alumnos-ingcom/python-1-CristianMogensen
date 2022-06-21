################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
9. Factores Primos
Escribir una función que retorne una tuple con factores primos de un numero
entero positivo.

def factores_primos(numero):
"""


# Se reutiliza la funcion signo del ejercicio 8:
try:
    from ejercicio8 import es_primo
except ImportError as exc:
    from src.ejercicio8 import es_primo


def factores_primos(numero: int) -> tuple:
    """
    Esta función analiza los factores primos de un numero y los retorna
    como tupla. (n1, n2, ...)
    PRECONDICIONES: Recibe un número entero.
    POSCONDICIONES: Retorna una tupla de números enteros.
    """

    # Se declara y define la variable en la que se guardarán los resultados,
    # inicializado con el primer factor primo de cualquier número (el 1).
    resultado = (1,)

    modulo = abs(numero)

    # Caso trivial.
    if (numero == 0):

        return None

    elif (es_primo(modulo)):

        if (modulo > 1):

            # Si el número es primo, basta con sumarle a la tuple su mismo
            # valor, y ese será el resultado final.
            resultado += (modulo,)

    # Si el número ingresado no es primo, entonces hay que verificar número
    # por número qué número es factor primo.
    else:

        # Se declara y define la variable que recorrerá todos los números
        # menores al número ingresado, en búsqueda de si es o no un factor
        # primo.
        i: int = 2

        while (i < modulo):

            # Se verifica si es divisible por i.
            if ((modulo % i) == 0):

                resultado += (i,)

            i += 1

    return resultado


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    # Se imprime el título del ejercicio:
    print("\nEjercicio 9: Factores Primos\n")

    # Se declara y define una variable en la que el usuario ingresará el
    # número a analizar.
    numero: int = None

    # Se define un ciclo while para asegurar que el número ingresado sea un
    # entero válido.
    while numero is None:

        # Se realiza el input del usuario y se ataja el error si no se ingresa
        # un valor válido. (se repite el input hasta que sea correcto).
        try:

            numero = int(input("Ingrese el número: "))

        except ValueError as exc:

            # Se ataja error, en caso de que no se haya ingresado un valor
            # válido, y se imprime mensaje de error.
            print("Error: El valor ingresado debe ser un número entero.\n")

            # Se reinicia la variable para que se repita el ciclo while.
            numero = None

    # Se calcula el resultado.
    resultado: tuple = factores_primos(numero)

    # Se imprime el resultado final.
    print(f"\nSus factores primos son: {resultado}")


if __name__ == "__main__":
    principal()
