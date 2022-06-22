################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################


import pytest


from src.ejercicio9 import factores_primos


"""
Tests del Ejercicio 9: Factores Primos

Se buscan testear 7 casos de prueba para la función factores_primos:

factores_primos(numero: int):
1- numero = 0. Resultado esperado: None
2- numero = 1. Resultado esperado: (1,)
3- numero = 2. Resultado esperado: (1, 2)
4- numero = 3. Resultado esperado: (1, 3)
5- numero = 4. Resultado esperado: (1, 2, 2)
6- numero = 24. Resultado esperado: (1, 2, 2, 2, 3)
6- numero = 53. Resultado esperado: (1, 53)
"""


def test_factores_primos_caso_1():
    """
    Test función factores_primos(numero)
    Caso de prueba 1:
    - Entrada: numero = 0
    - Resultado esperado: resultado = None
    """

    # Input para función a testear.
    numero: int = 0

    resultado: tuple = factores_primos(numero)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado is None), error_msj


def test_factores_primos_caso_2():
    """
    Test función factores_primos(numero)
    Caso de prueba 2:
    - Entrada: numero = 1
    - Resultado esperado: resultado = (1,)
    """

    # Input para función a testear.
    numero: int = 1

    resultado: tuple = factores_primos(numero)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == (1,)), error_msj


def test_factores_primos_caso_3():
    """
    Test función factores_primos(numero)
    Caso de prueba 3:
    - Entrada: numero = 2
    - Resultado esperado: resultado = (1, 2)
    """

    # Input para función a testear.
    numero: int = 2

    resultado: tuple = factores_primos(numero)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == (1, 2)), error_msj


def test_factores_primos_caso_4():
    """
    Test función factores_primos(numero)
    Caso de prueba 4:
    - Entrada: numero = 3
    - Resultado esperado: resultado = (1, 3)
    """

    # Input para función a testear.
    numero: int = 3

    resultado: tuple = factores_primos(numero)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == (1, 3)), error_msj


def test_factores_primos_caso_5():
    """
    Test función factores_primos(numero)
    Caso de prueba 5:
    - Entrada: numero = 4
    - Resultado esperado: resultado = (1, 2, 2)
    """

    # Input para función a testear.
    numero: int = 4

    resultado: tuple = factores_primos(numero)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == (1, 2, 2)), error_msj


def test_factores_primos_caso_6():
    """
    Test función factores_primos(numero)
    Caso de prueba 6:
    - Entrada: numero = 24
    - Resultado esperado: resultado = (1, 2, 2, 2, 3)
    """

    # Input para función a testear.
    numero: int = 24

    resultado: tuple = factores_primos(numero)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == (1, 2, 2, 2, 3)), error_msj


def test_factores_primos_caso_7():
    """
    Test función factores_primos(numero)
    Caso de prueba 7:
    - Entrada: numero = 53
    - Resultado esperado: resultado = (1, 53)
    """

    # Input para función a testear.
    numero: int = 53

    resultado: tuple = factores_primos(numero)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == (1, 53)), error_msj
