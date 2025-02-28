"""3.4.9 Haciendo uso de las listas
El bucle for"""


my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)): # para el valor de i en el rango de "longitud de la lista"
    total += my_list[i]

print(total)

"""Supongamos que deseas calcular la suma de todos los valores almacenados en la lista my_list.

Necesitas una variable cuya suma se almacenará y se le asignará inicialmente un valor de 0 - su nombre será total. (Nota: no la vamos a nombrar sum ya que Python utiliza el mismo nombre para una de sus funciones integradas: sum(). Utilizar ese nombre sería considerado una mala práctica.) Luego agrega todos los elementos de la lista usando el bucle for. Echa un vistazo al fragmento en el editor.

Comentemos este ejemplo:

a la lista se le asigna una secuencia de cinco valores enteros;
la variable i toma los valores 0, 1,2,3, y 4, y luego indexa la lista, seleccionando los elementos siguientes: el primero, segundo, tercero, cuarto y quinto;
cada uno de estos elementos se agrega junto con el operador += a la variable suma, dando el resultado final al final del bucle;
observa la forma en que se ha empleado la función len() - hace que el código sea independiente de cualquier posible cambio en el contenido de la lista."""


"""El segundo aspecto del bucle for
Pero el bucle for puede hacer mucho más. Puede ocultar todas las acciones conectadas a la indexación de la lista y entregar todos los elementos de la lista de manera práctica.

Este fragmento modificado muestra como funciona:

my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list: #  Para i dentro de la lista "my_list"
    total += i

print(total)

¿Qué sucede aquí?

la instrucción for especifica la variable utilizada para navegar por la lista (i) seguida de la palabra clave in y el nombre de la lista siendo procesado (my_list).
a la variable i se le asignan los valores de todos los elementos de la lista subsiguiente, y el proceso ocurre tantas veces como hay elementos en la lista;
esto significa que usa la variable i como una copia de los valores de los elementos, y no necesita emplear índices;
la función len() tampoco es necesaria aquí.

"""