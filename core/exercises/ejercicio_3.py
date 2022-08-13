from helpers.stdio.stdio import int_input
from helpers.math.math import sum_digits

print(
    "Solicitar números al usuario hasta que ingrese el cero. "
    + "Por cada uno, mostrar la suma de sus dígitos.\n"
    + "Al finalizar, mostrar la sumatoria de todos los números ingresados y la "
    + "suma de sus dígitos.\n"
    + "Reutilizar la misma función realizada en el ejercicio 2."
    + "\n\n"
)

total_sum = 0
total_sum_digits = 0

# Asking for numbers, sum their digits and sums everything together at the end
while True:
    num = int_input("Ingrese numero: ")

    if num == 0:
        print("Saliendo...")
        break

    sum = sum_digits(num)

    total_sum += num
    total_sum_digits += sum

    print(f"La suma de sus digitos es: {sum}")
    print("")


# Showing the total sum
print(f"\nLa suma total acumulada de digitos es: {total_sum}")
print(f"La suma total acumulada de digitos es: {total_sum_digits}")
