################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################


import pytest


from src.ejercicio6 import encontrar_mayor, encontrar_menor
from src.ejercicio6 import ordenar_mayor_a_menor, ordenar_menor_a_mayor


"""
Tests del Ejercicio 6: Ordenar 3 valores

Se buscan testear 2 casos de prueba para la función encontrar_mayor, 2 casos
de prueba para la función encontrar_mayor, 9 casos de prueba para la función
ordenar_mayor_a_menor y 9 casos de prueba para la función
ordenar_menor_a_mayor:

encontrar_mayor(lista_de_numeros: list):
1- lista con 1 elemento. Resultado esperado: numero
2- lista con 3 elementos. Resultado esperado: mayor

encontrar_menor(lista_de_numeros: list):
1- lista con 1 elemento. Resultado esperado: numero
2- lista con 3 elementos. Resultado esperado: menor

ordenar_mayor_a_menor(uno: Union[int, float],
                      dos: Union[int, float],
                      tres: Union[int, float]):
1- uno > dos > tres. Resultado esperado: [uno, dos, tres]
2- uno > tres > dos. Resultado esperado: [uno, tres, dos]
3- dos > uno > tres. Resultado esperado: [dos, uno, tres]
4- dos > tres > uno. Resultado esperado: [dos, tres, uno]
5- tres > uno > dos. Resultado esperado: [tres, uno, dos]
6- tres > dos > uno. Resultado esperado: [tres, dos, uno]
7- uno = tres = dos. Resultado esperado: [uno, dos, tres]
8- uno = tres > dos. Resultado esperado: [uno, tres, dos]
9- uno > tres = dos. Resultado esperado: [uno, dos, tres]

ordenar_menor_a_mayor(uno: Union[int, float],
                      dos: Union[int, float],
                      tres: Union[int, float]):
1- uno > dos > tres. Resultado esperado: [tres, dos, uno]
2- uno > tres > dos. Resultado esperado: [dos, tres, uno]
3- dos > uno > tres. Resultado esperado: [tres, uno, dos]
4- dos > tres > uno. Resultado esperado: [uno, tres, dos]
5- tres > uno > dos. Resultado esperado: [dos, uno, tres]
6- tres > dos > uno. Resultado esperado: [uno, dos, tres]
7- uno = tres = dos. Resultado esperado: [tres, dos, uno]
8- uno = tres > dos. Resultado esperado: [dos, tres, uno]
9- uno > tres = dos. Resultado esperado: [tres, dos, uno]
"""


def test_encontrar_mayor_1_elemento():
    """
    Test función encontrar_mayor(lista_de_numeros)
    Caso de prueba 1:
    - Entrada: lista_de_numeros = [5]
    - Resultado esperado: resultado = 5
    """

    # Input para función a testear.
    lista_de_numeros: list = [5]

    resultado: int = encontrar_mayor(lista_de_numeros)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == 5), error_msj


def test_encontrar_mayor_mas_de_1_elemento():
    """
    Test función encontrar_mayor(lista_de_numeros)
    Caso de prueba 2:
    - Entrada: lista_de_numeros = [5, 25, 11]
    - Resultado esperado: resultado = 25
    """

    # Input para función a testear.
    lista_de_numeros: list = [5, 25, 11]

    resultado: int = encontrar_mayor(lista_de_numeros)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == 25), error_msj


def test_encontrar_menor_1_elemento():
    """
    Test función encontrar_menor(lista_de_numeros)
    Caso de prueba 1:
    - Entrada: lista_de_numeros = [5]
    - Resultado esperado: resultado = 5
    """

    # Input para función a testear.
    lista_de_numeros: list = [5]

    resultado: int = encontrar_menor(lista_de_numeros)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == 5), error_msj


def test_encontrar_menor_mas_de_1_elemento():
    """
    Test función encontrar_menor(lista_de_numeros)
    Caso de prueba 2:
    - Entrada: lista_de_numeros = [5, 25, 11]
    - Resultado esperado: resultado = 25
    """

    # Input para función a testear.
    lista_de_numeros: list = [5, 25, 11]

    resultado: int = encontrar_menor(lista_de_numeros)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == 5), error_msj


def test_ordenar_mayor_a_menor_caso_1():
    """
    Test función ordenar_mayor_a_menor(uno, dos, tres)
    Caso de prueba 1:
    - Entrada: uno = 9
               dos = 6
               tres = 3
    - Resultado esperado: resultado = [uno, dos, tres]
    """

    # Input para función a testear.
    uno: int = 9
    dos: int = 6
    tres: int = 3

    resultado: list = ordenar_mayor_a_menor(uno, dos, tres)

    # Resultado esperado.
    esperado: list = [uno, dos, tres]

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == esperado), error_msj


