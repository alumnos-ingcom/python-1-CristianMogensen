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
    
    #Reutilizo la funcion signo del ejercicio 2:
    from Ejercicio2 import signo
    
    #Comparo ambos números y determino cuál es mayor
    #observando el signo final de la comparación.
    comparacion = numero - otro_numero
    
    return signo(comparacion)


def principal():
    """
    Escribir una función que utilizando sumas y restas,
    reciba dos valores y retorne:

        - Retornar -1 si el primero es menor que el segundo
        - Retornar 0 si son iguales
        - Retornar 1 si el primero es mayor que el segundo
    """
    
    #
    # PRECONDICIONES: Ingreso de números a comparar, sean decimales o enteros.
    #
    # POSCONDICIONES: Retorna números enteros (-1, 0 o 1).
    #    
    
    N1 = int(input("Ingrese numero1: "))
    N2 = int(input("Ingrese numero2: "))
    print(f"Resultado de comparación: {compara(N1, N2)}")


if __name__ == "__main__":
    principal()
