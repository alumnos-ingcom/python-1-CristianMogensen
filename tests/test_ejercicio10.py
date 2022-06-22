################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################


import pytest


from src.ejercicio10 import es_par, es_palindromo


"""
Tests del Ejercicio 10: Palíndromo

Se buscan testear 5 casos de prueba para la función es_par y 2 casos de prueba
para la función es_palindromo:

es_par(numero: int):
1- numero = 0. Resultado esperado: True
2- numero = 1. Resultado esperado: False
3- numero = 2. Resultado esperado: True
4- numero = 5. Resultado esperado: False
5- numero = 8. Resultado esperado: True

es_palindromo(texto: str):
1- texto = neuquen. Resultado esperado: True
2- texto = hola. Resultado esperado: False
"""


def test_es_par_caso_1():
    """
    Test función es_par(numero)
    Caso de prueba 1:
    - Entrada: numero = 0
    - Resultado esperado: resultado = True
    """

    # Input para función a testear.
    numero: int = 0

    resultado: bool = es_par(numero)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado is True), error_msj


def test_es_par_caso_2():
    """
    Test función es_par(numero)
    Caso de prueba 2:
    - Entrada: numero = 1
    - Resultado esperado: resultado = False
    """

    # Input para función a testear.
    numero: int = 1

    resultado: bool = es_par(numero)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado is False), error_msj


def test_es_par_caso_3():
    """
    Test función es_par(numero)
    Caso de prueba 3:
    - Entrada: numero = 2
    - Resultado esperado: resultado = True
    """

    # Input para función a testear.
    numero: int = 2

    resultado: bool = es_par(numero)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado is True), error_msj


def test_es_par_caso_4():
    """
    Test función es_par(numero)
    Caso de prueba 4:
    - Entrada: numero = 5
    - Resultado esperado: resultado = False
    """

    # Input para función a testear.
    numero: int = 5

    resultado: bool = es_par(numero)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado is False), error_msj


def test_es_par_caso_5():
    """
    Test función es_par(numero)
    Caso de prueba 5:
    - Entrada: numero = 8
    - Resultado esperado: resultado = True
    """

    # Input para función a testear.
    numero: int = 8

    resultado: bool = es_par(numero)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado is True), error_msj


def test_es_palindromo_true():
    """
    Test función es_palindromo(texto)
    Caso de prueba 1:
    - Entrada: texto = neuquen
    - Resultado esperado: resultado = True
    """

    # Input para función a testear.
    texto: str = "neuquen"

    resultado: bool = es_palindromo(texto)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado is True), error_msj


def test_es_palindromo_false():
    """
    Test función es_palindromo(texto)
    Caso de prueba 2:
    - Entrada: texto = hola
    - Resultado esperado: resultado = False
    """

    # Input para función a testear.
    texto: str = "hola"

    resultado: bool = es_palindromo(texto)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado is False), error_msj
