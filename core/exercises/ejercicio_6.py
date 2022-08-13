from helpers.stdio.stdio import int_input
from helpers.math.math import factorial

print(
    "Escribir un programa que pida números al usuario, "
    + "mostrar el factorial de cada uno y, al finalizar, \n"
    + "la  cantidad total de números leídos en total.\n"
    + "Utilizar una o más funciones, según sea necesario.\n\n"
)

count = 0

while True:

    number = int_input("Ingrese el numero a factorizar o ingrese cero para salir: ")
    if number == 0:
        print("Saliendo...")
        break

    try:
        result = factorial(number)
    except ValueError as e:
        print(e)
        print("")
    else:
        print(f"El factorial de {number} es: {result}\n")
    finally:
        count += 1


print(f"\nSe ingresaron un total de {count} numeros\n\n")
