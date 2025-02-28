"""3.6 Sección 6 – Operaciones con listas

La vida al interior de las listas

Ahora queremos mostrarte una característica importante y muy sorprendente de las listas, que las distingue de las variables ordinarias.

Queremos que lo memorices - ya que puede afectar tus programas futuros y causar graves problemas si se olvida o se pasa por alto.

Echa un vistazo al fragmento en el editor."""

list_1 = [1]
list_2 = list_1
list_1[0] = 2
print(list_2)

"""output: [2]
El programa:

crea una lista de un elemento llamada list_1;
la asigna a una nueva lista llamada list_2;
cambia el único elemento de list_1;
imprime la list_2;
La parte sorprendente es el hecho de que el programa mostrará como resultado: [2], no [1], que parece ser la solución obvia.

Las listas (y muchas otras entidades complejas de Python) se almacenan de diferentes maneras que las variables ordinarias (escalares).

Se podría decir que:

el nombre de una variable ordinaria es el nombre de su contenido;
el nombre de una lista es el nombre de una ubicación de memoria donde se almacena la lista.
Lee estas dos líneas una vez más - la diferencia es esencial para comprender de que vamos a hablar a continuación.

La asignación: list_2 = list_1 copia el nombre del arreglo no su contenido. En efecto, los dos nombres (list_1 y list_2) identifican la misma ubicación en la memoria de la computadora. Modificar uno de ellos afecta al otro, y viceversa.

¿Cómo te las arreglas con eso?
"""


list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

"""Su output es [1].

Esta parte no visible del código descrito como [:] puede producir una lista completamente nueva.

Una de las formas más generales de la rebanada es la siguiente:

my_list[inicio:fin]

Como puedes ver, se asemeja a la indexación, pero los dos puntos en el interior hacen una gran diferencia.

Una rebanada de este tipo crea una nueva lista (de destino), tomando elementos de la lista de origen - los elementos de los índices desde el start hasta el fin fin - 1.

Nota: no hasta el fin sino hasta fin-1. Un elemento con un índice igual a fin es el primer elemento el cual no participa en la segmentación.

Es posible utilizar valores negativos tanto para el inicio como para el fin(al igual que en la indexación).

Echa un vistazo al fragmento:


my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)
 
La lista new_list contendrá fin - inicio (3 - 1 = 2) elementos ‒ los que tienen índices iguales a 1 y 2 (pero no 3).

La output del fragmento es: [8, 6]

Ejecuta el código en el editor para ver cómo Python copia la lista completa y un fragmento de la lista. ¡Siéntete libre de experimentar!

# Copiando la lista completa.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copiando parte de la lista.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)


output: 
[1]
[8, 6]
"""