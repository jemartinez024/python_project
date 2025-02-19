"""largest_number = -99999999
counter = 0

while True:
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")

 ********************************************** """
"""largest_number = -99999999
counter = 0

number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Ingresa un número o escribe -1 para finalizar: "))

if counter:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")""" 
 
 
 
# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.
user_word = input("Ingresa una palabra: ")
# Convierte la palabra en mayusculas 
user_word = user_word.upper()

#letter = ()
for letter in user_word:
    # Completa el cuerpo del bucle for.
       if letter == "AEIOU":
        continue
print(letter)
    
