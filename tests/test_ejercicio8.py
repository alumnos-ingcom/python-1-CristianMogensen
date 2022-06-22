################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################


import pytest


from src.ejercicio8 import es_primo


"""
Tests del Ejercicio 8: Números primos

Se buscan testear 9 casos de prueba para la función es_primo:

es_primo(numero: int):
1- numero = 0. Resultado esperado: False
2- numero = 1. Resultado esperado: True
3- numero = 2. Resultado esperado: True
4- numero = 3. Resultado esperado: True
5- numero = 4. Resultado esperado: False
6- numero = 5. Resultado esperado: True
7- numero = 6. Resultado esperado: False
8- numero = 23. Resultado esperado: True
9- numero = 91. Resultado esperado: False
"""


def test_es_primo_caso_1():
    """
    Test función es_primo(numero)
    Caso de prueba 1:
    - Entrada: numero = 0
    - Resultado esperado: resultado = False
    """

    # Input para función a testear.
    numero: int = 0

    resultado: bool = es_primo(numero)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado is False), error_msj


def test_es_primo_caso_2():
    """
    Test función es_primo(numero)
    Caso de prueba 2:
    - Entrada: numero = 1
    - Resultado esperado: resultado = True
    """

    # Input para función a testear.
    numero: int = 1

    resultado: bool = es_primo(numero)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado is True), error_msj


def test_es_primo_caso_3():
    """
    Test función es_primo(numero)
    Caso de prueba 3:
    - Entrada: numero = 2
    - Resultado esperado: resultado = True
    """

    # Input para función a testear.
    numero: int = 2

    resultado: bool = es_primo(numero)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado is True), error_msj


def test_es_primo_caso_4():
    """
    Test función es_primo(numero)
    Caso de prueba 4:
    - Entrada: numero = 3
    - Resultado esperado: resultado = True
    """

    # Input para función a testear.
    numero: int = 3

    resultado: bool = es_primo(numero)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado is True), error_msj


def test_es_primo_caso_5():
    """
    Test función es_primo(numero)
    Caso de prueba 5:
    - Entrada: numero = 4
    - Resultado esperado: resultado = False
    """

    # Input para función a testear.
    numero: int = 4

    resultado: bool = es_primo(numero)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado is False), error_msj


def test_es_primo_caso_6():
    """
    Test función es_primo(numero)
    Caso de prueba 6:
    - Entrada: numero = 5
    - Resultado esperado: resultado = True
    """

    # Input para función a testear.
    numero: int = 5

    resultado: bool = es_primo(numero)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado is True), error_msj


def test_es_primo_caso_7():
    """
    Test función es_primo(numero)
    Caso de prueba 7:
    - Entrada: numero = 6
    - Resultado esperado: resultado = False
    """

    # Input para función a testear.
    numero: int = 6

    resultado: bool = es_primo(numero)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado is False), error_msj


def test_es_primo_caso_8():
    """
    Test función es_primo(numero)
    Caso de prueba 8:
    - Entrada: numero = 23
    - Resultado esperado: resultado = True
    """

    # Input para función a testear.
    numero: int = 23

    resultado: bool = es_primo(numero)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado is True), error_msj


def test_es_primo_caso_9():
    """
    Test función es_primo(numero)
    Caso de prueba 9:
    - Entrada: numero = 91
    - Resultado esperado: resultado = False
    """

    # Input para función a testear.
    numero: int = 91

    resultado: bool = es_primo(numero)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado is False), error_msj
