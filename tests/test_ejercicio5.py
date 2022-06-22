################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################


import pytest


from src.ejercicio5 import division_lenta


"""
Tests del Ejercicio 4: Suma lenta

Se buscan testear 8 casos de prueba para la función division_lenta:

division_lenta(dividendo: Union[int, float], divisor: Union[int, float]):
1- dividendo > divisor, positivos, enteros
2- dividendo < divisor, positivos, enteros
3- dividendo = divisor, positivos, enteros
4- dividendo > divisor, negativos, enteros
5- dividendo < divisor, negativos, enteros
6- dividendo = divisor, negativos, enteros
7- dividendo > divisor, intercambiados, enteros
8- dividendo < divisor, intercambiados, enteros
"""


def test_division_lenta_caso_1():
    """
    Test función division_lenta(dividendo, divisor)
    Caso de prueba 1:
    - Entrada: dividendo = 25
               divisor = 5
    - Resultado esperado: resultado = (5, 0)
    """

    # Input para función a testear.
    dividendo: int = 26
    divisor: int = 5

    resultado: int = division_lenta(dividendo, divisor)

    # Resultados esperados.
    cociente: int = dividendo // divisor
    resto: int = dividendo % divisor

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == (cociente, resto)), error_msj


def test_division_lenta_caso_2():
    """
    Test función division_lenta(dividendo, divisor)
    Caso de prueba 2:
    - Entrada: dividendo = 5
               divisor = 10
    - Resultado esperado: resultado = (0, 5)
    """

    # Input para función a testear.
    dividendo: int = 5
    divisor: int = 10

    resultado: int = division_lenta(dividendo, divisor)

    # Resultados esperados.
    cociente: int = dividendo // divisor
    resto: int = dividendo % divisor

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == (cociente, resto)), error_msj


def test_division_lenta_caso_3():
    """
    Test función division_lenta(dividendo, divisor)
    Caso de prueba 3:
    - Entrada: dividendo = 20
               divisor = 20
    - Resultado esperado: resultado = (1, 0)
    """

    # Input para función a testear.
    dividendo: int = 20
    divisor: int = 20

    resultado: int = division_lenta(dividendo, divisor)

    # Resultados esperados.
    cociente: int = dividendo // divisor
    resto: int = dividendo % divisor

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == (cociente, resto)), error_msj


def test_division_lenta_caso_4():
    """
    Test función division_lenta(dividendo, divisor)
    Caso de prueba 4:
    - Entrada: dividendo = -25
               divisor = -5
    - Resultado esperado: resultado = (-5, 0)
    """

    # Input para función a testear.
    dividendo: int = -27
    divisor: int = -5

    resultado: int = division_lenta(dividendo, divisor)

    # Resultados esperados.
    cociente: int = dividendo // divisor
    resto: int = dividendo % divisor

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == (cociente, resto)), error_msj


def test_division_lenta_caso_5():
    """
    Test función division_lenta(dividendo, divisor)
    Caso de prueba 5:
    - Entrada: dividendo = -101
               divisor = -10
    - Resultado esperado: resultado = (10, -1)
    """

    # Input para función a testear.
    dividendo: int = -101
    divisor: int = -10

    resultado: int = division_lenta(dividendo, divisor)

    # Resultados esperados.
    cociente: int = dividendo // divisor
    resto: int = dividendo % divisor

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == (cociente, resto)), error_msj


def test_division_lenta_caso_6():
    """
    Test función division_lenta(dividendo, divisor)
    Caso de prueba 6:
    - Entrada: dividendo = -7
               divisor = -7
    - Resultado esperado: resultado = (1, 0)
    """

    # Input para función a testear.
    dividendo: int = -7
    divisor: int = -7

    resultado: int = division_lenta(dividendo, divisor)

    # Resultados esperados.
    cociente: int = dividendo // divisor
    resto: int = dividendo % divisor

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == (cociente, resto)), error_msj


def test_division_lenta_caso_7():
    """
    Test función division_lenta(dividendo, divisor)
    Caso de prueba 7:
    - Entrada: dividendo = 25
               divisor = -6
    - Resultado esperado: resultado = (-4, 1)
    """

    # Input para función a testear.
    dividendo: int = 25
    divisor: int = -6

    resultado: int = division_lenta(dividendo, divisor)

    # Resultados esperados.
    cociente: int = -4
    resto: int = 1

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == (cociente, resto)), error_msj


def test_division_lenta_caso_8():
    """
    Test función division_lenta(dividendo, divisor)
    Caso de prueba 8:
    - Entrada: dividendo = -9
               divisor = 4
    - Resultado esperado: resultado = (-2, -1)
    """

    # Input para función a testear.
    dividendo: int = -9
    divisor: int = 4

    resultado: int = division_lenta(dividendo, divisor)

    # Resultados esperados.
    cociente: int = -2
    resto: int = -1

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == (cociente, resto)), error_msj
