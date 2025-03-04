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
Output
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

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

# Imprimir valores aquí.
print(dictionary)
print(phone_numbers)
print(empty_dictionary)

print(dictionary['gato'])
print(phone_numbers['Suzy'])

