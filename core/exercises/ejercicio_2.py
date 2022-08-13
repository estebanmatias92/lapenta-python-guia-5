from helpers.stdio.stdio import int_input
from helpers.math.math import sum_digits


print(
    "Solicitar números al usuario hasta que ingrese el cero. Por cada uno, "
    + "mostrar la suma de sus dígitos (utilizando una función que realice dicha suma)."
    + "\n\n"
)

while True:
    num = int_input("Ingrese numero: ")

    # Exit with input 0
    if num == 0:
        print("Saliendo...")
        break

    print(f"La suma de sus digitos es: {sum_digits(num)} \n")
