"""3.4.7 Funciones vs métodos
Un método es un tipo específico de función - se comporta como una función y se parece a una función, pero difiere en la forma en que actúa y en su estilo de invocación.

Una función no pertenece a ningún dato - obtiene datos, puede crear nuevos datos y (generalmente) produce un resultado.

Un método hace todas estas cosas, pero también puede cambiar el estado de una entidad seleccionada.

Un método es propiedad de los datos para los que trabaja, mientras que una función es propiedad de todo el código.

Esto también significa que invocar un método requiere alguna especificación de los datos a partir de los cuales se invoca el método.

Puede parecer desconcertante aquí, pero lo trataremos en profundidad cuando profundicemos en la programación orientada a objetos.

En general, una invocación de función típica puede tener este aspecto:

result = function(arg)
 
La función toma un argumento, hace algo, y devuelve un resultado.

Una invocación de un método típico usualmente se ve así:

result = data.method(arg)
 
Nota: el nombre del método está precedido por el nombre de los datos que posee el método. A continuación, se agrega un punto, seguido del nombre del método y un par de paréntesis que encierran los argumentos.

El método se comportará como una función, pero puede hacer algo más - puede cambiar el estado interno de los datos a partir de los cuales se ha invocado.

Puedes preguntar: ¿por qué estamos hablando de métodos, y no de listas?

Este es un tema esencial en este momento, ya que le mostraremos como agregar nuevos elementos a una lista existente. Esto se puede hacer con métodos propios de las listas, no por funciones.

********************************

3.4.8 Agregando elementos a una lista: append() y insert()
Un nuevo elemento puede ser añadido al final de la lista existente:

list.append(value)
 
Dicha operación se realiza mediante un método llamado append(). Toma el valor de su argumento y lo coloca al final de la lista que posee el método.

La longitud de la lista aumenta en uno.

El método insert() es un poco más inteligente - puede agregar un nuevo elemento en cualquier lugar de la lista, no solo al final.

list.insert(location, value)
"""

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)
print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

#

numbers.insert(1, 333)
print(len(numbers))
print(numbers)

"""Puedes iniciar la vida de una lista creándola vacía (esto se hace con un par de corchetes vacíos) y luego agregar nuevos elementos según sea necesario.

Echa un vistazo al fragmento en el editor. Intenta adivinar su output después de la ejecución del bucle for. Ejecuta el programa para comprobar si tenías razón.

my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.append(i + 1)

print(my_list)

Será una secuencia de números enteros consecutivos del 1 (luego agrega uno a todos los valores agregados) hasta 5.
"""