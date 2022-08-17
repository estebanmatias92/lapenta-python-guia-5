import re

print(
    "Escribir la funcion titulo(), la cual recibe un string y lo retorna, "
    "\nconvirtiendo la primera letra de cada palabra a mayuscula "
    "\ny las demas letras a minuscula, dejando inalterados los demas caracteres.\n\n"
)


def string_clean(string):
    stripped = string.strip()

    # Return stripped and cleaned string
    return re.sub(r"\s+", " ", stripped)


def to_titlecase(string):
    # Transform all the string to lower case
    lowercase = string.lower()
    # Pattern to match the first letter of each Word
    regex = r"\b(\w)"
    # Callback to map against each first letter to convert it to upper case
    capitalize = lambda x: x[0].upper()

    # Return parsed string
    return re.sub(regex, capitalize, lowercase)


def title_parser(text):
    # Cleans and parses to title case a string
    return to_titlecase(string_clean(text))


# Main program
while True:
    # Prepare exit message
    err = "Terminado..."

    # Try to get the input from the user
    try:
        phrase = input(
            "Ingrese frase a convertir en Title Case o presione ENTER para salir: "
        )
    except Exception:
        # If there is a problem with the input given, then exit
        print(err, "\n")
        break

    # If there is only white spaces with no nothing, then exit
    if not phrase.split():
        print(err, "\n")
        break

    # If you made it here, then parse the title and show it
    title = title_parser(phrase)
    print(title, "\n")
