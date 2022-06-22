################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################


import pytest


from src.ejercicio4 import suma_lenta


"""
Tests del Ejercicio 4: Suma lenta

Se buscan testear 11 casos de prueba para la función suma_lenta:

suma_lenta(numero: int, otro_numero: int):
1- numero > 0, otro_numero > 0. Resultado esperado: resultado > 0
2- numero > 0, otro_numero < 0. Resultado esperado: resultado > 0
3- numero > 0, otro_numero < 0. Resultado esperado: resultado < 0
4- numero < 0, otro_numero > 0. Resultado esperado: resultado > 0
5- numero < 0, otro_numero > 0. Resultado esperado: resultado < 0
6- numero < 0, otro_numero < 0. Resultado esperado: resultado < 0
7- numero = 0, otro_numero = 0. Resultado esperado: resultado = 0
8- numero > 0, otro_numero = 0. Resultado esperado: resultado = numero (>0)
9- numero < 0, otro_numero = 0. Resultado esperado: resultado = numero (<0)
10- numero = 0, otro_numero > 0. Res. esperado: resultado = otro_numero(>0)
11- numero = 0, otro_numero < 0. Res. esperado: resultado = otro_numero(<0)
"""


def test_suma_lenta_caso_1():
    """
    Test función suma_lenta(numero, otro_numero)
    Caso de prueba 1:
    - Entrada: numero = 10
               otro_numero = 20
    - Resultado esperado: resultado = 30
    """

    # Input para función a testear.
    numero: int = 10
    otro_numero: int = 20

    resultado: int = suma_lenta(numero, otro_numero)

    # Defino el primer mensaje de error (muy largo para pycodestyle):
    error1_msj: str = "El resultado debe ser un número entero."
    assert (isinstance(resultado, int)), error1_msj

    assert (resultado > 0), "El resultado debe ser mayor que cero."

    # Defino el tercer mensaje de error (muy largo para pycodestyle):
    error3_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == numero + otro_numero), error3_msj


def test_suma_lenta_caso_2():
    """
    Test función suma_lenta(numero, otro_numero)
    Caso de prueba 2:
    - Entrada: numero = 11
               otro_numero = -5
    - Resultado esperado: resultado = 6
    """

    # Input para función a testear.
    numero: int = 11
    otro_numero: int = -5

    resultado: int = suma_lenta(numero, otro_numero)

    # Defino el primer mensaje de error (muy largo para pycodestyle):
    error1_msj: str = "El resultado debe ser un número entero."
    assert (isinstance(resultado, int)), error1_msj

    assert (resultado > 0), "El resultado debe ser mayor que cero."

    # Defino el tercer mensaje de error (muy largo para pycodestyle):
    error3_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == numero + otro_numero), error3_msj


def test_suma_lenta_caso_3():
    """
    Test función suma_lenta(numero, otro_numero)
    Caso de prueba 3:
    - Entrada: numero = 5
               otro_numero = -15
    - Resultado esperado: resultado = -10
    """

    # Input para función a testear.
    numero: int = 5
    otro_numero: int = -15

    resultado: int = suma_lenta(numero, otro_numero)

    # Defino el primer mensaje de error (muy largo para pycodestyle):
    error1_msj: str = "El resultado debe ser un número entero."
    assert (isinstance(resultado, int)), error1_msj

    assert (resultado < 0), "El resultado debe ser menor que cero."

    # Defino el tercer mensaje de error (muy largo para pycodestyle):
    error3_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == numero + otro_numero), error3_msj


def test_suma_lenta_caso_4():
    """
    Test función suma_lenta(numero, otro_numero)
    Caso de prueba 4:
    - Entrada: numero = -5
               otro_numero = 10
    - Resultado esperado: resultado = 5
    """

    # Input para función a testear.
    numero: int = -5
    otro_numero: int = 10

    resultado: int = suma_lenta(numero, otro_numero)

    # Defino el primer mensaje de error (muy largo para pycodestyle):
    error1_msj: str = "El resultado debe ser un número entero."
    assert (isinstance(resultado, int)), error1_msj

    assert (resultado > 0), "El resultado debe ser mayor que cero."

    # Defino el tercer mensaje de error (muy largo para pycodestyle):
    error3_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == numero + otro_numero), error3_msj


def test_suma_lenta_caso_5():
    """
    Test función suma_lenta(numero, otro_numero)
    Caso de prueba 5:
    - Entrada: numero = -9
               otro_numero = 3
    - Resultado esperado: resultado = -6
    """

    # Input para función a testear.
    numero: int = -9
    otro_numero: int = 3

    resultado: int = suma_lenta(numero, otro_numero)

    # Defino el primer mensaje de error (muy largo para pycodestyle):
    error1_msj: str = "El resultado debe ser un número entero."
    assert (isinstance(resultado, int)), error1_msj

    assert (resultado < 0), "El resultado debe ser menor que cero."

    # Defino el tercer mensaje de error (muy largo para pycodestyle):
    error3_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == numero + otro_numero), error3_msj


