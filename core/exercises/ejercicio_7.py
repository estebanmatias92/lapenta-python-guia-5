from helpers.collections.lists import *

print(
    "Escribir un programa que pida números positivos al usuario.\n"
    + "Mostrar el número cuya sumatoria de  dígitos fue mayor "
    + "y la cantidad de números cuya sumatoria de dígitos fue menor que 10.\n"
    + "Utilizar una  o más funciones, según sea necesario.\n\n"
)


# 1 - Pedir numeros y retornar una lista
condition = lambda item: item > 0
numbers = input_list_int(
    "Añada un numero positivo a lista o ingrese cero para salir: ", condition
)

if len(numbers) < 2:
    print("\nSe necesitan al menos dos entradas para poder comparar.\nSaliendo...\n\n")
    exit()


# Create a function to map the list and sum each item's digits
sumar_digitos = lambda item: reduce_list_int(split_int(item), lambda x, y: x + y)


# 2 - Crear una lista nueva, con las sumas de los digitos de cada numero de la lista anterior
sums = map_list_int(numbers, sumar_digitos)


# 3 - Filtrar la lista de sumas y obtener el valor mas alto
max_value = find_max(sums)


# 4 - Filtrar la lista de sumas con los valores menores a 10 y retornar una lista nueva
numbers_below_ten = filter_list_int(sums, lambda item: item < 10)


# 5 - Contabilizar los items de la lista de resultados menores a 10 y retornar un entero
amount_below_ten = len(numbers_below_ten)


# 6 - Mostrar por pantalla los resultados
print("")

print("La suma de digitos mas alta es: " + f"{max_value}")
print(
    "La cantidad de numeros cuyos digitos sumados estan por debajo de 10 son: "
    + f"{amount_below_ten}"
)

print("\n")
