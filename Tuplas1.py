"""4.6.1 Tipos de secuencia y mutabilidad
Antes de comenzar a hablar acerca de tuplas y diccionarios, se deben introducir dos conceptos importantes: tipos de secuencia y mutabilidad.

Un tipo de secuencia es un tipo de dato en Python el cual es capaz de almacenar más de un valor (o ninguno si la secuencia esta vacía), los cuales pueden ser secuencialmente (de ahí el nombre) examinados, elemento por elemento.

Debido a que el bucle for es una herramienta especialmente diseñada para iterar a través de las secuencias, podemos definirlas de la siguiente manera: una secuencia es un tipo de dato que puede ser escaneado por el bucle for.

Hasta ahora, has trabajado con una secuencia en Python - la lista. La lista es un clásico ejemplo de una secuencia de Python. Aunque existen otras secuencias dignas de mencionar, las cuales se presentaran a continuación.

La segunda noción - la mutabilidad - es una propiedad de cualquier tipo de dato en Python que describe su disponibilidad para poder cambiar libremente durante la ejecución de un programa. Existen dos tipos de datos en Python: mutables e inmutables.

Los datos mutables pueden ser actualizados libremente en cualquier momento - a esta operación se le denomina "in situ".

In situ es una expresión en Latín que se traduce literalmente como en posición, en el lugar o momento. Por ejemplo, la siguiente instrucción modifica los datos "in situ":


list.append(1)
 
Los datos inmutables no pueden ser modificados de esta manera.

Imagina que una lista solo puede ser asignada y leída. No podrías adjuntar ni remover un elemento de la lista. Si se agrega un elemento al final de la lista provocaría que la lista se cree desde cero.

Se tendría que crear una lista completamente nueva, la cual contenga los elementos ya existentes más el nuevo elemento.

El tipo de datos que se desea tratar ahora se llama tupla. Una tupla es una secuencia inmutable. Se puede comportar como una lista pero no puede ser modificada en el momento."""


"""4.6.2 Tuplas
Lo primero que distingue una lista de una tupla es la sintaxis empleada para crearlas - las tuplas utilizan paréntesis, mientras que las listas usan corchetes, aunque también es posible crear una tupla tan solo separando los valores por comas.

Observa el ejemplo:


tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125
 
Se definieron dos tuplas, ambas contienen cuatro elementos.

A continuación se imprimen en consola:


tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125
 
print(tuple_1)
print(tuple_2)
 
Esto es lo que se muestra en consola:

(1, 2, 4, 8)
(1.0, 0.5, 0.25, 0.125)
Output
Nota: cada elemento de una tupla puede ser de distinto tipo (punto flotante, entero, cadena, o cualquier otro tipo de dato).

¿Cómo crear una tupla?
¿Es posible crear una tupla vacía? Si, solo se necesitan unos paréntesis:


empty_tuple = ()
 
Si se desea crear una tupla de un solo elemento, se debe de considerar el hecho de que, debido a la sintaxis (una tupla debe de poder distinguirse de un valor entero ordinario), se debe de colocar una coma al final:

one_element_tuple_1 = (1, )
one_element_tuple_2 = 1.,
 
El quitar las comas no arruinará el programa en el sentido sintáctico, pero serán dos variables, no tuplas.

¿Cómo utilizar un tupla?
Si deseas leer los elementos de una tupla, lo puedes hacer de la misma manera que se hace con las listas.

Observa el código en el editor.

my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)

El programa debe de generar la siguiente salida, ejecútalo y comprueba:

1
1000
(10, 100, 1000)
(1, 10)
1
10
100
1000
Output
Las similitudes pueden ser engañosas - no intentes modificar el contenido de la tupla ¡No es una lista!

Todas estas instrucciones (con excepción de primera) causarán un error de ejecución:


my_tuple = (1, 10, 100, 1000)
 
my_tuple.append(10000)
del my_tuple[0]
my_tuple[1] = -10
 
Este es el mensaje que Python arrojará en la ventana de consola:

AttributeError: 'tuple' object has no attribute 'append'
Output
¿Qué más pueden hacer las tuplas?

la función len() acepta tuplas, y regresa el número de elementos contenidos dentro;
el operador + puede unir tuplas (ya se ha mostrado esto antes)
el operador * puede multiplicar las tuplas, así como las listas;
los operadores in y not in funcionan de la misma manera que en las listas.
El fragmento de código en el editor presenta todo esto.

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

La salida es la siguiente:

9
(1, 10, 100, 1000, 10000)
(1, 10, 100, 1, 10, 100, 1, 10, 100)
True
True
Output
Una de las propiedades de las tuplas más útiles es que pueden aparecer en el lado izquierdo del operador de asignación. Este fenómeno ya se vio con anterioridad, cuando fue necesario encontrar una manera de intercambiar los valores entre dos variables.

Observa el siguiente fragmento de código:


var = 123
 
t1 = (1, )
t2 = (2, )
t3 = (3, var)
 
t1, t2, t3 = t2, t3, t1
 
print(t1, t2, t3)
 
Muestra tres tuplas interactuando - en efecto, los valores almacenados en ellas "circulan" entre ellas - t1 se convierte en t2, t2 se convierte en t3, y t3 se convierte en t1.

Nota: el ejemplo presenta un importante hecho mas: los elementos de una tupla pueden ser variables, no solo literales. Además, pueden ser expresiones si se encuentran en el lado derecho del operador de asignación.


var = 123
 
t1 = (1, )
t2 = (2, )
t3 = (3, var)
 
t1, t2, t3 = t2, t3, t1
 
print(t1, t2, t3)"""