################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
10. Palíndromo
Escribir una función que indique con True si una palabra o frase ingresada
se trata de un palindromo. Palíndromo, es si se lee igual de derecha a
izquierda que de izquierda a derecha.

def es_palindromo(texto):
"""


def es_par(numero: int) -> bool:
    """
    Esta función analiza un número y retorna True o False si es par o impar.
    PRECONDICIONES: Recibe un número entero.
    POSCONDICIONES: Devuelve un bool (True: par, False: impar).
    """

    return not (numero % 2)


def es_palindromo(texto: str) -> bool:
    """
    Esta función analiza si el texto o la palabra ingresada es un palíndromo
    o no, y retorna un booleano 'True' en caso de que sí y 'False' en caso de
    que no lo sea.
    PRECONDICIONES: Recibe un string.
    POSCONDICIONES: Devuelve un bool.
    """

    # Se declara y define la variable en la que se guardará el resultado final.
    palindromo: bool = True

    # Se declara y define la variable con la que se recorrerá cada caracter del
    # texto ingresado.
    elem: int = 0

    if (es_par(len(texto))):

        while (elem < len(texto)//2):

            if (texto[elem] != texto[(len(texto) - 1 - elem)]):

                palindromo = False

                break

            elem += 1

    else:

        while (elem < (len(texto)//2 + 1)):

            if (texto[elem] != texto[(len(texto) - 1 - elem)]):

                palindromo = False

                break

            elem += 1

    return palindromo


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    # Se imprime el título del ejercicio:
    print("\nEjercicio 10: Palíndromo\n")

    # Se hace el input del usuario.
    texto: str = input("Ingrese palabra: ")

    # Se verifica si es palíndromo.
    palindromo: bool = es_palindromo(texto)

    # Se imprime el resultado final.
    if palindromo:

        print(f"La palabra {texto} es un palíndromo.")

    else:

        print(f"La palabra {texto} NO es un palíndromo.")


if __name__ == "__main__":
    principal()
