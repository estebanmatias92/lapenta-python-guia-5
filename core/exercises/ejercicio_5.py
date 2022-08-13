from helpers.stdio.stdio import int_input
from helpers.math.math import int_count

print(
    "Solicitar al usuario un número entero y luego un dígito.\n"
    + " Informar la cantidad de ocurrencias del dígito  en el número, "
    + "utilizando para ello una función que calcule la frecuencia.\n\n"
)

while True:

    number = int_input("Ingrese el numero a comprobar o ingrese cero para salir: ")
    if number == 0:
        print("Saliendo...")
        break

    digit = int_input("Ingrese un digito mayor que cero: ")
    if digit < 1 or digit > 9:
        print("El digito no cumple el criterio dado. Saliendo...")
        break

    print(f"El numero aparece {int_count(number, digit)} veces.\n")
