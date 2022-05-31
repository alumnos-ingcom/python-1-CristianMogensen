################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Números positivos y negativos
"""



def signo(numero):
    """
    Retorna el signo del numero ingresado.
    - (1) es positivo
    - (-1) es negativo
    - (0) es cero
    """

    resultado = 0
    
    if numero > 0:
        resultado += 1 #Si es positivo, le sumo 1 al resultado a devolver.
    elif numero < 0:
        resultado -= 1 #Si es negativo, le resto 1 al resultado a devolver.
        
    return resultado


def principal():
    """
    Escribir una función que reciba un número e indique si el mismo es
    positivo, negativo o cero utilizando sumas y restas.
    """
    
    #
    # PRECONDICIONES: Ingreso de números, sean decimales o enteros.
    #
    # POSCONDICIONES: Retorna números enteros (-1, 0 o 1).
    #    
    
    #Pruebo la funcion con los 3 posibles casos de prueba:
    
    #-- Positivo:
    n = 20
    print(f"El numero {n} es positivo, la funcion signo({n}) retorna: {signo(n)}.")
    
    #-- Negativo:
    n = -30
    print(f"El numero {n} es negativo, la funcion signo({n}) retorna: {signo(n)}.")
    
    #-- Cero:
    n = 0
    print(f"El numero {n} es cero, la funcion signo({n}) retorna: {signo(n)}.")
    
    pass

if __name__ == "__main__":
    principal()