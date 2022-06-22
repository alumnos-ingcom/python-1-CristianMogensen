################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest

from src.ejercicio2 import signo


"""
Tests del Ejercicio 2: Números positivos y negativos

Se buscan testear 3 casos de prueba para la función signo:

signo(numero: int) -> int:
1- numero > 0. Resultado esperado: 1
2- numero = 0. Resultado esperado: 0
3- numero < 0. Resultado esperado: -1
"""


def test_signo_positivo():
    """
    Test función signo(numero)
    Caso de prueba 1:
    - Entrada: numero = 12
    - Resultado esperado: resultado = 1
    """

    # Entrada para probar en la función.
    numero: int = 12

    resultado: int = signo(numero)

    # Mensaje de error (string muy larga, uso de variable por pycodestyle).
    error_msj: str = "El resultado debe ser un número entero."
    assert (isinstance(resultado, int)), error_msj

    assert (resultado > 0), "El resultado debe ser mayor que cero."

    assert (resultado == 1), "El resultado obtenido no es el esperado."


def test_signo_nulo():
    """
    Test función signo(numero)
    Caso de prueba 2:
    - Entrada: numero = 0
    - Resultado esperado: resultado = 0
    """

    # Entrada para probar en la función.
    numero: int = 0

    resultado: int = signo(numero)

    # Mensaje de error (string muy larga, uso de variable por pycodestyle).
    error_msj: str = "El resultado debe ser un número entero."
    assert (isinstance(resultado, int)), error_msj

    assert (resultado == 0), "El resultado obtenido no es el esperado."


def test_signo_negativo():
    """
    Test función signo(numero)
    Caso de prueba 3:
    - Entrada: numero = -33
    - Resultado esperado: resultado = -1
    """

    # Entrada para probar en la función.
    numero: int = -33

    resultado: int = signo(numero)

    # Mensaje de error (string muy larga, uso de variable por pycodestyle).
    error_msj: str = "El resultado debe ser un número entero."
    assert (isinstance(resultado, int)), error_msj

    assert (resultado < 0), "El resultado debe ser menor que cero."

    assert (resultado == -1), "El resultado obtenido no es el esperado."
