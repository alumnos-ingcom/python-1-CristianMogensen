################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest

from src.Ejercicio1 import convertir_a_fahrenheit, convertir_a_centigrados


"""
Tests del ejercicio 1.
Defino 6 casos de prueba en total.
"""


def test_conversion_centigrados_a_fahrenheit_positivos():
    """
    Test para verificar el resultado de la conversion con números positivos.
    """
    numero = 100.0
    resultado = convertir_a_fahrenheit(numero)
    assert (isinstance(resultado, int) or isinstance(resultado, float)), "El resultado debe ser un número decimal."
    assert resultado > 0, "El resultado debe ser mayor que cero."
    assert resultado == 212.0, "El resultado obtenido no es el esperado."


def test_conversion_centigrados_a_fahrenheit_negativos():
    """
    Test para verificar el resultado de la conversion con números negativos.
    """
    numero = -100.0
    resultado = convertir_a_fahrenheit(numero)
    assert (isinstance(resultado, int) or isinstance(resultado, float)), "El resultado debe ser un número decimal."
    assert resultado < 0, "El resultado debe ser menor que cero."
    assert resultado == -148.0, "El resultado obtenido no es el esperado."


def test_conversion_centigrados_a_fahrenheit_cero():
    """
    Test para verificar el resultado de la conversion con números negativos.
    """
    numero = 0.0
    resultado = convertir_a_fahrenheit(numero)
    assert (isinstance(resultado, int) or isinstance(resultado, float)), "El resultado debe ser un número decimal."
    assert resultado > 0, "El resultado debe ser mayor que cero."
    assert resultado == 32.0, "El resultado obtenido no es el esperado."


def test_conversion_fahrenheit_a_centigrados_positivos():
    """
    Test para verificar el resultado de la conversion con números positivos.
    """
    numero = 50.0
    resultado = convertir_a_fahrenheit(numero)
    assert (isinstance(resultado, int) or isinstance(resultado, float)), "El resultado debe ser un número decimal."
    assert resultado > 0, "El resultado debe ser mayor que cero."
    assert resultado == 10.0, "El resultado obtenido no es el esperado."


def test_conversion_fahrenheit_a_centigrados_negativos():
    """
    Test para verificar el resultado de la conversion con números negativos.
    """
    numero = -100.0
    resultado = convertir_a_fahrenheit(numero)
    assert (isinstance(resultado, int) or isinstance(resultado, float)), "El resultado debe ser un número decimal."
    assert resultado < 0, "El resultado debe ser menor que cero."
    assert resultado == (-100-32)*5/9, "El resultado obtenido no es el esperado."


def test_conversion_fahrenheit_a_centigrados_cero():
    """
    Test para verificar el resultado de la conversion con números negativos.
    """
    numero = 0.0
    resultado = convertir_a_fahrenheit(numero)
    assert (isinstance(resultado, int) or isinstance(resultado, float)), "El resultado debe ser un número decimal."
    assert resultado < 0, "El resultado debe ser mayor que cero."
    assert resultado == -32*5/9, "El resultado obtenido no es el esperado."
