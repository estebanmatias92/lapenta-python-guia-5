from helpers.collections.lists import *
from helpers.math.math import *

print(
    "Solicitar al usuario el ingreso de números primos. "
    + "La lectura finalizará cuando ingrese un número  que no sea primo.\n"
    + "Por cada número, mostrar la suma de sus dígitos. "
    + "También solicitar al usuario un  dígito e informar la cantidad de veces "
    + "que aparece en el número (frecuencia).\n"
    + "Al finalizar el  programa, mostrar el factorial del mayor número ingresado.\n\n"
)

data_list = []

while True:
    data = {"number": None, "digit": None, "digit_frequency": None, "digits_sum": None}

    try:
        data["number"] = int_input(
            "Añada un numeros primo a la lista o ingrese un numero no primo para salir: "
        )
    except ValueError as e:
        print(e)
        print("")

    if is_prime(data["number"]) == False:
        print("Saliendo...\n")
        break

    digit = int_input("Ingrese digito: ")
    if digit < 1 or digit > 9:
        print("El digito ingresado no es valido.\n")
        break

    # Splitting the number into list of digits
    digits_list = split_int(data["number"])

    # Populate the dictionary
    data["digit"] = digit
    data["digit_frequency"] = digits_list.count(digit)
    data["digits_sum"] = reduce_list_int(digits_list, lambda x, y: x + y)

    # Show digit sum and digit frequency
    print(
        f"El numero {data['digit']} aparece {data['digit_frequency']} ve{'z' if data['digit_frequency'] == 1 else 'ces'}"
    )
    print(f"La suma de los digitos {digits_list} es: {data['digits_sum']}")
    print("")
    # Now add the dictionary to the list
    data_list.append(data)


# If there is no data, just exit
if data_list == []:
    exit()

# Create a list of the numbers stored in each dictionary
numbers = [data["number"] for item in data]
# Get the maximun value within those numbers from the list
max_value = find_max(numbers)
# Get the factorial of that maximun value
fact = factorial(max_value)
# Show the factorial
print(f"El mayor numero ingresado fue {max_value} y su factorial es: {fact}")
print("\n")
