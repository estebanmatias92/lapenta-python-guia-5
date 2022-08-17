from core.exercises.helpers_13 import *

print(
    "Escribir un programa que permita al usuario obtener un identificador "
    "para cada uno de los socios de un club."
    "\nPara eso ingresara nombre completo y numero de DNI de cada socio, "
    "\nindicando que finalizara el procesamiento mediante el ingreso de un nombre vacio.\n\n"
)


def try_input(func, phrase):
    """Ask for input in a loop until the input is validated, otherwise return an
    exception or None if the user doesnt input data.

    Args:
        func (function): Input function with it-s validation to put in the loop
        phrase (string): Phrase to pass to input() as argument

    Raises:
        Exception: Catch possible error with the user hitting enter without data

    Returns:
        string: Returns the first name or last name, depending on the
        callback passed as argument
    """

    while True:
        try:
            name = func(phrase)
        except ValueError as e:
            print(e, "Intente de nuevo...")
        else:
            if not name:
                raise Exception("Dato vacio.")
            else:
                return name


def try_input_DNI(phrase):
    """Ask for input in a loop until the DNI is correct, otherwise print an
    error or return None.

    Args:
        phrase (string): Phrase to pass to the input() function

    Returns:
        int: Returns a DNI
    """
    while True:
        try:
            DNI = input_DNI(phrase)
        except ValueError as e:
            print(e)
        else:
            return DNI


def generate_ID(firstname, lastname, DNI):
    """Simple function that combines the first name of the partner, with the length
    of the last name and the first three digits from their DNI, to make an
    unique identifier and return it.

    Args:
        firstname (string): First name of the partner
        lastname (string): Last name of the partner
        DNI (int): DNI of the partner

    Returns:
        string: Result of the unique combination
    """
    # Only get the first name of first names
    firstname_1 = firstname.split()[0]
    # Now get the characters length of the last name
    lastname_len = str(len(lastname))
    # And now get the first three digits from the DNI
    DNI = str(DNI)
    DNI_firstdigits = DNI[0] + DNI[1] + DNI[2]

    # Combine all in a string
    ID = firstname_1 + lastname_len + DNI_firstdigits

    # And return it
    return ID


def ingresar_socio():
    """Ask for partner's data and returns a populated dictionary, or an empty one.
    This program ask for data input on one subject each time, asking for
    firstname, lastname and DNI, and populating the rest of the data, like the
    iD and the complete name.

    Returns:
        dictionary: Partner data type populated if everything is correct, otherwise
        will return an empty dictionary
    """
    socio = {"ID": None, "name": None, "firstname": None, "lastname": None, "DNI": None}

    try:
        firstname = try_input(input_firstname, "Ingrese nombre del socio: ")
        lastname = try_input(input_lastname, "Ingrese apellido del socio: ")
        DNI = try_input_DNI("Ingrese DNI: ")
    except Exception as e:
        print("")
        print("Ingreso de datos terminado.")
        return {}
    else:
        socio["ID"] = generate_ID(firstname, lastname, DNI)
        socio["name"] = firstname + " " + lastname
        socio["firstname"] = firstname
        socio["lastname"] = lastname
        socio["DNI"] = DNI

        return socio


# Main business logic
def main():
    """Ask for partners data in a loop and store the data in a list. Only exit
    when the user enters nothing.
    """
    # Initialize the partner's list
    lista_socios = []

    print("Ingresar datos de socios\n------------------------\n")
    while True:
        nuevo_socio = ingresar_socio()
        print("")

        if not nuevo_socio:
            break

        # Everything if correct, add socio to the list
        lista_socios.append(nuevo_socio)

    print("\nMostrando lista de socios\n-------------------------\n")
    for socio in lista_socios:
        print(
            f"ID: {socio['ID']}"
            f"\nNombre: {socio['name']}"
            f"\nDNI: {socio['DNI']}"
            "\n"
        )


# Call the excercise
main()
