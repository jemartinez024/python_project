word_without_vowels = ""

# Pedir al usuario que ingrese una palabra
user_word = input("Ingresa una palabra: ")

# Convertir la palabra a mayúsculas
user_word = user_word.upper()

# Recorrer cada letra de la palabra
for letter in user_word:
    # Si la letra es una vocal, saltar a la siguiente iteración
    if letter in "AEIOU":
        continue
    # Imprimir la letra no consumida en una línea separada
    print(letter)
print(word_without_vowels)
# Imprimir la palabra asignada a word_without_vowels.
#letter = word_without_vowels

