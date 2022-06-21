################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
6. Ordenar 3 valores
Escribir una función que a partir de tres variables de tipo entero retorne
una tupla con dichos valores ordenados de menor a mayor. Y Viceversa

def ordenar_mayor_a_menor(uno, dos, tres):
def ordenar_menor_a_mayor(uno, dos, tres):
"""


from typing import Union, List


def encontrar_mayor(lista_de_numeros: list) -> Union[int, float]:
    """
    Esta función encuentra el MAYOR de todos los numeros de una lista y
    retorna su valor.
    PRECONDICIONES: Recibe una lista de numeros (enteros o decimales).
    POSCONDICIONES: Devuelve un entero o decimal (depende del tipo de
                    dato de la lista).
    """

    # Se declara y define la variable que recorrerá cada elemento en el bucle
    # while y la variable en la que se guardará el resultado final.
    elemento: int = 0
    mayor: Union[int, float] = lista_de_numeros[0]

    # Caso trivial (1 elemento en la lista):
    # lista_de_numeros.len() = 1
    if (len(lista_de_numeros) == 1):

        return mayor

    # Caso normal (más de 1 elemento):
    while (elemento < (len(lista_de_numeros) - 1)):

        if (mayor < lista_de_numeros[elemento + 1]):

            mayor = lista_de_numeros[elemento + 1]

        elemento += 1

    return mayor


def encontrar_menor(lista_de_numeros: list) -> Union[int, float]:
    """
    Esta función encuentra el MENOR de todos los numeros de una lista y
    retorna su valor.
    PRECONDICIONES: Recibe una lista de numeros (enteros o decimales).
    POSCONDICIONES: Devuelve un entero o decimal (depende del tipo de
                    dato de la lista).
    """

    # Se declara y define la variable que recorrerá cada elemento en el bucle
    # while y la variable en la que se guardará el resultado final.
    elemento: int = 0
    menor: Union[int, float] = lista_de_numeros[0]

    # Caso trivial (1 elemento):
    # lista_de_numeros.len() = 1
    if (len(lista_de_numeros) == 1):

        return menor

    # Caso normal (más de 1 elemento):
    while (elemento < (len(lista_de_numeros) - 1)):

        if (menor > lista_de_numeros[elemento + 1]):

            menor = lista_de_numeros[elemento + 1]

        elemento += 1

    return menor


def ordenar_mayor_a_menor(uno: Union[int, float],
                          dos: Union[int, float],
                          tres: Union[int, float]) -> list:
    """
    Esta función recibe tres números y los retorna en una lista, ordenados de
    mayor a menor.
    PRECONDICIONES: Recibe 3 números (enteros o decimales).
    POSCONDICIONES: Devuelve una lista de enteros o decimales (depende de los
                    números ingresados).
    """

    # Se declara y define la variable en la que se guardará el resutlado
    # final
    resultado: list = [0, 0, 0]

    # Casos en que los tres numeros son distintos.
    if (uno > dos) and (uno > tres):

        resultado[0] = uno

        if (dos > tres):

            resultado[1] = dos
            resultado[2] = tres

        else:

            resultado[1] = tres
            resultado[2] = dos

    elif (dos > uno) and (dos > tres):

        resultado[0] = dos

        if (uno > tres):

            resultado[1] = uno
            resultado[2] = tres

        else:

            resultado[1] = tres
            resultado[2] = uno

    elif (tres > uno) and (tres > dos):

        resultado[0] = tres

        if (uno > dos):

            resultado[1] = uno
            resultado[2] = dos

        else:

            resultado[1] = dos
            resultado[2] = uno

    else:  # Caso en que dos o tres elementos sean iguales

        if (uno == dos) and (dos == tres):

            resultado = uno

        else:

            numeros: list = [uno, dos, tres]

            mayor: Union[int, float] = encontrar_mayor(numeros)
            menor: Union[int, float] = encontrar_menor(numeros)

            i: int = 0

            for elem in numeros:

                if elem == mayor:

                    i += 1

            if (i == 2):

                resultado[0] = mayor
                resultado[1] = mayor
                resultado[2] = menor

            else:

                resultado[0] = mayor
                resultado[1] = menor
                resultado[2] = menor

    return resultado


def ordenar_menor_a_mayor(uno: Union[int, float],
                          dos: Union[int, float],
                          tres: Union[int, float]) -> list:
    """
    Esta función recibe tres números y los retorna en una lista, ordenados de
    menor a mayor.
    PRECONDICIONES: Recibe 3 números (enteros o decimales).
    POSCONDICIONES: Devuelve una lista de enteros o decimales (depende de los
                    números ingresados).
    """

    # Reutilizo el código de la función ordenar_mayor_a_menor
    # pero al terminar invierto el orden de la lista.
    resultado: list = ordenar_mayor_a_menor(uno, dos, tres)

    resultado.reverse()

    return resultado


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    # Se imprime el título del ejercicio:
    print("\nEjercicio 6: Ordenar 3 valores\n")

    # Se declara y define una variable en la que se guardará la decisión del
    # usuario, si quiere ordenar de menor a mayor o al revés.
    mayor_a_menor: bool = None

    # En el ciclo while se verifica que el usuario ingrese un valor válido
    # para decidir cómo ordenar la lista de números que ingrese más adelante.
    while mayor_a_menor is None:

        print("¿Cómo quiere ordenar los 3 valores?")
        print("1: Mayor a menor")
        print("2: Menor a mayor")

        # Se prueba que el usuario ingrese un valor válido.
        try:

            entrada: int = int(input("Ingrese su respuesta: "))

            if (entrada == 1):

                mayor_a_menor = True

            elif (entrada == 2):

                mayor_a_menor = False

            else:

                print("Debe ingresar un valor válido (1 o 2).\n")

                mayor_a_menor = None

        # Se ataja posible error en el input.
        except ValueError as exc:

            print("Debe ingresar un valor válido (1 o 2).\n")

            # Se reinicia la variable para que se repita el ciclo e ingrese
            # correctamente el valor.
            mayor_a_menor = None

    # Se declara y define la variable que indica el número a ingresar.
    elemento: int = 0

    # Se declara y define la lista que guardará los valores ingresados por
    # el usuario. Primero se los define con valores 'None' para que sean
    # verificados en el ciclo while.
    lista_de_numeros: List[float] = [None, None, None]

    # Se ingresan los datos de los tres números a ordenar.
    while (elemento < 3):

        while lista_de_numeros[elemento] is None:

            # Se prueba que el usuario ingrese un valor válido.
            try:

                # Se define el mensaje del input en una variable para cumplir
                # con pycodestyle.
                msj_entrada: str = f"Ingrese número {elemento + 1}: "

                lista_de_numeros[elemento] = float(input(msj_entrada))

            # Se ataja el error al ingresar un valor incorrecto.
            except ValueError as exc:

                print("Error: Valor no válido, intente nuevamente.")

                lista_de_numeros[elemento] = None

        elemento += 1

    # Según la decisión que haya ingresado el usuario, el programa ordenará
    # de menor a mayor o al revés.
    if mayor_a_menor:

        resultado: list = ordenar_mayor_a_menor(lista_de_numeros[0],
                                                lista_de_numeros[1],
                                                lista_de_numeros[2])

    else:

        resultado: list = ordenar_menor_a_mayor(lista_de_numeros[0],
                                                lista_de_numeros[1],
                                                lista_de_numeros[2])

    # Se imprime el resultado final.
    print(f"El resultado es: {resultado}")


if __name__ == "__main__":
    principal()
