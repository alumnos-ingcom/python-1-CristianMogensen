################
# Cristian Gustavo Mogensen - @CristianMogensen
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Números positivos y negativos
Escribir una función que reciba un número e indique si el mismo es positivo,
negativo o cero utilizando sumas y restas.

def signo(numero):
"""


def signo(numero: int) -> int:
    """
    Esta función analiza el signo de un número entero y retorna otro número
    entero que indica el signo del número ingresado:
    - (1) es positivo
    - (-1) es negativo
    - (0) es cero
    PRECONDICIONES: Recibe un número entero.
    POSCONDICIONES: Devuelve un número entero (1, -1, o 0).
    """

    # Se declaran y definen variables auxiliares:
    resultado: int = 0
    modulo: int = abs(numero)
    aux: int = numero
    contador: int = 0

    if (numero != 0):
        # Si el numero es cero, el resultado será 0 y no hará falta que
        # entre en el bucle.

        resultado = -1

        # En el bucle while se verifica que el número sea positivo.
        # Si no lo es, el resultado del bucle while no realizará cambios
        # en la variable resultado y, por lo tanto, el mismo será -1
        # (definido anteriormente) y querrá decir que el número es negativo.
        while (contador <= modulo):

            if (aux == 1):
                # Si es positivo, en los últimos pasos del bucle se debe
                # cumplir la condición (aux == 1) y la variable resultado
                # cambiará a 1, saliendo del bucle con el break.
                resultado = 1
                break

            aux -= 1
            contador += 1

    return resultado


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """

    # Se imprime el título del ejercicio:
    print("\nEjercicio 2: Números positivos y negativos\n")

    # Se declara y define una variable en la que el usuario ingresará
    # el número para probar con la función signo(). Se la inicializa con valor
    # None para que se pueda utilizar el ciclo while que 'valida' esta entrada.
    numero_entrada: int = None

    # Se define un ciclo while para asegurar que el número ingresado sea un
    # entero válido.
    while numero_entrada is None:

        # Se realiza el input del usuario y se ataja el error si no se ingresa
        # un valor válido. (se repite el input hasta que sea correcto).
        try:

            numero_entrada = int(input("Ingrese número: "))

        except ValueError as exc:

            # Se ataja error, en caso de que no se haya ingresado un valor
            # válido, y se imprime mensaje de error.
            print("Error: El valor ingresado debe ser un número entero.\n")

            # Se reinicia la variable para que se repita el ciclo while.
            numero_entrada = None

    # Se analiza el resultado.
    signo_numero: int = signo(numero_entrada)

    if (signo_numero == 1):  # número positivo

        resultado: str = "Positivo"

    elif (signo_numero == -1):  # número negativo

        resultado: str = "Negativo"

    else:  # número nulo

        resultado: str = "Nulo/cero"

    # Output del resultado.
    print(f"El signo del número ingresado {numero_entrada} es:")
    print(f"{resultado}.")


if __name__ == "__main__":
    principal()
