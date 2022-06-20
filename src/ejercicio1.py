################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
1. Conversión de temperaturas
Se quiere transformar temperaturas en grados fahrenheit a grados centígrados
y viceversa.

Escribir las funciones para convertir la temperatura en grados centigrados
en fahrenheit como un número decimal, utilice esta formula para calcular los
grados centígrados y retorne el resultado obtenido. Y viceversa.

def convertir_a_fahrenheit(centigrados):
def convertir_a_centigrados(fahrenheit):
"""


def convertir_a_fahrenheit(grados_centigrados: float) -> float:
    """
    Esta función convierte grados centígrados a grados fahrenheit.
    PRECONDICIONES: Recibe un float (grados_centigrados).
    POSCONDICIONES: Devuelve un float (grados fahrenheit).
    """

    # Se realiza la operación de conversión:
    resultado_fahrenheit: float = (grados_centigrados * 9/5) + 32

    return resultado_fahrenheit


def convertir_a_centigrados(grados_fahrenheit: float) -> float:
    """
    Esta función convierte grados fahrenheit a grados centígrados.
    PRECONDICIONES: Recibe un float (grados_centigrados).
    POSCONDICIONES: Devuelve un float (grados fahrenheit).
    """

    # Se realiza la operación de conversión:
    resultado_centigrados: float = (grados_fahrenheit - 32) * 5/9

    return resultado_centigrados


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    # Se imprime el título del ejercicio:
    print("\nEjercicio 1: Conversión de temperaturas\n")

    # Se declara y define la variable que indicará el tipo de grados que
    # ingresará el usuario.
    tipo_de_grados: str = ''

    # Se verifica que se indique correctamente el tipo de grados a ingresar.
    while (tipo_de_grados != 'c' and tipo_de_grados != 'f'
           and tipo_de_grados != 'C' and tipo_de_grados != 'F'):

        # Se prueba que no haya errores al ingresar el caracter. Si hay un
        # error, se lo ataja con la excepción.
        try:

            print("Indique el tipo de grados que ingresará:")

            # El usuario ingresa el caracter que indica el tipo de grados
            # que ingresará:
            tipo_de_grados = input("(c:centigrados / f:fahrenheit): ")

        except ValueError as exc:

            # Si el ingreso del tipo de grado va mal, se imprime un mensaje
            # de error.
            print("Error al ingresar el tipo de grados.")
            print("Inténtelo nuevamente...\n")

    # Se declara y define la variable en la que el usuario ingresará la
    # cantidad de grados a convertir.
    grados_a_convertir: float = None

    # Se verifica con el ciclo while que se ingrese un valor válido para la
    # conversión.
    while grados_a_convertir is None:

        # Se prueba que no haya errores al ingresar el número. Si hay un
        # error, se lo ataja con la excepción.
        try:

            # Aquí el usuario hace el input del dato.
            grados_a_convertir = float(input("Ingrese cantidad de grados: "))

        except ValueError as exc:

            # Se imprime un mensaje de error.
            print("Error al ingresar la cantidad de grados a convertir.")
            print("El valor debe ser un número decimal.\n")

            # Se reinicia la variable para que se siga cumpliendo la condición
            # del ciclo while y así ingrese nuevamente el valor para la
            # variable.
            grados_a_convertir = None

    # Dependiendo del tipo de grados ingresado se convierte a °C o °F.
    if (tipo_de_grados == 'f' or tipo_de_grados == 'F'):

        grados_convertidos: float = convertir_a_centigrados(grados_a_convertir)

        # Se define una variable con el caracter correspondiente al tipo
        # de grados convertidos, para agregarlo al output final.
        grado: str = 'C'

    if (tipo_de_grados == 'c' or tipo_de_grados == 'C'):

        grados_convertidos: float = convertir_a_fahrenheit(grados_a_convertir)

        # Se define una variable con el caracter correspondiente al tipo
        # de grados convertidos, para agregarlo al output final.
        grado: str = 'F'

    # Se crea el mensaje para el output final.
    output_final: str = f"{grados_a_convertir} °{tipo_de_grados.upper()} = "
    output_final += f"{grados_convertidos} °{grado}"

    # Y, por último, se imprime el resultado.
    print("\nEl resultado para la conversión de grados es:")
    print(output_final)


if __name__ == "__main__":
    principal()
