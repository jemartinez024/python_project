hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.
print("Lista original: ", hat_list)
print("La longitud de la lista original es: ", len(hat_list))

user_number = input("Ingresa número: ")# Paso 1: escribe una línea de código que solicite al usuario
hat_list[2] = user_number# reemplazar el número de en medio con un número entero ingresado por el usuario.
print("Muestra el número que ingresó el usuario en la lista ", hat_list)

print("Borraremos el ultimo valor de la lista y queda de la siguiente forma: ")
del hat_list[4]# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
print("Muestra la lista con los nuevos valores: ", hat_list)
# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("Longitud de la nueva lista:", len(hat_list))
print(hat_list)
