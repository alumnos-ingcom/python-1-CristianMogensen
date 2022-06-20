################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
7. Transformación de un número
"""

def sexadecimal_a_decimal(horas, minutos, segundos):
    """
    Convierte un número en sexadecimal (horas, minutos, segundos)
    a decimal.
    """
    resultado = segundos + 60*minutos + 60*60*horas
    
    return resultado

def decimal_a_sexadecimal(numero):
    """
    Convierte un número en decimal en sexadecimal
    (horas, minutos, segundos).
    """
    cociente = numero // 3600
    resto = numero % 3600
    
    horas = cociente
    
    cociente = resto // 60
    resto = resto % 60
    
    minutos = cociente
    segundos = resto
    
    return (horas, minutos, segundos)    

def principal():
    """
    Escribir un programa que permita transformar un número solicitado
    expresado en grados, minutos y segundos a segundos a segundos. Y
    otra que haga el cambio en el sentido contrario, devolviendo una tuple.

    Recuerden que un grado son 60 minutos y un minuto son 60 segundos.
    """
    print(decimal_a_sexadecimal(3600 + 60 + 5))
    print(sexadecimal_a_decimal(1, 1, 5))

if __name__ == "__main__":
    principal()