def test_ordenar_mayor_a_menor_caso_2():
    """
    Test función ordenar_mayor_a_menor(uno, dos, tres)
    Caso de prueba 2:
    - Entrada: uno = 10
               dos = 5
               tres = 9
    - Resultado esperado: resultado = [uno, tres, dos]
    """

    # Input para función a testear.
    uno: int = 10
    dos: int = 5
    tres: int = 9

    resultado: list = ordenar_mayor_a_menor(uno, dos, tres)

    # Resultado esperado.
    esperado: list = [uno, tres, dos]

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == esperado), error_msj


def test_ordenar_mayor_a_menor_caso_3():
    """
    Test función ordenar_mayor_a_menor(uno, dos, tres)
    Caso de prueba 3:
    - Entrada: uno = 22
               dos = 25
               tres = 3
    - Resultado esperado: resultado = [dos, uno, tres]
    """

    # Input para función a testear.
    uno: int = 22
    dos: int = 25
    tres: int = 3

    resultado: list = ordenar_mayor_a_menor(uno, dos, tres)

    # Resultado esperado.
    esperado: list = [dos, uno, tres]

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == esperado), error_msj


def test_ordenar_mayor_a_menor_caso_4():
    """
    Test función ordenar_mayor_a_menor(uno, dos, tres)
    Caso de prueba 4:
    - Entrada: uno = 15
               dos = 19
               tres = 17
    - Resultado esperado: resultado = [dos, tres, uno]
    """

    # Input para función a testear.
    uno: int = 15
    dos: int = 19
    tres: int = 17

    resultado: list = ordenar_mayor_a_menor(uno, dos, tres)

    # Resultado esperado.
    esperado: list = [dos, tres, uno]

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == esperado), error_msj


def test_ordenar_mayor_a_menor_caso_5():
    """
    Test función ordenar_mayor_a_menor(uno, dos, tres)
    Caso de prueba 5:
    - Entrada: uno = 14
               dos = 2
               tres = 17
    - Resultado esperado: resultado = [tres, uno, dos]
    """

    # Input para función a testear.
    uno: int = 14
    dos: int = 2
    tres: int = 17

    resultado: list = ordenar_mayor_a_menor(uno, dos, tres)

    # Resultado esperado.
    esperado: list = [tres, uno, dos]

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == esperado), error_msj


def test_ordenar_mayor_a_menor_caso_6():
    """
    Test función ordenar_mayor_a_menor(uno, dos, tres)
    Caso de prueba 6:
    - Entrada: uno = 1
               dos = 24
               tres = 30
    - Resultado esperado: resultado = [tres, dos, uno]
    """

    # Input para función a testear.
    uno: int = 1
    dos: int = 24
    tres: int = 30

    resultado: list = ordenar_mayor_a_menor(uno, dos, tres)

    # Resultado esperado.
    esperado: list = [tres, dos, uno]

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == esperado), error_msj


def test_ordenar_mayor_a_menor_caso_7():
    """
    Test función ordenar_mayor_a_menor(uno, dos, tres)
    Caso de prueba 7:
    - Entrada: uno = 7
               dos = 7
               tres = 7
    - Resultado esperado: resultado = [uno, dos, tres]
    """

    # Input para función a testear.
    uno: int = 7
    dos: int = uno
    tres: int = uno

    resultado: list = ordenar_mayor_a_menor(uno, dos, tres)

    # Resultado esperado.
    esperado: list = [uno, dos, tres]

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == esperado), error_msj


def test_ordenar_mayor_a_menor_caso_8():
    """
    Test función ordenar_mayor_a_menor(uno, dos, tres)
    Caso de prueba 8:
    - Entrada: uno = 5
               dos = 1
               tres = 5
    - Resultado esperado: resultado = [uno, tres, dos]
    """

    # Input para función a testear.
    uno: int = 5
    dos: int = 1
    tres: int = 5

    resultado: list = ordenar_mayor_a_menor(uno, dos, tres)

    # Resultado esperado.
    esperado: list = [uno, tres, dos]

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == esperado), error_msj


def test_ordenar_mayor_a_menor_caso_9():
    """
    Test función ordenar_mayor_a_menor(uno, dos, tres)
    Caso de prueba 9:
    - Entrada: uno = 23
               dos = 11
               tres = 11
    - Resultado esperado: resultado = [uno, dos, tres]
    """

    # Input para función a testear.
    uno: int = 23
    dos: int = 11
    tres: int = 11

    resultado: list = ordenar_mayor_a_menor(uno, dos, tres)

    # Resultado esperado.
    esperado: list = [uno, dos, tres]

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == esperado), error_msj


def test_ordenar_menor_a_mayor_caso_1():
    """
    Test función ordenar_menor_a_mayor(uno, dos, tres)
    Caso de prueba 1:
    - Entrada: uno = 9
               dos = 6
               tres = 3
    - Resultado esperado: resultado = [tres, dos, uno]
    """

    # Input para función a testear.
    uno: int = 9
    dos: int = 6
    tres: int = 3

    resultado: list = ordenar_menor_a_mayor(uno, dos, tres)

    # Resultado esperado.
    esperado: list = [tres, dos, uno]

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == esperado), error_msj


