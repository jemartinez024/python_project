"""4.6.3 Diccionarios
El diccionario es otro tipo de estructura de datos de Python. No es una secuencia (pero puede adaptarse fácilmente a un procesamiento secuencial) y además es mutable.

Para explicar lo que es un diccionario en Python, es importante comprender de manera literal lo que es un diccionario.


¿Cómo crear un diccionario?
Si deseas asignar algunos pares iniciales a un diccionario, utiliza la siguiente sintaxis:


dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
 
print(dictionary)
print(phone_numbers)
print(empty_dictionary)
 
En este primer ejemplo, el diccionario emplea claves y valores las cuales ambas son cadenas. En el segundo, las claves con cadenas pero los valores son enteros. El orden inverso (claves → números, valores → cadenas) también es posible, así como la combinación número a número.

La lista de todos los pares es encerrada con llaves, mientras que los pares son separados por comas, y las claves y valores por dos puntos.

El primer diccionario es muy simple, es un diccionario Español-Francés. El segundo es un directorio telefónico muy pequeño.

Los diccionarios vacíos son construidos por un par vacío de llaves - nada inusual.

Un diccionario en Python funciona de la misma manera que un diccionario bilingüe. Por ejemplo, se tiene la palabra en español "gato" y se necesita su equivalente en francés. Lo que se haría es buscar en el diccionario para encontrar la palabra "gato". Eventualmente la encontrarás, y sabrás que la palabra equivalente en francés es "chat".

En el mundo de Python, la palabra que se esta buscando se denomina key. La palabra que se obtiene del diccionario es denominada value.

Esto significa que un diccionario es un conjunto de pares de key y value. Nota:

cada clave debe de ser única - no es posible tener una clave duplicada;
una clave puede ser un de dato de cualquier tipo - puede ser un número (entero o flotante), incluso una cadena, pero no una lista;
un diccionario no es una lista - una lista contiene un conjunto de valores numerados, mientras que un diccionario almacena pares de valores;
la función len() aplica también para los diccionarios - regresa la cantidad de pares (clave-valor) en el diccionario;
un diccionario es una herramienta de un solo sentido - si fuese un diccionario español-francés, podríamos buscar en español para encontrar su contraparte en francés más no viceversa.
A continuación veamos algunos ejemplos:

El diccionario entero se puede imprimir con una invocación a la función print(). El fragmento de código puede producir la siguiente salida:

{'perro': 'chien', 'caballo': 'cheval', 'gato': 'chat'}
{'Suzy': 5557654321, 'jefe': 5551234567}
{}
Output
¿Has notado que el orden de los pares impresos es diferente a la asignación inicial? ¿Qué significa esto?

Primeramente, recordemos que los diccionarios no son listas - no guardan el orden de sus datos, el orden no tiene significado (a diferencia de los diccionarios reales). El orden en que un diccionario almacena sus datos esta fuera de nuestro control. Esto es normal. (*)

  Nota  
(*) En Python 3.6x los diccionarios se han convertido en colecciones ordenadas de manera predeterminada. Tu resultado puede variar dependiendo en la versión de Python que se este utilizando.

¿Cómo utilizar un diccionario?
Analiza el código en el editor:

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}



Si deseas obtener cualquiera de los valores, debes de proporcionar una clave válida:


print(dictionary['cat'])
print(phone_numbers['Suzy'])
 
El obtener el valor de un diccionario es semejante a la indexación, gracias a los corchetes alrededor del valor de la clave.

Nota:

si una clave es una cadena, se tiene que especificar como una cadena;
las claves son sensibles a las mayúsculas y minúsculas: 'Suzy' sería diferente a 'suzy'.
El fragmento de código da las siguientes salidas:

chat
22657854310
Output
Ahora algo muy importante: No se puede utilizar una clave que no exista. Hacer algo como lo siguiente:


print(phone_numbers['president'])
 
Provocará un error de ejecución. Inténtalo.

Afortunadamente, existe una manera simple de evitar dicha situación. El operador in, junto con su acompañante, not in, pueden salvarnos de esta situación.

El siguiente código busca de manera segura palabras en francés:


dictionary = {"cat": "gato", "perro": "chien", "caballo": "cheval"}
words = ['gato', 'león', 'caballo']
 
for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")
 
La salida del código es la siguiente:

gato -> chat
león no está en el diccionario
caballo -> cheval

Nota  
Cuando escribes una expresión grande o larga, puede ser una buena idea mantenerla alineada verticalmente. Así es como puede hacer que el código sea más legible y más amigable para el programador, por ejemplo:


# Ejemplo 1:
dictionary = {
              "gato": "chat",
              "perro": "chien",
              "caballo": "cheval"
}
# Ejemplo 2:
phone_numbers = {'jefe': 5551234567,
              'Suzy': 22657854310
}
 
Este tipo de formato se llama sangría francesa.

"""


