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


"""4.6.5 Las tuplas y los diccionarios pueden trabajar juntos
Se ha preparado un ejemplo sencillo, mostrando como las tuplas y los diccionarios pueden trabajar juntos.

Imaginemos el siguiente problema:

necesitas un programa para calcular los promedios de tus alumnos;
el programa pide el nombre del alumno seguido de su calificación;
los nombres son ingresados en cualquier orden;
el ingresar un nombre vacío finaliza el ingreso de los datos (Nota 1: ingresar una puntuación vacía generará la excepción ValueError, pero no te preocupes por eso ahora, verás cómo manejar tales casos cuando hablemos de excepciones en el segundo parte de la serie del curso Fundamentos de Python)
una lista con todos los nombre y el promedio de cada alumno debe ser mostrada al final.
Observa el código en el editor, se muestra la solución.

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


Ahora se analizará línea por línea:

línea 1: crea un diccionario vacío para ingresar los datos; el nombre del alumno es empleado como clave, mientras que todas las calificaciones asociadas son almacenadas en una tupla (la tupla puede ser el valor de un diccionario, esto no es un problema)
línea 3: se ingresa a un bucle "infinito" (no te preocupes, saldrémos de el en el momento indicado)
línea 4: se lee el nombre del alumno aquí;
línea 5-6: si el nombre es una cadena vacía (), salimos del bucle;
línea 8: se pide la calificación del estudiante (un valor entero en el rango del 0-10)
línea 9-10: si la puntuación ingresada no está dentro del rango de 0 a 10, se abandona el bucle;
línea 12-13: si el nombre del estudiante ya se encuentra en el diccionario, se alarga la tupla asociada con la nueva calificación (observa el operador +=)
línea 14-15: si el estudiante es nuevo (desconocido para el diccionario), se crea una entrada nueva, su valor es una tupla de un solo elemento la cual contiene la calificación ingresada;
línea 17: se itera a través de los nombres ordenados de los estudiantes;
línea 18-19: inicializa los datos necesarios para calcular el promedio (sum y counter).
línea 20-22: se itera a través de la tupla, tomado todas las calificaciones subsecuentes y actualizando la suma junto con el contador.
línea 23: se calcula e imprime el promedio del alumno junto con su nombre.
Este es un ejemplo del programa:

Ingresa el nombre del estudiante: Bob
Ingresa la calificación del estudiante (0-10): 7
Ingresa el nombre del estudiante: Andy
Ingresa la calificación del estudiante (0-10): 3
Ingresa el nombre del estudiante: Bob
Ingresa la calificación del estudiante (0-10): 2
Ingresa el nombre del estudiante: Andy
Ingresa la calificación del estudiante (0-10): 10
Ingresa el nombre del estudiante: Andy
Ingresa la calificación del estudiante (0-10): 3
Ingresa el nombre del estudiante: Bob
Ingresa la calificación del estudiante (0-10): 9
Ingresa el nombre del estudiante:
Andy : 5.333333333333333
Bob : 6.0

"""

