################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
8. Números primos
"""

def es_primo(numero):
    """
    Evalúa si el número es primo, retornando un booleano
    (True o False).
    """
        
    EsPrimo = True
    modulo = abs(numero)    
    i = 2
    
    if (modulo > 3):    
        while (i < modulo):
            #Chequeo si es divisible por i.
            if ((modulo % i) == 0):
                EsPrimo = False
                break
            i += 1
    else:
        if (modulo == 0):
            EsPrimo = False
        else:
            EsPrimo = True
    
    return EsPrimo
    
def principal():
    """
    Escribir una función que indique con True si un numero indicado es Primo.
    """
    entrada = int(input("Ingrese numero: "))
    print(f"Es primo? {es_primo(entrada)}")

if __name__ == "__main__":
    principal()