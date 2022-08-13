from helpers.math.math import dividir

print("Importamos fichero y Dividimos (funcion) con Try-Catch (Try-Except)")

dividendo = float(input("\nIngrese dividendo: "))
divisor = float(input("Ingrese divisor: "))
print("")

resultado = dividir(dividendo, divisor)

print(f"El resultado es: {resultado}\n")
