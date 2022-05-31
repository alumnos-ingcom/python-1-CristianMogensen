################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
3. Comparación de números
"""

def compara(numero, otro_numero):
    """
    Compara dos numeros, retornando:
        
        - (-1) si el primero es menor que el segundo
        - (0) si son iguales
        - (1) si el primero es mayor que el segundo
    """
    
    #Reutilizo la funcion del ejercicio 2:
    from Ejercicio2 import signo
    comparacion = numero - otro_numero
    
    return signo(comparacion)


def principal():
    """
    Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:

        - Retornar -1 si el primero es menor que el segundo
        - Retornar 0 si son iguales
        - Retornar 1 si el primero es mayor que el segundo
    """
    
    #
    # PRECONDICIONES: Ingreso de números a comparar, sean decimales o enteros.
    #
    # POSCONDICIONES: Retorna números enteros (-1, 0 o 1).
    #    
    
    #Pruebo la funcion con los 3 casos de prueba posibles:
    
    #-- numero < otro_numero (resultado=-1)
    N1 = 5
    N2 = 6
    print(f"Dado {N1}<{N2} la funcion compara({N1},{N2}) retorna: {compara(N1,N2)}")
    
    #-- numero > otro_numero (resultado=1)
    N1 = 8
    N2 = 3
    print(f"Dado {N1}>{N2} la funcion compara({N1},{N2}) retorna: {compara(N1,N2)}")
    
    #-- numero == otro_numero (resultado=0)
    N1 = 3
    N2 = 3
    print(f"Dado {N1}={N2} la funcion compara({N1},{N2}) retorna: {compara(N1,N2)}")
    
    pass

if __name__ == "__main__":
    principal()