"""
4.6.6 RESUMEN DE SECCIÓN
Puntos Clave: tuplas
1. Las Tuplas son colecciones de datos ordenadas e inmutables. Se puede pensar en ellas como listas inmutables. Se definen con paréntesis:


my_tuple = (1, 2, True, "una cadena", (3, 4), [5, 6], None)
print(my_tuple)
 
my_list = [1, 2, True, "una cadena", (3, 4), [5, 6], None]
print(my_list)
 
Cada elemento de la tupla puede ser de un tipo de dato diferente (por ejemplo, enteros, cadenas, boleanos, etc.). Las tuplas pueden contener otras tuplas o listas (y viceversa).

2. Se puede crear una tupla vacía de la siguiente manera:


empty_tuple = ()
print(type(empty_tuple)) # salida: <class 'tuple'>
 
3. La tupla de un solo elemento se define de la siguiente manera:


one_elem_tuple_1 = ("uno", ) # Paréntesis y una coma.
one_elem_tuple_2 = "uno", # Sin paréntesis, solo la coma.
 
Si se elimina la coma, Python creará una variable no una tupla:


my_tuple_1 = 1,
print(type(my_tuple_1)) # salida: <class 'tuple'>
 
my_tuple_2 = 1 # Esto no es una tupla.
print(type(my_tuple_2)) # salida: <class 'int'>
 
4. Se pueden acceder los elementos de la tupla al indexarlos:


my_tuple = (1, 2.0, "cadena", [3, 4], (5, ), True)
print(my_tuple[3]) # salida: [3, 4]
 
5. Las tuplas son immutable, lo que significa que no se puede agregar, modificar, cambiar o quitar elementos. El siguiente fragmento de código provocará una excepción:


my_tuple = (1, 2.0, "cadena", [3, 4], (5, ), True)
my_tuple[2] = "guitarra" # Se genera la excepción TypeError.
 
Sin embargo, se puede eliminar la tupla completa:


my_tuple = 1, 2, 3,
del my_tuple
print(my_tuple) # NameError: name 'my_tuple' is not defined
 
6. Puedes iterar a través de los elementos de una tupla con un bucle (Ejemplo 1), verificar si un elemento o no esta presente en la tupla (Ejemplo 2), emplear la función len() para verificar cuantos elementos existen en la tupla (Ejemplo 3), o incluso unir o multiplicar tuplas (Ejemplo 4):


# Ejemplo 1
tuple_1 = (1, 2, 3)
for elem in tuple_1:
    print(elem)
 
# Ejemplo 2
tuple_2 = (1, 2, 3, 4)
print(5 in tuple_2)
print(5 not in tuple_2)
 
# Ejemplo 3
tuple_3 = (1, 2, 3, 4)
print(len(tuple_3))
print(5 not in tuple_3)
# Ejemplo 4
tuple_4 = tuple_1 + tuple_2
tuple_5 = tuple_3 * 2
 
print(tuple_4)
print(tuple_5)
 
  EXTRA  
También se puede crear una tupla utilizando la función integrada de Python tuple(). Esto es particularmente útil cuando se desea convertir un iterable (por ejemplo, una lista, rango, cadena, etcétera) en una tupla:


my_tuple = tuple((1, 2, "cadena"))
print(my_tuple)
 
my_list = [2, 4, 6]
print(my_list) # salida: [2, 4, 6]
print(type(my_list)) # salida: <class 'list'>
tup = tuple(my_list)
print(tup) # salida: (2, 4, 6)
print(type(tup)) # salida: <class 'tuple'>
 
De la misma manera, cuando se desea convertir un iterable en una lista, se puede emplear la función integrada de Python denominada list():


tup = 1, 2, 3,
my_list = list(tup)
print(type(my_list)) # salida: <class 'list'>
"""

"""Puntos clave: diccionarios
1. Los diccionarios son *colecciones indexadas de datos, mutables y desordenadas. (*En Python 3.6x los diccionarios están ordenados de manera predeterminada.

Cada diccionario es un par de clave:valor. Se puede crear empleando la siguiente sintaxis:


my_dictionary = {
    key1: value1,
    key2: value2,
    key3: value3,
}
 
2. Si se desea acceder a un elemento del diccionario, se puede hacer haciendo referencia a su clave colocándola dentro de corchetes (Ejemplo 1) o utilizando el método get() (Ejemplo 2):


pol_esp_dictionary = {
    "kwiat": "flor",
    "woda": "agua",
    "gleba": "tierra"
    }
 
item_1 = pol_esp_dictionary["gleba"] # Ejemplo 1
print(item_1) # salida: tierra
 
item_2 = pol_esp_dictionary.get("woda") # Ejemplo 2
print(item_2) # salida: agua
 
3. Si se desea cambiar el valor asociado a una clave específica, se puede hacer haciendo referencia a la clave del elemento, a continuación se muestra un ejemplo:


pol_esp_dictionary = {
    "zamek": "castillo",
    "woda": "agua",
    "gleba": "tierra"
    }
 
pol_esp_dictionary["zamek"] = "cerradura"
item = pol_esp_dictionary["zamek"]
print(item) # salida: cerradura
 
4. Para agregar o eliminar una clave (junto con su valor asociado), emplea la siguiente sintaxis:


phonebook = {} # un diccionario vacío
 
phonebook["Adán"] = 3456783958 # crear/agregar un par clave-valor
print(phonebook) # salida: {'Adán': 3456783958}
 
del phonebook["Adán"]
print(phonebook) # salida: {}
 
Además, se puede insertar un elemento a un diccionario utilizando el método update(), y eliminar el ultimo elemento con el método popitem(), por ejemplo:


pol_esp_dictionary = {"kwiat": "flor"}
 
pol_esp_dictionary.update({"gleba": "tierra"})
print(pol_esp_dictionary) # salida: {'kwiat': 'flor', 'gleba': 'tierra'}
 
pol_esp_dictionary.popitem()
print(pol_esp_dictionary) # salida: {'kwiat': 'flor'}
 
5. Se puede emplear el bucle for para iterar a través del diccionario, por ejemplo:


pol_esp_dictionary = {
    "zamek": "castillo",
    "woda": "agua",
    "gleba": "tierra"
    }
 
for item in pol_esp_dictionary:
    print(item)
#          zamek
#          woda
#          gleba
 
6. Si deseas examinar los elementos (claves y valores) del diccionario, puedes emplear el método items(), por ejemplo:


pol_esp_dictionary = {
    "zamek": "castillo",
    "woda": "agua",
    "gleba": "tierra"
    }
 
for key, value in pol_esp_dictionary.items():
    print("Pol/Esp ->", key, ":", value)
 
7. Para comprobar si una clave existe en un diccionario, se puede emplear la palabra clave reservada in:


pol_esp_dictionary = {
    "zamek": "castillo",
    "woda": "agua",
    "gleba": "tierra"
    }
 
if "zamek" in pol_esp_dictionary:
   print("Si")
else:
   print("No")
 
8. Se puede emplear la palabra reservada del para eliminar un elemento, o un diccionario entero. Para eliminar todos los elementos de un diccionario se debe emplear el método clear():


pol_esp_dictionary = {
    "zamek": "castillo",
    "woda": "agua",
    "gleba": "tierra"
    }
 
print(len(pol_esp_dictionary)) # salida: 3
del pol_esp_dictionary["zamek"] # eliminar un elemento
print(len(pol_esp_dictionary)) # salida: 2
 
pol_esp_dictionary.clear() # eliminar todos los elementos
print(len(pol_esp_dictionary)) # salida: 0
 
del pol_esp_dictionary # elimina el diccionario
 
9. Para copiar un diccionario, emplea el método copy():


pol_esp_dictionary = {
    "zamek": "castillo",
    "woda": "agua",
    "gleba": "tierra"
    }
 
copy_dictionary = pol_esp_dictionary.copy()"""


