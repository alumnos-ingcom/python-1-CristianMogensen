################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
11. Multiplos de
"""

def es_multiplo(numero, multiplo):
    """
    Dados los argumentos (numero, multiplo), analiza si numero
    es múltiplo de multiplo.
    """
    
    from Ejercicio5 import division_lenta
    #Importo la funcion division_lenta del ejercicio 5, que utiliza
    #solamente sumas y restas.
    
    EsMultiplo = False
    div = division_lenta(numero, multiplo)
    
    if (div[1] == 0):
        EsMultiplo = True
    
    return EsMultiplo

def principal():
    """
    Escribir una función que indique con True si un número
    entero es multiplo de otro, utilizando sumas y restas.
    """
    num = int(input("Ingrese numero: "))
    mul = int(input("Ingrese multiplo: "))
    
    print(f"Son múltiplos? {es_multiplo(num, mul)}")

if __name__ == "__main__":
    principal()