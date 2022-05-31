################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
10. Palíndromo
"""

def es_par(numero):
    """
    Retorna True o False si es par o impar.
    """
    
    EsPar = False
    
    if ((numero % 2) == 0):
        EsPar = True
    
    return EsPar

def es_palindromo(texto):
    """
    Analiza el texto o palabra ingresado y retorna True o False
    si se trata de un palíndromo o no.
    """
    EsPalindromo = True
    elem = 0
    
    if (es_par(len(texto))):
        while (elem < len(texto)//2):
            if (texto[elem] != texto[(len(texto)-1 - elem)]):
                EsPalindromo = False
                break
            elem += 1
    else:
        while (elem < (len(texto)//2 + 1)):
            if (texto[elem] != texto[(len(texto)-1 - elem)]):
                EsPalindromo = False
                break
            elem += 1
    
    return EsPalindromo

def principal():
    """
    Escribir una función que indique con True si una palabra
    o frase ingresada se trata de un palindromo. Palíndromo,
    es si se lee igual de derecha a izquierda que de izquierda
    a derecha.
    """
    entrada = str(input("Ingrese palabra: "))
    print(f"La palabra {entrada} es un palíndromo? {es_palindromo(entrada)}")

if __name__ == "__main__":
    principal()