"""Rebanadas – índices negativos
Observa el fragmento de código a continuación:

my_list[start:end]
 
Para confirmar:

start es el índice del primer elemento incluido en la rebanada.
end es el índice del primer elemento no incluido en la rebanada.
Así es como los índices negativos funcionan en las rebanadas:


my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)
 
El resultado del fragmento es:

[8, 6, 4]


Si start especifica un elemento que se encuentra más allá del descrito por end (desde el punto de vista inicial de la lista), la rebanada estará vacía:


my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)
 
La output del fragmento es:

[]
Output
Si omites el start en tu rebanada, se supone que deseas obtener un segmento que comienza en el elemento con índice 0.

En otras palabras, la rebanada sería de esta forma:

my_list[:end]
 
es un equivalente más compacto de:

my_list[0:end]

Observa el fragmento de código a continuación:


my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)
 
Es por esto que su output es: [10, 8, 6].

Del mismo modo, si omites el end en tu rebanada, se supone que deseas que el segmento termine en el elemento con el índice len(my_list).

En otras palabras, la rebanada sería de esta forma:

my_list[start:]
 
es un equivalente más compacto de:

my_list[start:len(my_list)]
 
Observa el siguiente fragmento de código:


my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)
 
Por lo tanto, la output es: [4, 2].

Como hemos dicho anteriormente, el omitir el INICIO y FIN [INICIO:FIN] crea una copia de toda la lista:


my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)
 
El resultado del fragmento es: [10, 8, 6, 4, 2].

"""


"""Más sobre la instrucción del
La instrucción del descrita anteriormente puede eliminar más de un elemento de la lista a la vez - también puede eliminar rebanadas:


my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)
 
Nota: En este caso, la rebanada ¡no produce ninguna lista nueva!

La output del fragmento es: [10, 4, 2].

También es posible eliminar todos los elementos a la vez:


my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)
 
La lista se queda vacía y la output es: [].

Al eliminar la rebanada del código, su significado cambia dramáticamente.

Echa un vistazo:


my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list)
 
La instrucción del eliminará la lista, no su contenido.

La función print() de la última línea del código provocará un error de ejecución."""

"""3.6.4 Los operadores in y not in
Python ofrece dos operadores muy poderosos, capaces de revisar la lista para verificar si un valor específico está almacenado dentro de la lista o no.

Estos operadores son:


elem in my_list
elem not in my_list
 
El primero de ellos (in) verifica si un elemento dado (el argumento izquierdo) está actualmente almacenado en algún lugar dentro de la lista (el argumento derecho) - el operador devuelve True en este caso.

El segundo (not in) comprueba si un elemento dado (el argumento izquierdo) está ausente en una lista - el operador devuelve True en este caso.

Observa el código en el editor. El fragmento muestra ambos operadores en acción. ¿Puedes adivinar su output? Ejecuta el programa para comprobar si tenías razón.

my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

Listas - algunos programas simples
Ahora queremos mostrarte algunos programas simples que utilizan listas.

El primero de ellos intenta encontrar el valor mayor en la lista. Mira el código en el editor.

my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[2]

for i in range(1, len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print(largest)


El concepto es bastante simple - asumimos temporalmente que el primer elemento es el más grande y comparamos la hipótesis con todos los elementos restantes de la lista.

El código da como resultado el 17 (como se espera).

El código puede ser reescrito para hacer uso de la forma recién introducida del bucle for:


my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list:
    if i > largest:
        largest = i
 
print(largest)
 
El programa anterior realiza una comparación innecesaria, cuando el primer elemento se compara consigo mismo, pero esto no es un problema en absoluto.

El código da como resultado el 17 también (nada inusual).

Si necesitas ahorrar energía de la computadora, puedes usar una rebanada:


my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]
 
for i in my_list[1:]:
    if i > largest:
        largest = i
 
print(largest)
 
La pregunta es: ¿Cuál de estas dos acciones consume más recursos informáticos - solo una comparación o rebanar casi todos los elementos de una lista?

Ahora encontremos la ubicación de un elemento dado dentro de una lista:


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = 5
found = False
 
for i in range(len(my_list)):
    found = my_list[i] == to_find
    if found:
        break
 
if found:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")
    
    
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Es una lista de números enteros # del 1 al 10.
to_find = 5 # El número que queremos encontrar en la lista (en este caso, 5).
found = False # Variable booleana que se usa como bandera para indicar si el #  # elemento ha sido encontrado (inicia en False).

for i in range(len(my_list)): # Recorre todos los índices de la lista (de 0 a 9 en este caso, porque hay 10 elementos).
    found = my_list[i] == to_find # Compara el elemento en el índice i con el número que queremos encontrar (5). Si encuentra el número, found se vuelve True.
    if found: # verifica si la bandera cambió a True. Si es así, ejecuta break para salir inmediatamente del bucle y evitar seguir buscando.
        break


Ejemplo de iteraciones:

Iteración Índice (i) Valor (my_list[i])	Comparación (my_list[i] == 5) found
    1	        0	        1	                False	                False
    2	        1	        2	                False	                False
    3	        2	        3	                False	                False   
    4	        3	        4	                False	                False
    5	        4	        5	                True	                True (se detiene aquí

if found:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente") # Si el número no está en la lista, imprime
 
🔗 Flujo de ejecución completo (si el número está presente)
Comienza con found = False.
Recorre la lista elemento por elemento.
Al encontrar el número (5), cambia found a True y sale del bucle con break.
Imprime el índice donde se encontró el elemento.


drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0

for number in bets:
    if number in drawn:
        hits += 1

print(hits) 

Nota:

la lista drawn almacena todos los números sorteados;
La lista bets almacena los números con que se juega;
la variable hits cuenta tus aciertos.
la output del programa es: 4.



Iteración	Número (number)	Está en drawn?    Acción	hits
1	        3	            ✅ Sí	        hits += 1	1
2	        7	            ❌ No	        Sin cambios	1
3	        11	            ✅ Sí	        hits += 1	2
4	        42	            ✅ Sí	        hits += 1	3
5	        34	            ❌ No	        Sin cambios	3
6	        49	            ✅ Sí	        hits += 1	4




elem in my_list
elem not in my_list"""

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
unique_list = []# Escribe tu código aquí.

