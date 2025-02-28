
"""Dejemos de lado las listas por un breve momento y veamos un tema intrigante.

Imagina que necesitas reorganizar los elementos de una lista, es decir, revertir el orden de los elementos: el primero y el quinto, así como el segundo y cuarto elementos serán intercambiados. El tercero permanecerá intacto.

Pregunta: ¿cómo se pueden intercambiar los valores de dos variables?

Echa un vistazo al fragmento:

Python ofrece una forma más conveniente de hacer el intercambio - echa un vistazo:


variable_1 = 1
variable_2 = 2
 
variable_1, variable_2 = variable_2, variable_1

Claro, efectivo y elegante - ¿no?

Ahora puedes intercambiar fácilmente los elementos de la lista para revertir su orden:


my_list = [10, 1, 8, 3, 5]
 
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
 
print(my_list)
 
Ejecuta el fragmento. Su output debería verse así:

[5, 3, 8, 1, 10]

Se ve bien con cinco elementos.

¿Seguirá siendo aceptable con una lista que contenga 100 elementos? No, no lo hará.

¿Puedes usar el bucle for para hacer lo mismo automáticamente, independientemente de la longitud de la lista? Si, si puedes.

Así es como lo hemos hecho:

my_list = [10, 1, 8, 3, 5]
length = 0

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)

Nota:

hemos asignado la variable length a la longitud de la lista actual (esto hace que nuestro código sea un poco más claro y más corto)
hemos preparado el bucle for para que se ejecute su cuerpo length // 2 veces (esto funciona bien para listas con longitudes pares e impares, porque cuando la lista contiene un número impar de elementos, el del medio permanece intacto)
hemos intercambiado el elemento i (desde el principio de la lista) por el que tiene un índice igual a (length - i - 1) (desde el final de la lista); en nuestro ejemplo, for i igual a 0 a la (length - i - 1) da 4; for i igual a 3, da 3 - esto es exactamente lo que necesitábamos.

Las listas son extremadamente útiles y las encontrarás muy a menudo.
"""

"""Escribe un programa que refleje estos cambios y le permita practicar con el concepto de listas. Tu tarea es:

paso 1: crea una lista vacía llamada beatles;
paso 2: emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison;
paso 3: emplea el buclefor y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best;
paso 4: usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista;
paso 5: usa el método insert() para agregar a Ringo Starr al principio de la lista.
Por cierto, ¿eres fan de los Beatles? (Los Beatles son una de las bandas favoritas de Greg. Pero espera...¿Quién es Greg?)"""


# paso 1
beatles = []  # Creando una lista vacía.
print("Paso 1:", beatles)
my_list = ["John Lennon", "Paul McCartney", "George Harrison"]

# paso 2
beatles.append(my_list)
print("Paso 2:", beatles)

# paso 3
for my_list in beatles:
    my_list.append(input("Ingresa los nombres de Stu Sutcliffe a la lista de integrantes: "))
    my_list.append(input("Ingresa los nombres de Pete Best a la lista de integrantes: "))
print("Paso 3:", beatles)

# paso 4
del my_list[4]  # Eliminando elementos de la lista.
del my_list[3]
print("Paso 4:", beatles)

# paso 5
my_list.insert(0, "Ringo Star")
print("Paso 5:", beatles)

# probando la longitud de la lista
beatles = my_list
print("Los Fav", len(beatles))

