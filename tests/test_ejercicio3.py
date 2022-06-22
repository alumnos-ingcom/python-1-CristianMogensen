################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import pytest

from src.ejercicio3 import compara


"""
Tests del Ejercicio 3: Comparación de números

Se buscan testear 3 casos de prueba para la función compara:

compara(numero: int, otro_numero: int):
1- numero > otro_numero. Resultado esperado: 1
2- numero < otro_numero. Resultado esperado: -1
3- numero = otro_numero. Resultado esperado: 0
"""


def test_compara_primer_numero_mayor():
    """
    Test función compara(numero, otro_numero)
    Caso de prueba 1:
    - Entrada: numero = 33
               otro_numero = 22
    - Resultado esperado: resultado = 1
    """

    # Entrada para probar en la función:
    numero: int = 33
    otro_numero: int = 22

    resultado: int = compara(numero, otro_numero)

    # Defino el primer mensaje de error (muy largo para pycodestyle):
    error1_msj: str = "El resultado debe ser un número entero."
    assert (isinstance(resultado, int)), error1_msj

    assert (resultado > 0), "El resultado debe ser mayor que cero."

    assert (resultado == 1), "El resultado obtenido no es el esperado."


def test_compara_primer_numero_menor():
    """
    Test función compara(numero, otro_numero)
    Caso de prueba 2:
    - Entrada: numero = 11
               otro_numero = 33
    - Resultado esperado: resultado = -1
    """

    # Entrada para probar en la función:
    numero: int = 11
    otro_numero: int = 33

    resultado: int = compara(numero, otro_numero)

    # Defino el primer mensaje de error (muy largo para pycodestyle):
    error1_msj: str = "El resultado debe ser un número entero."
    assert (isinstance(resultado, int)), error1_msj

    assert (resultado < 0), "El resultado debe ser mayor que cero."

    assert (resultado == -1), "El resultado obtenido no es el esperado."


def test_compara_numeros_iguales():
    """
    Test función compara(numero, otro_numero)
    Caso de prueba 3:
    - Entrada: numero = 22
               otro_numero = 22
    - Resultado esperado: resultado = 0
    """

    # Entrada para probar en la función:
    numero: int = 22
    otro_numero: int = 22

    resultado: int = compara(numero, otro_numero)

    # Defino el primer mensaje de error (muy largo para pycodestyle):
    error1_msj: str = "El resultado debe ser un número entero."
    assert (isinstance(resultado, int)), error1_msj

    assert (resultado == 0), "El resultado obtenido no es el esperado."
