################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest

from src.Ejercicio3 import compara


"""
Test del ejercicio 3.
Defino 3 casos de prueba en total.
"""


def test_compara_mayor_menor():
    """
    Testeo el caso en que el primero es mayor que el segundo.
    """
    N1 = 8
    N2 = 3
    resultado = compara(N1, N2)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado > 0, "El resultado debe ser mayor que cero."
    assert resultado == 1, "El resultado obtenido no es el esperado."


def test_compara_mayor_menor():
    """
    Testeo el caso en que el primero es mayor que el segundo.
    """
    N1 = 5
    N2 = 6
    resultado = compara(N1, N2)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado < 0, "El resultado debe ser menor que cero."
    assert resultado == -1, "El resultado obtenido no es el esperado."


def test_compara_iguales():
    """
    Testeo el caso en que el primero es mayor que el segundo.
    """
    N1 = 3
    N2 = 3
    resultado = compara(N1, N2)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado == 0, "El resultado obtenido no es el esperado."
