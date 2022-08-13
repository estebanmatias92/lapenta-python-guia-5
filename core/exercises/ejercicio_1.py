import re

print(
    "Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje "
    "indicando si la dirección es válida o no, valiéndose de una función "
    "para decidirlo.\n Una dirección se considerará válida si contiene el "
    "símbolo '@'.\n\n"
)


def email_isvalid(email):
    """Validate through regular expression if an string meet the criteria to of
    an email, if it's correct returns True, else returns False.

    Args:
        email (string): String that contains an email

    Returns:
        bool: Returns True if the email meets the criteria or False if does not
    """

    # Regular expression that matches an email structured string
    regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

    # Checking
    if re.search(regex, email):
        return True

    return False


# Ask for the input
email = input("Ingrese email: ")

# Show message
print(f"Email {'es' if email_isvalid(email) else 'no es'} valido!")
