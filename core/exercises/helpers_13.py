from core.exercises.dni import is_valid_DNI
from helpers.stdio.stdio import int_input
import re


def is_valid_name(name):
    """Check for legit name words, without numbers and etc, return False if
    the name does not match the criteria from the regular expression.

    Args:
        name (string): Name to check

    Returns:
        bool: Returns True if the name is valid, otherwise returns False
    """
    # Regular expression that matches owrds with no numbers, that have more than
    # two characters
    regex = "^[A-Z]'?[- a-zA-Z]+$"

    if re.search(regex, name) and len(name) >= 1:
        return True

    return False


def is_valid_lastname(lastname):
    """Additional validation on top of is_valid_name() that verifies if the lastname
    have multiple words, in that case returns False

    Args:
        lastname (string): Name to check

    Returns:
        bool: Returns True if the name is valid, otherwise returns False
    """
    if is_valid_name(lastname) and len(lastname.split()) == 1:
        return True

    return False


def is_empty(name):
    """Uses regular expression to verify is a string is empty.

    Args:
        name (string): String the check

    Returns:
        bool: Returns True if the string is empty, otherwise returns False
    """

    # Math if the string is full of empty spaces
    regex = "^\s*$"

    if re.search(regex, name):
        return True

    return False


def input_firstname(phrase="Ingrese nombre(s): "):
    """Ask for name input or for empty data, if no value is given or just empty
    spaces, then returns None.
    If a value is given, proceeds to validate it, if is not valid, throws an
    exception, otherwise returns the name entered.

    Args:
        phrase (string, optional): Name to enter on the system. Defaults to "Ingrese nombre(s): ".

    Raises:
        ValueError: Exception to show that the input data wasn't valid

    Returns:
        None|String: If the data es correct, returns the string, otherwise returns
        a None object
    """
    try:
        firstname = input(phrase)
    except Exception:
        return None

    if is_empty(firstname):
        return None

    if not is_valid_name(firstname):
        raise ValueError("Formato invalido para nombre.")

    return firstname


def input_lastname(phrase="Ingrese apellido: "):
    """Ask for name input or for empty data, if no value is given or just empty
    spaces, then returns None.
    If a value is given, proceeds to validate it, if is not valid, throws an
    exception, otherwise returns the name entered.

    Args:
        phrase (string, optional): Name to enter on the system. Defaults to "Ingrese apellido: ".

    Raises:
        ValueError: Exception to show that the input data wasn't valid

    Returns:
        None|String: If the data es correct, returns the string, otherwise returns
        a None object
    """
    try:
        lastname = input(phrase)
    except Exception:
        return None

    if is_empty(lastname):
        return None

    if not is_valid_lastname(lastname):
        raise ValueError("Formato invalido para apellido.")

    return lastname


def input_DNI(phrase="Ingrese DNI: "):
    """Ask for DNI input, validates and returns it.
    If the input given is empty, throw an exception
    If the DNI is not valid, throws an exception, otherwise returns the DNI.

    Args:
        phrase (string): DNI data. Defaults to "Ingrese DNI: ".

    Raises:
        ValueError: Throws an Exception if the input is empty or the DNI is invalid.

    Returns:
        int: If the DNI is valid, it will be returned
    """
    # Prepare error message
    error_message = "DNI invalido. Intente de nuevo."

    try:
        DNI = int_input(phrase)
    except Exception:
        raise ValueError(error_message)
    else:
        if not is_valid_DNI(DNI):
            raise ValueError(error_message)

    return DNI
