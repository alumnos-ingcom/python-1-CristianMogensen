################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
5. Divisiones
"""

def division_lenta(dividendo, divisor):
    """
    Realiza la division entre dos numeros (dividendo, divisor)
    mediante restas sucesivas.
    Devuelve una tupla con (cociente, resto)
    """
    
    cociente = 0
    #Cuenta las veces que el divisor 'entra' en el dividendo,
    #para finalmente determinar el cociente final.
    
    resto = dividendo
    #Determina el resto de la división.
    
    #Importo la función signo del ejercicio 2,
    #para verificar que los signos del divisor y dividendo
    #sean iguales:
    from Ejercicio2 import signo
    
    #Importo la función de suma_lenta para reemplazar la suma
    from Ejercicio4 import suma_lenta
    
    if (signo(dividendo) == signo(divisor)):
        while (abs(resto) >= abs(divisor)):
            #cociente += 1
            #resto -= divisor
            
            cociente = suma_lenta(cociente, 1)
            resto = suma_lenta(resto, -divisor)
    else:
        while (abs(resto) >= abs(divisor)):
            #cociente -= 1
            #resto += divisor
            
            cociente = suma_lenta(cociente, -1)
            resto = suma_lenta(resto, divisor)
    
    #Defino la tupla a retornar por la función:
    resultado = (cociente, resto)
    
    return resultado


def principal():
    """
    Escribir una función que mediante restas sucesivas, obtenga
    el valor del cociente y resto de dos números enteros.
    """
    
    #
    # PRECONDICIONES: Ingreso de números enteros o decimales (dividendo y divisor).
    #
    # POSCONDICIONES: Retorna una tupla con números enteros y/o entero y
    #                 decimal (resultado de la división).
    #
    
    # Pruebo 6 casos posibles de prueba:
    print("División lenta, pruebas:")
    print("CASO\t\t\t\tSIGNOS\t\tTIPOS\t\tRESULTADO")
    
    # dividendo > divisor, positivos, enteros:
    NUM = 11
    DIV = 5
    RES = division_lenta(NUM, DIV)
    print(f"dividendo({NUM}) > divisor({DIV}),\tpositivos,\tenteros:\t{RES}")
    
    # dividendo < divisor, positivos, enteros:
    NUM = 7
    DIV = 10
    RES = division_lenta(NUM, DIV)
    print(f"dividendo({NUM}) < divisor({DIV}),\tpositivos,\tenteros:\t{RES}")
    
    # dividendo = divisor, positivos, enteros:
    NUM = 10
    DIV = 10
    RES = division_lenta(NUM, DIV)
    print(f"dividendo({NUM}) = divisor({DIV}),\tpositivos,\tenteros:\t{RES}")
    
    # dividendo > divisor, negativos, enteros:
    NUM = -2
    DIV = -4
    RES = division_lenta(NUM, DIV)
    print(f"dividendo({NUM}) > divisor({DIV}),\tnegativos,\tenteros:\t{RES}")
    
    # dividendo < divisor, negativos, enteros:
    NUM = -16
    DIV = -3
    RES = division_lenta(NUM, DIV)
    print(f"dividendo({NUM}) < divisor({DIV}),\tnegativos,\tenteros:\t{RES}")
    
    # dividendo = divisor, negativos, enteros:
    NUM = -10
    DIV = -10
    RES = division_lenta(NUM, DIV)
    print(f"dividendo({NUM}) > divisor({DIV}),\tnegativos,\tenteros:\t{RES}")
    
    # dividendo > divisor, intercambiados, enteros:
    NUM = 10
    DIV = -3
    RES = division_lenta(NUM, DIV)
    print(f"dividendo({NUM}) > divisor({DIV}),\tintercambiados,\tenteros:\t{RES}")
    
    # dividendo < divisor, intercambiados, enteros:
    NUM = -10
    DIV = 3
    RES = division_lenta(NUM, DIV)
    print(f"dividendo({NUM}) < divisor({DIV}),\tintercambiados,\tenteros:\t{RES}")


if __name__ == "__main__":
    principal()
