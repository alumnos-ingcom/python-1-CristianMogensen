################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
4. Suma lenta
"""

def suma_lenta(numero, otro_numero):
    """
    Realiza la suma de numero y otro_numero en pasos de 1 unidad.
    Ejemplo: 4+3 = 4+1+1+1 = 7
    """
    
    contador = abs(otro_numero)
    resultado = numero
    
    #Importo la función signo del ejercicio 2
    from Ejercicio2 import signo
    
    #Determina si la unidad a sumar es positiva o negativa:
    unidad = signo(otro_numero)

    #Suma o resta de a 1 unidad:
    while (contador > 0):
        resultado += unidad
        contador -= 1
        
    return resultado


def principal():
    """
    Escribir una función que haga la suma entre dos números enteros sin hacer
    la operación de manera directa. Esto quiere decir que para hacer la suma
    entre 4 y 3, las operaciones resultantes deberán ser 4+1+1+1.

    La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.
    """
    
    #
    # PRECONDICIONES: Ingreso de números enteros (numero y otro_numero).
    #
    # POSCONDICIONES: Retorna un número entero (resultado de la suma).
    #
    
    #Imprimo título:
    print("Suma lenta:")
    
    N1 = int(input("Ingrese numero1: "))
    N2 = int(input("Ingrese numero2: "))
    
    print(f"{N1} + {N2} = {suma_lenta(N1, N2)}")


if __name__ == "__main__":
    principal()