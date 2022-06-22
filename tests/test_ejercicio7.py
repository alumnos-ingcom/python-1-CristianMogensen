################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################


import pytest


from src.ejercicio7 import sexadecimal_a_decimal, decimal_a_sexadecimal


"""
Tests del Ejercicio 7: Transformación de un número

Se buscan testear 4 casos de prueba para la función sexadecimal_a_decimal y
4 para la función decimal_a_sexadecimal:

sexadecimal_a_decimal(horas: int, minutos: int, segundos: int):
1- horas = 1. Resultado esperado: 3600
2- minutos = 1. Resultado esperado: 60
3- segundos = 1. Resultado esperado: 1
4- horas = 3, minutos = 33, segundos = 5. Resultado esperado: 12785

decimal_a_sexadecimal(numero: int):
1- numero = 3600. Resultado esperado: (1, 0, 0)
2- numero = 60. Resultado esperado: (0, 1, 0)
3- numero = 1. Resultado esperado: (0, 0, 1)
4- numero = 12785. Resultado esperado: (3, 33, 5)
"""


def test_sexadecimal_a_decimal_caso_1():
    """
    Test función sexadecimal_a_decimal(horas, minutos, segundos)
    Caso de prueba 1:
    - Entrada: horas = 1
               minutos = 0
               segundos = 0
    - Resultado esperado: resultado = 3600
    """

    # Input para función a testear.
    horas: int = 1
    minutos: int = 0
    segundos: int = 0

    resultado: int = sexadecimal_a_decimal(horas, minutos, segundos)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == 3600), error_msj


def test_sexadecimal_a_decimal_caso_2():
    """
    Test función sexadecimal_a_decimal(horas, minutos, segundos)
    Caso de prueba 2:
    - Entrada: horas = 0
               minutos = 1
               segundos = 0
    - Resultado esperado: resultado = 60
    """

    # Input para función a testear.
    horas: int = 0
    minutos: int = 1
    segundos: int = 0

    resultado: int = sexadecimal_a_decimal(horas, minutos, segundos)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == 60), error_msj


def test_sexadecimal_a_decimal_caso_3():
    """
    Test función sexadecimal_a_decimal(horas, minutos, segundos)
    Caso de prueba 3:
    - Entrada: horas = 0
               minutos = 0
               segundos = 1
    - Resultado esperado: resultado = 1
    """

    # Input para función a testear.
    horas: int = 0
    minutos: int = 0
    segundos: int = 1

    resultado: int = sexadecimal_a_decimal(horas, minutos, segundos)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == 1), error_msj


def test_sexadecimal_a_decimal_caso_4():
    """
    Test función sexadecimal_a_decimal(horas, minutos, segundos)
    Caso de prueba 4:
    - Entrada: horas = 3
               minutos = 33
               segundos = 5
    - Resultado esperado: resultado = 12785
    """

    # Input para función a testear.
    horas: int = 3
    minutos: int = 33
    segundos: int = 5

    resultado: int = sexadecimal_a_decimal(horas, minutos, segundos)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == 12785), error_msj


def test_decimal_a_sexadecimal_caso_1():
    """
    Test función decimal_a_sexadecimal(horas, minutos, segundos)
    Caso de prueba 1:
    - Entrada: numero = 3600
    - Resultado esperado: resultado = (1, 0, 0)
    """

    # Input para función a testear.
    numero: int = 3600

    resultado: int = decimal_a_sexadecimal(numero)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == (1, 0, 0)), error_msj


def test_decimal_a_sexadecimal_caso_2():
    """
    Test función decimal_a_sexadecimal(horas, minutos, segundos)
    Caso de prueba 2:
    - Entrada: numero = 60
    - Resultado esperado: resultado = (0, 1, 0)
    """

    # Input para función a testear.
    numero: int = 60

    resultado: int = decimal_a_sexadecimal(numero)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == (0, 1, 0)), error_msj


def test_decimal_a_sexadecimal_caso_3():
    """
    Test función decimal_a_sexadecimal(horas, minutos, segundos)
    Caso de prueba 3:
    - Entrada: horas = 0
               minutos = 0
               segundos = 1
    - Resultado esperado: resultado = (0, 0, 1)
    """

    # Input para función a testear.
    numero: int = 1

    resultado: int = decimal_a_sexadecimal(numero)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == (0, 0, 1)), error_msj


def test_decimal_a_sexadecimal_caso_4():
    """
    Test función decimal_a_sexadecimal(horas, minutos, segundos)
    Caso de prueba 4:
    - Entrada: numero = 12785
    - Resultado esperado: resultado = (3, 33, 5)
    """

    # Input para función a testear.
    numero: int = 12785

    resultado: int = decimal_a_sexadecimal(numero)

    # Defino el mensaje de error (muy largo para pycodestyle):
    error_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == (3, 33, 5)), error_msj
