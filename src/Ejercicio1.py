################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
1. Conversión de temperaturas
"""


def convertir_a_fahrenheit(centigrados):
    """
    Convierte grados fahrenheit a grados centígrados.
    """
    resultado_fahrenheit = (centigrados * 9/5) + 32
    return resultado_fahrenheit

def convertir_a_centigrados(fahrenheit):
    """
    Convierte grados centígrados a grados fahrenheit.
    """
    resultado_centigrados = (fahrenheit - 32) * 5/9
    return resultado_centigrados


def principal():
    """
    Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa.

    Escribir las funciones para convertir la temperatura en grados centigrados en fahrenheit como un número decimal, utilice esta formula para calcular los grados centígrados y retorne el resultado obtenido. Y viceversa.
    """
    
    #
    # PRECONDICIONES: Ingreso de números decimales (grados) y un caracter (string) para indicar el tipo de grado.
    #
    # POSCONDICIONES: Retorna números decimales.
    #    
    
    print("Conversor de grados: centigrados <-> fahrenheit")
    
    TipoDeGrados = '' #Declaro y defino la variable que indicará el tipo de grados que ingresará el usuario.
    
    while (TipoDeGrados != 'c' and TipoDeGrados != 'f' and TipoDeGrados != 'C' and TipoDeGrados != 'F'):
        #Verifico que se indique correctamente el tipo de grados a ingresar.
        
        #El usuario ingresa el caracter que indica el tipo de grados que ingresará:
        TipoDeGrados = str(input("Indique tipo de grados a ingresar (c:centigrados / f:fahrenheit): "))
    
    #El usuario ingresa la cantidad de grados a convertir:
    grados = float(input("Ingrese cantidad de grados: "))
    
    #Dependiendo del tipo de grados ingresado se convierte a °C o °F.
    if TipoDeGrados == 'f' or TipoDeGrados == 'F':
        grados_convertidos = convertir_a_centigrados(grados)
        grado = 'C'
    if TipoDeGrados == 'c' or TipoDeGrados == 'C':
        grados_convertidos = convertir_a_fahrenheit(grados)
        grado = 'F'
    
    #Imprimo resultado
    print(f"{grados} °{TipoDeGrados.upper()} = {grados_convertidos} °{grado}")
    
    pass

if __name__ == "__main__":
    principal()