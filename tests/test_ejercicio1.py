################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################


import pytest


from src.ejercicio1 import convertir_a_fahrenheit, convertir_a_centigrados


"""
Tests del Ejercicio 1:Conversión de temperaturas

Se buscan testear 3 casos de prueba para la función convertir_a_fahrenheit y
3 para la función convertir_a_centigrados:

convertir_a_fahrenheit(grados_centigrados: float):
1 - grados_centigrados > 0. Resultado esperado: float
2 - grados_centigrados < 0. Resultado esperado: float
3 - grados_centigrados = 0. Resultado esperado: float

convertir_a_centigrados(grados_fahrenheit: float):
1 - grados_fahrenheit > 0. Resultado esperado: float
2 - grados_fahrenheit < 0. Resultado esperado: float
3 - grados_fahrenheit = 0. Resultado esperado: float
"""


def test_convertir_centigrados_a_fahrenheit_positivos():
    """
    Test función convertir_a_centigrados(grados_centigrados)
    Caso de prueba 1:
    - Entrada: grados_centigrados = 100.0
    - Resultado esperado: resultado = 212.0
    """

    # Input para función a testear.
    grados_centigrados: float = 100.0

    resultado: float = convertir_a_fahrenheit(grados_centigrados)

    # Defino el primer mensaje de error (muy largo para pycodestyle):
    error1_msj: str = "El resultado debe ser un número decimal."
    assert (isinstance(resultado, int)
            or isinstance(resultado, float)), error1_msj

    assert (resultado > 0), "El resultado debe ser mayor que cero."

    assert (resultado == 212.0), "El resultado obtenido no es el esperado."


def test_convertir_centigrados_a_fahrenheit_negativos():
    """
    Test función convertir_a_centigrados(grados_centigrados)
    Caso de prueba 2:
    - Entrada: grados_centigrados = -100.0
    - Resultado esperado: resultado = -148.0
    """

    # Input para función a testear.
    grados_centigrados = -100.0

    resultado: float = convertir_a_fahrenheit(grados_centigrados)

    # Defino el primer mensaje de error (muy largo para pycodestyle):
    error1_msj: str = "El resultado debe ser un número decimal."
    assert (isinstance(resultado, int)
            or isinstance(resultado, float)), error1_msj

    assert (resultado < 0), "El resultado debe ser menor que cero."

    assert (resultado == -148.0), "El resultado obtenido no es el esperado."


def test_convertir_centigrados_a_fahrenheit_cero():
    """
    Test función convertir_a_centigrados(grados_centigrados)
    Caso de prueba 3:
    - Entrada: grados_centigrados = 0.0
    - Resultado esperado: resultado = 32.0
    """

    # Input para función a testear.
    grados_centigrados: float = 0.0

    resultado: float = convertir_a_fahrenheit(grados_centigrados)

    # Defino el primer mensaje de error (muy largo para pycodestyle):
    error1_msj: str = "El resultado debe ser un número decimal."
    assert (isinstance(resultado, int)
            or isinstance(resultado, float)), error1_msj

    assert (resultado > 0), "El resultado debe ser mayor que cero."

    assert (resultado == 32.0), "El resultado obtenido no es el esperado."


def test_convertir_fahrenheit_a_centigrados_positivos():
    """
    Test función convertir_a_centigrados(grados_fahrenheit)
    Caso de prueba 1:
    - Entrada: grados_fahrenheit = 50.0
    - Resultado esperado: resultado = 10.0
    """

    # Input para función a testear.
    grados_fahrenheit: float = 50.0

    resultado: float = convertir_a_centigrados(grados_fahrenheit)

    # Defino el primer mensaje de error (muy largo para pycodestyle):
    error1_msj: str = "El resultado debe ser un número decimal."
    assert (isinstance(resultado, int)
            or isinstance(resultado, float)), error1_msj

    assert (resultado > 0), "El resultado debe ser mayor que cero."

    assert (resultado == 10.0), "El resultado obtenido no es el esperado."


def test_convertir_fahrenheit_a_centigrados_negativos():
    """
    Test función convertir_a_centigrados(grados_fahrenheit)
    Caso de prueba 2:
    - Entrada: grados_fahrenheit = -4.0
    - Resultado esperado: resultado = -20.0
    """

    # Input para función a testear.
    grados_fahrenheit: float = -4.0

    resultado: float = convertir_a_centigrados(grados_fahrenheit)

    # Defino el primer mensaje de error (muy largo para pycodestyle):
    error1_msj: str = "El resultado debe ser un número decimal."
    assert (isinstance(resultado, int)
            or isinstance(resultado, float)), error1_msj

    assert (resultado < 0), "El resultado debe ser menor que cero."

    assert (resultado == -20.0), "El resultado obtenido no es el esperado."


def test_convertir_fahrenheit_a_centigrados_cero():
    """
    Test función convertir_a_centigrados(grados_fahrenheit)
    Caso de prueba 3:
    - Entrada: grados_fahrenheit = 0
    - Resultado esperado: resultado = -17.7778 (número periódico)
    """

    # Input para función a testear.
    grados_fahrenheit: float = 0.0

    resultado: float = convertir_a_centigrados(grados_fahrenheit)

    # Defino el primer mensaje de error (muy largo para pycodestyle):
    error1_msj: str = "El resultado debe ser un número decimal."
    assert (isinstance(resultado, int)
            or isinstance(resultado, float)), error1_msj

    assert (resultado < 0), "El resultado debe ser menor que cero."

    # Defino el primer mensaje de error (muy largo para pycodestyle):
    error2_msj: str = "El resultado debe ser un número decimal."
    assert ((resultado > -17.8) and (resultado < -17.7)), error2_msj