for number in my_list:
    if number not in unique_list:
        unique_list.append(number)

print("La lista con elementos únicos:")
print(unique_list)


"""
3.6.7 RESUMEN DE SECCIÓN
1. Si tienes una lista list_1, y la siguiente asignación: list_2 = list_1 esto no hace una copia de la lista list_1, pero hace que las variables list_1 y list_2 apunten a la misma lista en la memoria. Por ejemplo:


vehicles_one = ['coche', 'bicicleta', 'motor']
print(vehicles_one) # output: ['coche', 'bicicleta', 'motor']
 
vehicles_two = vehicles_one
del vehicles_one[0] # elimina 'coche'
print(vehicles_two) # output: ['bicicleta', 'motor']
 
2. Si deseas copiar una lista o parte de la lista, puedes hacerlo haciendo uso de rebanadas:


colors = ['rojo', 'verde', 'naranja']
 
copy_whole_colors = colors[:]  # copia la lista entera
copy_part_colors = colors[0:2]  # copia parte de la lista
 
3. También puede utilizar índices negativos para hacer uso de rebanadas. Por ejemplo:


sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # output: ['C', 'D']
 
4. Los parámetros start y end son opcionales al partir en rebanadas una lista: list[start:end], por ejemplo:


my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2: ]
slice_two = my_list[ :2]
slice_three = my_list[-2: ]
 
print(slice_one)  # output: [3, 4, 5]
print(slice_two)  # output: [1, 2]
print(slice_three)  # output: [4, 5]
 
5. Puedes eliminar rebanadas utilizando la instrucción del:


my_list = [1, 2, 3, 4, 5]
del my_list[0:2]
print(my_list)  # output: [3, 4, 5]
 
del my_list[:]
print(my_list)  # elimina el contenido de la lista, genera: []
 
6. Puedes probar si algunos elementos existen en una lista o no utilizando las palabras clave in y not in, por ejemplo:


my_list = ["A", "B", 1, 2]
 
print("A" in my_list)  # output: True
print("C" not in my_list)  # output: True
print(2 not in my_list)  # output: False
 """
 
 
"""
3.6.8 QUIZ DE SECCIÓN
Pregunta 1: ¿Cuál es el resultado del siguiente fragmento de código?


list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
 
del list_1[0]
del list_2[0]
 
print(list_3)
 
Ocultar
['C']
Pregunta 2: ¿Cuál es el resultado del siguiente fragmento de código?


list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
 
del list_1[0]
del list_2
 
print(list_3)
 
Ocultar
['B', 'C']
Pregunta 3: ¿Cuál es el resultado del siguiente fragmento de código?


list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
 
del list_1[0]
del list_2[:]
 
print(list_3)
 
Ocultar
[]
Pregunta 4: ¿Cuál es el resultado del siguiente fragmento de código?


list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]
 
del list_1[0]
del list_2[0]
 
print(list_3)
 
Ocultar
['A', 'B', 'C']
Pregunta 5: Inserta in o not in en lugar de ??? para que el código genere el resultado esperado.


my_list = [1, 2, "in", True, "ABC"]
 
print(1 ??? my_list)  # output True
print("A" ??? my_list)  # output True
print(3 ??? my_list)  # output True
print(False ??? my_list)  # output False
 
Ocultar
my_list = [1, 2, "in", True, "ABC"]

print(1 in my_list)  # output True
print("A" not in my_list)  # output True
print(3 not in my_list)  # output True
print(False in my_list)  # output False"""