"""4.6.4 Métodos y funciones de los diccionarios
El método keys()
¿Pueden los diccionarios ser examinados utilizando el bucle for, como las listas o tuplas?

No y si.

No, porque un diccionario no es un tipo de dato secuencial - el bucle for no es útil aquí.

Si, porque hay herramientas simples y muy efectivas que pueden adaptar cualquier diccionario a los requerimientos del bucle for (en otras palabras, se construye un enlace intermedio entre el diccionario y una entidad secuencial temporal).

El primero de ellos es un método denominado keys(), el cual es parte de todo diccionario. El método retorna o regresa una lista de todas las claves dentro del diccionario. Al tener una lista de claves se puede acceder a todo el diccionario de una manera fácil y útil.

A continuación se muestra un ejemplo:


dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for key in dictionary.keys():
    print(key, "->", dictionary[key])
 
El código produce la siguiente salida:

caballo -> cheval
perro -> chien
gato -> chat
Output
Otra manera de hacerlo es utilizar el método items(). Este método retorna una lista de tuplas (este es el primer ejemplo en el que las tuplas son mas que un ejemplo de si mismas) donde cada tupla es un par de cada clave con su valor.

Así es como funciona:


dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for spanish, french in dictionary.items():
    print(spanish, "->", french)
 
Nota la manera en que la tupla ha sido utilizada como una variable del bucle for.

El ejemplo imprime lo siguiente:

gato -> chat
perro -> chien
caballo -> cheval
Output
Modificar, agregar y eliminar valores
El asignar un nuevo valor a una clave existente es sencillo - debido a que los diccionarios son completamente mutables, no existen obstáculos para modificarlos.

Se va a reemplazar el valor "chat" por "minou", lo cual no es muy adecuado, pero funcionará con nuestro ejemplo.

Observa:


dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary['gato'] = 'minou'
print(dictionary)
 
La salida es:

{'gato': 'minou', 'perro': 'chien', 'caballo': 'cheval'}
Output
La función sorted()
¿Deseas que la salida este ordenada? Solo hay que agregar al bucle for lo siguiente:


for key in sorted(dictionary.keys()):
También existe un método denominado values(), funciona de manera muy similar al de keys(), pero regresa una lista de valores.

Este es un ejemplo sencillo:


dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
for french in dictionary.values():
    print(french)
 
Como el diccionario no es capaz de automáticamente encontrar la clave de un valor dado, el rol de este método es algo limitado.

Agregando nuevas claves
El agregar una nueva clave con su valor a un diccionario es tan simple como cambiar un valor. Solo se tiene que asignar un valor a una nueva clave que no haya existido antes.

Nota: este es un comportamiento muy diferente comparado a las listas, las cuales no permiten asignar valores a índices no existentes.

A continuación se agrega un par nuevo al diccionario - un poco extraño pero válido:


dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary['cisne'] = 'cygne'
print(dictionary)
 
El ejemplo muestra como salida:

{'gato': 'chat', 'perro': 'chien', 'caballo': 'cheval', 'cisne': 'cygne'}
Output
  Nota  
También es posible insertar un elemento al diccionario utilizando el método update(), por ejemplo:


dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary.update({"pato": "canard"})
print(dictionary)
 
Eliminado una clave
¿Puedes deducir como eliminar una clave de un diccionario?

Nota: al eliminar la clave también se removerá el valor asociado. Los valores no pueden existir sin sus claves.

Esto se logra con la instrucción del.

A continuación un ejemplo:


dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
del dictionary['perro']
print(dictionary)
 
Nota: el eliminar una clave no existente, provocará un error.

El ejemplo da como salida:

{'gato': 'chat', 'caballo': 'cheval'}
Output
  EXTRA  
Para eliminar el ultimo elemento de la lista, se puede emplear el método popitem():


dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary.popitem()
print(dictionary) # salida: {'gato': 'chat', 'perro': 'chien'}
 
En versiones anteriores de Python, por ejemplo, antes de la 3.6.7, el método popitem() elimina un elemento al azar del diccionario."""


school_class = {}

while True:
    name = input("Ingresa el nombre del estudiante: ")
    if name == '':
        break
    
    score = int(input("Ingresa la calificación del estudiante (0-10): "))
    if score not in range(0, 11):
	    break

if name in school_class:
    school_class[name] += (score,)
else:
    school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)
