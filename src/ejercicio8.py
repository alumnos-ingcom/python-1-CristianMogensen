################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
8. Números primos
Escribir una función que indique con True si un numero indicado es Primo.

def es_primo(numero):
"""


def es_primo(numero: int) -> bool:
    """
    Esta función evalúa si un número ingresado es primo o no, y retorna un
    booleano ('True' si es primo, 'False' si no lo es).
    PRECONDICIONES: Recibe un número entero.
    POSCONDICIONES: Devuelve un bool.
    """

    # Se declaran y definen las variables que ayudan a determinar si un número
    # es primo no.
    primo: bool = True
    modulo_numero: int = abs(numero)
    i: int = 2

    if (modulo_numero > 3):

        while (i < modulo_numero):

            # Chequeo si es divisible por i.
            if ((modulo_numero % i) == 0):

                primo = False

                break

            i += 1

    else:

        if (modulo_numero == 0):

            primo = False

        else:

            primo = True

    return primo


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    # Se imprime el título del ejercicio:
    print("\nEjercicio 8: Números primos\n")

    # Se declara y define una variable en la que se guardará el input del
    # usuario.
    numero: int = None

    # En el ciclo while se verifica que el usuario ingrese un valor válido
    # para el número a verificar si es primo.
    while numero is None:

        # Se prueba que el usuario ingrese un valor válido.
        try:

            numero = int(input("Ingrese un número: "))

            if (numero < 0):

                print("Error: Ingrese un número positivo.")

                # Se reinicia la variable para que se repita el ciclo e ingrese
                # correctamente el valor.
                numero = None

        # Se ataja posible error en el input.
        except ValueError as exc:

            print("Error: Debe ingresar un número entero.\n")

            # Se reinicia la variable para que se repita el ciclo e ingrese
            # correctamente el valor.
            numero = None

    # Se calcula el resultado.
    resultado: bool = es_primo(numero)

    # Se imprime el resultado final.
    if resultado:

        print(f"El número {numero} es primo.")

    else:

        print(f"El número {numero} NO es primo.")


if __name__ == "__main__":
    principal()