def test_suma_lenta_caso_6():
    """
    Test función suma_lenta(numero, otro_numero)
    Caso de prueba 6:
    - Entrada: numero = -9
               otro_numero = -3
    - Resultado esperado: resultado = -12
    """

    # Input para función a testear.
    numero: int = -9
    otro_numero: int = -3

    resultado: int = suma_lenta(numero, otro_numero)

    # Defino el primer mensaje de error (muy largo para pycodestyle):
    error1_msj: str = "El resultado debe ser un número entero."
    assert (isinstance(resultado, int)), error1_msj

    assert (resultado < 0), "El resultado debe ser menor que cero."

    # Defino el tercer mensaje de error (muy largo para pycodestyle):
    error3_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == numero + otro_numero), error3_msj


def test_suma_lenta_caso_7():
    """
    Test función suma_lenta(numero, otro_numero)
    Caso de prueba 7:
    - Entrada: numero = 0
               otro_numero = 0
    - Resultado esperado: resultado = 0
    """

    # Input para función a testear.
    numero: int = 0
    otro_numero: int = 0

    resultado: int = suma_lenta(numero, otro_numero)

    # Defino el primer mensaje de error (muy largo para pycodestyle):
    error1_msj: str = "El resultado debe ser un número entero."
    assert (isinstance(resultado, int)), error1_msj

    # Defino el tercer mensaje de error (muy largo para pycodestyle):
    error3_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == numero + otro_numero), error3_msj


def test_suma_lenta_caso_8():
    """
    Test función suma_lenta(numero, otro_numero)
    Caso de prueba 8:
    - Entrada: numero = 8
               otro_numero = 0
    - Resultado esperado: resultado = 8
    """

    # Input para función a testear.
    numero: int = 8
    otro_numero: int = 0

    resultado: int = suma_lenta(numero, otro_numero)

    # Defino el primer mensaje de error (muy largo para pycodestyle):
    error1_msj: str = "El resultado debe ser un número entero."
    assert (isinstance(resultado, int)), error1_msj

    assert (resultado > 0), "El resultado debe ser mayor que cero."

    # Defino el tercer mensaje de error (muy largo para pycodestyle):
    error3_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == numero + otro_numero), error3_msj


def test_suma_lenta_caso_9():
    """
    Test función suma_lenta(numero, otro_numero)
    Caso de prueba 9:
    - Entrada: numero = -4
               otro_numero = 0
    - Resultado esperado: resultado = -4
    """

    # Input para función a testear.
    numero: int = -4
    otro_numero: int = 0

    resultado: int = suma_lenta(numero, otro_numero)

    # Defino el primer mensaje de error (muy largo para pycodestyle):
    error1_msj: str = "El resultado debe ser un número entero."
    assert (isinstance(resultado, int)), error1_msj

    assert (resultado < 0), "El resultado debe ser menor que cero."

    # Defino el tercer mensaje de error (muy largo para pycodestyle):
    error3_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == numero + otro_numero), error3_msj


def test_suma_lenta_caso_10():
    """
    Test función suma_lenta(numero, otro_numero)
    Caso de prueba 10:
    - Entrada: numero = 0
               otro_numero = 12
    - Resultado esperado: resultado = 12
    """

    # Input para función a testear.
    numero: int = 0
    otro_numero: int = 12

    resultado: int = suma_lenta(numero, otro_numero)

    # Defino el primer mensaje de error (muy largo para pycodestyle):
    error1_msj: str = "El resultado debe ser un número entero."
    assert (isinstance(resultado, int)), error1_msj

    assert (resultado > 0), "El resultado debe ser mayor que cero."

    # Defino el tercer mensaje de error (muy largo para pycodestyle):
    error3_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == numero + otro_numero), error3_msj


def test_suma_lenta_caso_11():
    """
    Test función suma_lenta(numero, otro_numero)
    Caso de prueba 11:
    - Entrada: numero = 0
               otro_numero = -7
    - Resultado esperado: resultado = -7
    """

    # Input para función a testear.
    numero: int = 0
    otro_numero: int = -7

    resultado: int = suma_lenta(numero, otro_numero)

    # Defino el primer mensaje de error (muy largo para pycodestyle):
    error1_msj: str = "El resultado debe ser un número entero."
    assert (isinstance(resultado, int)), error1_msj

    assert (resultado < 0), "El resultado debe ser menor que cero."

    # Defino el tercer mensaje de error (muy largo para pycodestyle):
    error3_msj: str = "El resultado obtenido no es el esperado."
    assert (resultado == numero + otro_numero), error3_msj
