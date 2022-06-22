################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
7. Transformación de un número
Escribir un programa que permita transformar un número solicitado expresado
en grados, minutos y segundos a segundos a segundos. Y otra que haga el cambio
en el sentido contrario, devolviendo una tuple.

Recuerden que un grado son 60 minutos y un minuto son 60 segundos.

def sexadecimal_a_decimal(horas, minutos, segundos):
def decimal_a_sexadecimal(numero):
"""


def sexadecimal_a_decimal(horas: int, minutos: int, segundos: int) -> int:
    """
    Esta función convierte un número en sexadecimal (horas, minutos, segundos)
    a decimal. Retorna el valor decimal en segundos.
    PRECONDICIONES: Recibe 3 números enteros positivos (horas, minutos,
                    segundos).
    POSCONDICIONES: Devuelve un entero positivo.
    """

    resultado = segundos + 60 * minutos + 60 * 60 * horas

    return resultado


def decimal_a_sexadecimal(numero: int) -> tuple:
    """
    Esta función convierte un número en decimal (numero en segundos) a
    sexadecimal (horas, minutos, segundos). Retorna un tuple con enteros
    (horas, minutos, segundos).
    PRECONDICIONES: Recibe 1 número entero positivo (numero en segundos).
    POSCONDICIONES: Devuelve un tuple de enteros positivos (horas, minutos,
                    segundos).
    """

    # Se realizan las operaciones de conversión.
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
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    # Se imprime el título del ejercicio:
    print("\nEjercicio 7: Transformación de un número\n")

    # Se declara y define una variable en la que se guardará la decisión del
    # usuario, si quiere convertir a decimal o sexadecimal.
    convertir_a_decimal: bool = None

    # En el ciclo while se verifica que el usuario ingrese un valor válido
    # para decidir cómo convertir los valores ingresados.
    while convertir_a_decimal is None:

        print("¿Que conversión desea realizar?")
        print("1: Sexadecimal a decimal")
        print("2: Decimal a sexadecimal")

        # Se prueba que el usuario ingrese un valor válido.
        try:

            entrada: int = int(input("Ingrese su respuesta: "))

            if (entrada == 1):

                convertir_a_decimal = True

            elif (entrada == 2):

                convertir_a_decimal = False

            else:

                print("Debe ingresar un valor válido (1 o 2).\n")

                convertir_a_decimal = None

        # Se ataja posible error en el input.
        except ValueError as exc:

            print("Debe ingresar un valor válido (1 o 2).\n")

            # Se reinicia la variable para que se repita el ciclo e ingrese
            # correctamente el valor.
            convertir_a_decimal = None

    # Si el usuario elige convertir de sexadecimal a decimal.
    if convertir_a_decimal:

        # Se declaran y definen las variables necesarias para el sistema
        # sexadecimal.
        horas: int = None
        minutos: int = None
        segundos: int = None

        # Verificación de que se ingresen correctamente las horas.
        while horas is None:

            try:

                horas = int(input("Ingrese cantidad de horas: "))

                if (horas < 0):

                    print("Error: debe ser un número entero positivo")

                    # Se reinicia la variable para que se repita el ciclo
                    # while.
                    horas = None

            # Se ataja el error de input.
            except ValueError as exc:

                print("Error: Valor no válido. Debe ser un número entero.")

                # Se reinicia la variable para que se repita el ciclo while.
                horas = None

        # Verificación de que se ingresen correctamente los minutos.
        while minutos is None:

            try:

                minutos = int(input("Ingrese cantidad de minutos: "))

                if (minutos < 0):

                    print("Error: debe ser un número entero positivo")

                    # Se reinicia la variable para que se repita el ciclo
                    # while.
                    minutos = None

            # Se ataja el error de input.
            except ValueError as exc:

                print("Error: Valor no válido. Debe ser un número entero.")

                # Se reinicia la variable para que se repita el ciclo while.
                minutos = None

        # Verificación de que se ingresen correctamente los segundos.
        while segundos is None:

            try:

                segundos = int(input("Ingrese cantidad de segundos: "))

                if (segundos < 0):

                    print("Error: debe ser un número entero positivo")

                    # Se reinicia la variable para que se repita el ciclo
                    # while.
                    segundos = None

            # Se ataja el error de input.
            except ValueError as exc:

                print("Error: Valor no válido. Debe ser un número entero.")

                # Se reinicia la variable para que se repita el ciclo while.
                segundos = None

        # Se realiza la conversión.
        resultado: int = sexadecimal_a_decimal(horas, minutos, segundos)

        # Se imprime el resultado final.
        print(f"\nEl resultado de la conversión es: {resultado} segundos.")

    # Si el usuario no quiso hacer conversión sexadecimal a decimal, entonces
    # se realiza la conversión decimal a sexadecimal.
    else:

        # Se declara y define las variable para que el usuario ingrese los
        # segundos.
        segundos: int = None

        # Verificación de que se ingresen correctamente los segundos.
        while segundos is None:

            try:

                segundos = int(input("Ingrese cantidad de segundos: "))

                if (segundos < 0):

                    print("Error: debe ser un número entero positivo")

                    # Se reinicia la variable para que se repita el ciclo
                    # while.
                    segundos = None

            # Se ataja el error de input.
            except ValueError as exc:

                print("Error: Valor no válido. Debe ser un número entero.")

                # Se reinicia la variable para que se repita el ciclo while.
                segundos = None

        # Se realiza la conversión.
        resultado: tuple = decimal_a_sexadecimal(segundos)

        # Se imprime el resultado final.
        print(f"\nEl resultado de la conversión es: {resultado}")
        print(f"{resultado[0]} horas")
        print(f"{resultado[1]} minutos")
        print(f"{resultado[2]} segundos")


if __name__ == "__main__":
    principal()
