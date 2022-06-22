################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################


import pytest


from src.ejercicio11 import es_multiplo


"""
Tests del Ejercicio 11: Multiplos de

Se buscan testear 2 casos de prueba para la función es_multiplo:

es_multiplo(numero: int, multiplo: int):
1- numero = 6, multiplo = 3. Resultado esperado: True
2- numero = 10, multiplo = 6. Resultado esperado: False
"""


def test_es_multiplo_true():
    """
    Test función es_multiplo(numero, multiplo)
    Caso de prueba 1:
    - Entrada: numero = 6
               multiplo = 3
    - Resultado esperado: resultado = True
    """

    # Input para función a testear.
    numero: int = 6
    multiplo: int = 3

    resultado: bool = es_multiplo(numero, multiplo)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado is True), error_msj


def test_es_multiplo_false():
    """
    Test función es_multiplo(numero, multiplo)
    Caso de prueba 2:
    - Entrada: numero = 10
               multiplo = 6
    - Resultado esperado: resultado = False
    """

    # Input para función a testear.
    numero: int = 10
    multiplo: int = 6

    resultado: bool = es_multiplo(numero, multiplo)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado is False), error_msj
