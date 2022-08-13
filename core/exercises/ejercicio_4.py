from helpers.stdio.stdio import int_input
from helpers.math.math import is_prime

print(
    "Requerir al usuario que ingrese un número entero e informar si es primo o no, "
    + "utilizando una función booleana que lo decida."
    + "\n\n"
)

while True:
    number = int_input("Ingrese el numero a comprobar o ingrese cero para salir: ")

    if number == 0:
        print("Saliendo...")
        break

    print(f"El numero {'es' if is_prime(number) else 'no es'} primo\n")