"""
4.6.7 PRUEBA DE SECCIÓN
Pregunta 1: ¿Qué ocurrirá cuando se intente ejecutar el siguiente código?


my_tup = (1, 2, 3)
print(my_tup[2])
 
Ocultar
El programa imprimirá 3 en pantalla.

Pregunta 2: ¿Cuál es la salida del siguiente fragmento de código?


tup = 1, 2, 3
a, b, c = tup
 
print(a * b * c)
 
Ocultar
El programa imprimirá 6 en pantalla. Los elementos de la tupla tup han sido "desempaquetados" en las variables a, b, y c.

Pregunta 3: Completa el código para emplear correctamente el método count() para encontrar la cantidad de 2 duplicados en la tupla siguiente.


tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = # Escribe tu código aquí.
 
print(duplicates) # salida: 4
 
Ocultar
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)

print(duplicates)    # salida: 4
Pregunta 4: Escribe un programa que "una" los dos diccionarios (d1 y d2) para crear uno nuevo (d3).


d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}
 
for item in (d1, d2):
    # Escribe tu código aquí.
 
print(d3)
 
Ocultar
d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)

print(d3)
Pregunta 5: Escribe un programa que convierta la lista my_list en una tupla.


my_list = ["car", "Ford", "flower", "Tulip"]
 
t = # Escribe tu código aquí.
print(t)
Ocultar
my_list = ["car", "Ford", "flower", "Tulip"]

t = tuple(my_list)
print(t)
Pregunta 6: Escribe un programa que convierta la tupla colors en un diccionario.


colors = (("green", "#008000"), ("blue", "#0000FF"))
 
# Escribe tu código aquí.
 
print(colors_dictionary)
 
Ocultar
colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)
print(colors_dictionary)
Pregunta 7: ¿Que ocurrirá cuando se ejecute el siguiente código?


my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()
my_dictionary.clear()
 
print(copy_my_dictionary)
 
Ocultar
El programa mostrará {'A': 1, 'B': 2} en pantalla.

Pregunta 8: ¿Cuál es la salida del siguiente programa?


colors = {
    "blanco": (255, 255, 255),
    "gris": (128, 128, 128),
    "rojo": (255, 0, 0),
    "verde": (0, 128, 0)
    }
 
for col, rgb in colors.items():
    print(col, ":", rgb)
 
Ocultar
blanco : (255, 255, 255)
gris : (128, 128, 128)

ojo : (255, 0, 0)
verde : (0, 128, 0)
"""