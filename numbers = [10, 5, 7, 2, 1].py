numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

numbers[0] = 111
print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.

print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

"""El valor dentro de los corchetes que selecciona un elemento de la lista se llama un índice, mientras que la operación de seleccionar un elemento de la lista se conoce como indexación.

Vamos a utilizar la función print() para imprimir el contenido de la lista cada vez que realicemos los cambios. Esto nos ayudará a seguir cada paso con más cuidado y ver que sucede después de una modificación de la lista en particular.

Si deseas verificar la longitud actual de la lista, puedes usar una función llamada len() (su nombre proviene de length - longitud).

Cualquier elemento de la lista puede ser eliminado en cualquier momento - esto se hace con una instrucción llamada del (eliminar). Nota: es una instrucción, no una función.
"""
###

del numbers[1]  # Eliminando el segundo elemento de la lista.
print("Longitud de la nueva lista:", len(numbers))  # Imprimiendo nueva longitud de la lista.
print("\nNuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

###

"""Puede parecer extraño, pero los índices negativos son válidos, y pueden ser muy útiles.

Un elemento con un índice igual a -1 es el último en la lista.

numbers = [111, 7, 2, 1]
print(numbers[-1])

El código del ejemplo mostrará 1. Ejecuta el programa y comprueba.
Del mismo modo, el elemento con un índice igual a -2 es el anterior al último en la lista.

numbers = [111, 7, 2, 1]
print(numbers[-2])

El fragmento de ejemplo dará como output un 2.
"""