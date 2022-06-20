################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
6. Ordenar 3 valores
"""

def encontrar_mayor(lista_de_numeros):
    """
    Dada una lista de numeros, encuentra el mayor de todos
    los numeros pertenecientes a la misma.
    """
    
    elemento = 0
    mayor = lista_de_numeros[0]
    
    #Caso trivial (1 elemento):
    #lista_de_numeros.len() = 1
    if (len(lista_de_numeros) == 1):
        return mayor
    
    #Caso normal (más de 1 elemento):
    while (elemento < (len(lista_de_numeros) - 1)):
        if (mayor < lista_de_numeros[elemento + 1]):
            mayor = lista_de_numeros[elemento + 1]
        elemento += 1
    
    return mayor

def encontrar_menor(lista_de_numeros):
    """
    Dada una lista de numeros, encuentra el menor de todos
    los numeros pertenecientes a la misma.
    """
    
    elemento = 0
    menor = lista_de_numeros[0]
    
    #Caso trivial (1 elemento):
    #lista_de_numeros.len() = 1
    if (len(lista_de_numeros) == 1):
        return menor
    
    #Caso normal (más de 1 elemento):
    while (elemento < (len(lista_de_numeros) - 1)):
        if (menor > lista_de_numeros[elemento + 1]):
            menor = lista_de_numeros[elemento + 1]
        elemento += 1
    
    return menor
        

def ordenar_mayor_a_menor(uno, dos, tres):
    """
    Dados 3 numeros, retorna una lista ordenada de
    mayor a menor.
    """
    
    resultado = [0, 0, 0]
    
    #Casos en que sos los tres numeros distintos
    if (uno > dos) and (uno > tres):
        resultado[0] = uno
        if (dos > tres):
            resultado[1] = dos
            resultado[2] = tres
        else:
            resultado[1] = tres
            resultado[2] = dos
    elif (dos > uno) and (dos > tres):
        resultado[0] = dos
        if (uno > tres):
            resultado[1] = uno
            resultado[2] = tres
        else:
            resultado[1] = tres
            resultado[2] = uno
    elif (tres > uno) and (tres > dos):
        resultado[0] = tres
        if (uno > dos):
            resultado[1] = uno
            resultado[2] = dos
        else:
            resultado[1] = dos
            resultado[2] = uno
    else: #Caso en que dos o tres elementos sean iguales
        if (uno == dos) and (dos == tres):
            resultado = uno
        else:
            numeros = [uno, dos, tres]
            mayor = encontrar_mayor(numeros)
            menor = encontrar_menor(numeros)
            
            i = 0
            for elem in numeros:
                if elem == mayor:
                    i += 1
            
            if (i == 2):
                resultado[0] = mayor
                resultado[1] = mayor
                resultado[2] = menor
            else:
                resultado[0] = mayor
                resultado[1] = menor
                resultado[2] = menor
    
    return resultado
    
    
def ordenar_menor_a_mayor(uno, dos, tres):
    """
    Dados 3 numeros, retorna una lista ordenada de
    mayor a menor.
    """
    
    #Reutilizo el código de la función ordenar_mayor_a_menor
    #pero al terminar invierto el orden de la lista.
    
    resultado = [0, 0, 0]
    
    #Casos en que sos los tres numeros distintos
    if (uno > dos) and (uno > tres):
        resultado[0] = uno
        if (dos > tres):
            resultado[1] = dos
            resultado[2] = tres
        else:
            resultado[1] = tres
            resultado[2] = dos
    elif (dos > uno) and (dos > tres):
        resultado[0] = dos
        if (uno > tres):
            resultado[1] = uno
            resultado[2] = tres
        else:
            resultado[1] = tres
            resultado[2] = uno
    elif (tres > uno) and (tres > dos):
        resultado[0] = tres
        if (uno > dos):
            resultado[1] = uno
            resultado[2] = dos
        else:
            resultado[1] = dos
            resultado[2] = uno
    else: #Caso en que dos o tres elementos sean iguales
        if (uno == dos) and (dos == tres):
            resultado = uno
        else:
            numeros = [uno, dos, tres]
            mayor = encontrar_mayor(numeros)
            menor = encontrar_menor(numeros)
            
            i = 0
            for elem in numeros:
                if elem == mayor:
                    i += 1
            
            if (i == 2):
                resultado[0] = mayor
                resultado[1] = mayor
                resultado[2] = menor
            else:
                resultado[0] = mayor
                resultado[1] = menor
                resultado[2] = menor
    
    resultado.reverse()
    
    return resultado

def principal():
    """
    Escribir una función que a partir de tres variables de tipo entero
    retorne una tupla con dichos valores ordenados de menor a mayor.
    (Y viceversa)
    """
    
    print(ordenar_menor_a_mayor(1,9,-5))

if __name__ == "__main__":
    principal()
