################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
9. Factores Primos
"""

def factores_primos(numero):
    """
    Analiza los factores primos de un numero y los retorna
    como tupla. (n1, n2, ...)
    """
    from Ejercicio8 import es_primo
    
    resultado = (1,)
    modulo = abs(numero)
    
    if (numero == 0):
        return None
    elif (es_primo(modulo)):
        if (modulo > 1):
            resultado += (modulo,)
    else:
        i = 2
        while (i < modulo):
            #Chequeo si es divisible por i.
            if ((modulo % i) == 0):
                resultado += (i,)
            i += 1
    
    return resultado

def principal():
    """
    Escribir una función que retorne una tuple con factores
    primos de un numero entero positivo.
    """
    entrada = int(input("Ingrese numero: "))
    print(f"Sus factores primos son: {factores_primos(entrada)}")

if __name__ == "__main__":
    principal()
