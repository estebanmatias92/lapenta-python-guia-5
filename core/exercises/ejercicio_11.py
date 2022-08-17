from helpers.stdio.stdio import int_input
from core.exercises.dni import is_valid_DNI

print(
    "Escribir una funcion que, dado un numero de DNI, retorne True si el numero "
    + "es valido y False si no lo es. \nPara que un numero de DNI sea valido "
    + "debe tener entre 7 y 8 digitos\n\n"
)


while True:
    # Ask for the number and handle the possible errors
    try:
        DNI = int_input("Ingrese un numero de DNI o ingrese cero para salir: ")
    except ValueError as e:
        print(e, "\nSaliendo...")
        break
    else:
        # Scape if the number is zero
        if DNI == 0:
            print("Saliendo...")
            break

    if is_valid_DNI(DNI):
        print("El numero de DNI es valido.")
    else:
        print("El numero de DNI no es valido.")

    print("")

print("")
