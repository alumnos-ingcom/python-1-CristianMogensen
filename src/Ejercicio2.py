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
    
    #Declaro y defino variables auxiliares:
    resultado = 0
    modulo = abs(numero)
    aux = numero
    contador = 0
    
    if (numero != 0):
        #Si el numero es cero, el resultado será 0
        #y no hará falta que entre en el bucle.
        
        resultado = -1
        
        #En el bucle while verifico que el número sea positivo.
        #Si no lo es, el resultado del bucle while no realizará cambios
        #en la variable resultado y, por lo tanto, el mismoserá -1
        #(definido anteriormente) y querrá decir que el número es negativo.
        while (contador <= modulo):
            
            aux -= 1
            contador += 1
            
            if (aux == 1):
                #Si es positivo, en los últimos pasos del bucle se debe
                #cumplir la condición (aux == 1) y la variable resultado
                #cambiará a 1, saliendo del bucle con el break.
                resultado = 1
                break
    
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
    
    entrada = int(input("Ingrese número: "))
    print(f"Signo de {entrada}: {signo(entrada)}")


if __name__ == "__main__":
    principal()