def is_valid_DNI(num):
    """Checks if the number given is 7 or 8 digits long and returns True,
    else returns False.

    Args:
        num (int): DNI to validate

    Returns:
        bool: If the DNI is valid, returns True, otherwise returns False
    """
    count = len(str(num))

    if count < 7 or count > 8:
        return False

    return True
