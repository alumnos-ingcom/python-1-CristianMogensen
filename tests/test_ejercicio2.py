################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest

from src.Ejercicio2 import signo


"""
Test del ejercicio 2.
Defino 5 casos de prueba en total.
"""


def test_signo_negativo_entero():
    """
    Testeo el signo negativo de la función, con
    número entero (int) en el input.
    """
    numero = -30
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado < 0, "El resultado debe ser menor que cero."
    assert resultado == -1, "El resultado obtenido no es el esperado."


def test_signo_negativo_float():
    """
    Testeo el signo negativo de la función, con
    número decimal (float) en el input.
    """
    numero = -15.55
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado < 0, "El resultado debe ser menor que cero."
    assert resultado == -1, "El resultado obtenido no es el esperado."


def test_signo_nulo():
    """
    Testeo el signo nulo o cero de la función.
    """
    numero = 0
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado == 0, "El resultado obtenido no es el esperado."


def test_signo_positivo_entero():
    """
    Testeo el signo positivo de la función, con
    número entero (int) en el input.
    """
    numero = 22.57
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado > 0, "El resultado debe ser menor que cero."
    assert resultado == 1, "El resultado obtenido no es el esperado."


def test_signo_positivo_float():
    """
    Testeo el signo positivo de la función, con
    número decimal (float) en el input.
    """
    numero = 22.57
    resultado = signo(numero)
    assert isinstance(resultado, int), "El resultado debe ser un número entero."
    assert resultado > 0, "El resultado debe ser menor que cero."
    assert resultado == 1, "El resultado obtenido no es el esperado."
