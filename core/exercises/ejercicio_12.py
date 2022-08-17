print(
    "Escribir una funcion que, dado un string, retorne la longitud de la ultima palabras.\n"
    + "Se considera que las palabras estan separadas por uno o mas espacios.\n"
    + "Tambien podria haber espacios al principio o al final del string pasado por parametro.\n\n"
)


def last_word_length(string):
    words = string.split()
    return len(words[-1])


phrase = input("Ingrese una frase: ")
print(f"La ultima palabra de la frase tiene {last_word_length(phrase)} caracteres\n")