def test_ordenar_menor_a_mayor_caso_2():
    """
    Test función ordenar_menor_a_mayor(uno, dos, tres)
    Caso de prueba 2:
    - Entrada: uno = 10
               dos = 5
               tres = 9
    - Resultado esperado: resultado = [dos, tres, uno]
    """

    # Input para función a testear.
    uno: int = 10
    dos: int = 5
    tres: int = 9

    resultado: list = ordenar_menor_a_mayor(uno, dos, tres)

    # Resultado esperado.
    esperado: list = [dos, tres, uno]

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == esperado), error_msj


def test_ordenar_menor_a_mayor_caso_3():
    """
    Test función ordenar_menor_a_mayor(uno, dos, tres)
    Caso de prueba 3:
    - Entrada: uno = 22
               dos = 25
               tres = 3
    - Resultado esperado: resultado = [tres, uno, dos]
    """

    # Input para función a testear.
    uno: int = 22
    dos: int = 25
    tres: int = 3

    resultado: list = ordenar_menor_a_mayor(uno, dos, tres)

    # Resultado esperado.
    esperado: list = [tres, uno, dos]

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == esperado), error_msj


def test_ordenar_menor_a_mayor_caso_4():
    """
    Test función ordenar_menor_a_mayor(uno, dos, tres)
    Caso de prueba 4:
    - Entrada: uno = 15
               dos = 19
               tres = 17
    - Resultado esperado: resultado = [uno, tres, dos]
    """

    # Input para función a testear.
    uno: int = 15
    dos: int = 19
    tres: int = 17

    resultado: list = ordenar_menor_a_mayor(uno, dos, tres)

    # Resultado esperado.
    esperado: list = [uno, tres, dos]

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == esperado), error_msj


def test_ordenar_menor_a_mayor_caso_5():
    """
    Test función ordenar_menor_a_mayor(uno, dos, tres)
    Caso de prueba 5:
    - Entrada: uno = 14
               dos = 2
               tres = 17
    - Resultado esperado: resultado = [dos, uno, tres]
    """

    # Input para función a testear.
    uno: int = 14
    dos: int = 2
    tres: int = 17

    resultado: list = ordenar_menor_a_mayor(uno, dos, tres)

    # Resultado esperado.
    esperado: list = [dos, uno, tres]

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == esperado), error_msj


def test_ordenar_menor_a_mayor_caso_6():
    """
    Test función ordenar_menor_a_mayor(uno, dos, tres)
    Caso de prueba 6:
    - Entrada: uno = 1
               dos = 24
               tres = 30
    - Resultado esperado: resultado = [uno, dos, tres]
    """

    # Input para función a testear.
    uno: int = 1
    dos: int = 24
    tres: int = 30

    resultado: list = ordenar_menor_a_mayor(uno, dos, tres)

    # Resultado esperado.
    esperado: list = [uno, dos, tres]

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == esperado), error_msj


def test_ordenar_menor_a_mayor_caso_7():
    """
    Test función ordenar_menor_a_mayor(uno, dos, tres)
    Caso de prueba 7:
    - Entrada: uno = 7
               dos = 7
               tres = 7
    - Resultado esperado: resultado = [tres, dos, uno]
    """

    # Input para función a testear.
    uno: int = 7
    dos: int = uno
    tres: int = uno

    resultado: list = ordenar_menor_a_mayor(uno, dos, tres)

    # Resultado esperado.
    esperado: list = [tres, dos, uno]

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == esperado), error_msj


def test_ordenar_menor_a_mayor_caso_8():
    """
    Test función ordenar_menor_a_mayor(uno, dos, tres)
    Caso de prueba 8:
    - Entrada: uno = 5
               dos = 1
               tres = 5
    - Resultado esperado: resultado = [dos, tres, uno]
    """

    # Input para función a testear.
    uno: int = 5
    dos: int = 1
    tres: int = 5

    resultado: list = ordenar_menor_a_mayor(uno, dos, tres)

    # Resultado esperado.
    esperado: list = [dos, tres, uno]

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == esperado), error_msj


def test_ordenar_menor_a_mayor_caso_9():
    """
    Test función ordenar_menor_a_mayor(uno, dos, tres)
    Caso de prueba 9:
    - Entrada: uno = 23
               dos = 11
               tres = 11
    - Resultado esperado: resultado = [tres, dos, uno]
    """

    # Input para función a testear.
    uno: int = 23
    dos: int = 11
    tres: int = 11

    resultado: list = ordenar_menor_a_mayor(uno, dos, tres)

    # Resultado esperado.
    esperado: list = [tres, dos, uno]

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == esperado), error_msj
