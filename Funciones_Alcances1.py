"""
    En esta parte del curso, aprenderás sobre los alcances en Python y la palabra clave global. Al final de la sección, podrás distinguir entre variables locales y globales, y sabrás cómo utilizar el mecanismo de espacios de nombres (namespaces) en tus programas.

4.4.1 Funciones y alcances
Comencemos con una definición:

El alcance de un nombre (por ejemplo, el nombre de una variable) es la parte del código donde el nombre es reconocido correctamente.

Por ejemplo, el alcance del parámetro de una función es la función en sí. El parámetro es inaccesible fuera de la función.

Vamos a revisarlo. Observa el código en el editor. ¿Qué ocurrirá cuando se ejecute?
    
    def scope_test():
    x = 123


scope_test()
print(x)

El programa no correrá. El mensaje de error dirá:

NameError: name 'x' is not defined
Output
Esto era de esperarse.

Vamos a conducir algunos experimentos para mostrar como es que Python define los alcances, y como los puedes utilizar para tu beneficio.

Comencemos revisando si una variable creada fuera de una función es visible dentro de una función. En otras palabras, ¿El nombre de la variable se propaga dentro del cuerpo de la función?

Observa el código en el editor. Ahí esta nuestro conejillo de indias.  
    
    
    def my_function():
    print("¿Conozco a la variable?", var)


var = 1
my_function()
print(var)

El resultado de la prueba es positivo - el código da como salida:

¿Conozco a la variable? 1
1
Output
La respuesta es: una variable que existe fuera de una función tiene alcance dentro del cuerpo de la función.

Esta regla tiene una excepción muy importante. Intentemos encontrarla.

Hagamos un pequeño cambio al código:


def my_function():
    var = 2
    print("¿Conozco a la variable?", var)
 
 
var = 1
my_function()
print(var)
 
El resultado ha cambiado también - el código arroja una salida con una ligera diferencia:

¿Conozco a la variable? 2
1
Output
¿Qué es lo que ocurrió?


la variable var creada dentro de la función no es la misma que cuando se define fuera de ella; parece que hay dos variables diferentes con el mismo nombre;
además, la variable de la función es una sombra de la variable fuera de la función.
La regla anterior se puede definir de una manera más precisa y adecuada:

Una variable que existe fuera de una función tiene un alcance dentro del cuerpo de la función, excluyendo a aquellas que tienen el mismo nombre.

También significa que el alcance de una variable existente fuera de una función solo se puede implementar dentro de una función cuando su valor es leído. El asignar un valor hace que la función cree su propia variable.

Asegúrate bien de entender esto correctamente y de realizar tus propios experimentos.
    
    """
    
    
"""4.4.2 Funciones y alcances: la palabra clave global
Al llegar a este punto, debemos hacernos la siguiente pregunta: ¿Una función es capaz de modificar una variable que fue definida fuera de ella? Esto sería muy incomodo.

Afortunadamente, la respuesta es no.

Existe un método especial en Python el cual puede extender el alcance de una variable incluyendo el cuerpo de las funciones (para poder no solo leer los valores de las variables sino también modificarlos).

Este efecto es causado por la palabra clave reservada llamada global:


global name
global name1, name2, ...
 
El utilizar la palabra reservada dentro de una función con el nombre o nombres de las variables separados por comas, obliga a Python a abstenerse de crear una nueva variable dentro de la función - se empleará la que se puede acceder desde el exterior.

En otras palabras, este nombre se convierte en global (tiene un alcance global, y no importa si se esta leyendo o asignando un valor).

Observa el código en el editor.

def my_function():
    global var
    var = 2
    print("¿Conozco a aquella variable?", var)


var = 1
my_function()
print(var)


Se ha agregado la palabra global a la función.

El código ahora da como salida:

¿Conozco a aquella variable? 2
2
Output
Esto debe de ser suficiente evidencia para mostrar lo que la palabra clave reservada global puede hacer.

"""


"""4.4.3 Cómo interactúa la función con sus argumentos
Ahora descubramos como la función interactúa con sus argumentos.

El código en el editor nos enseña algo. Como puedes observar, la función cambia el valor de su parámetro. ¿Este cambio afecta el argumento?

def my_function(n):
    print("Yo recibí", n)
    n += 1
    print("Ahora tengo", n)


var = 1
my_function(var)
print(var)

Ejecuta el programa y verifícalo.

La salida del código es:

Yo recibí 1
Ahora tengo 2
1

La conclusión es obvia - al cambiar el valor del parámetro este no se propaga fuera de la función (más específicamente, no cuando la variable es un valor escalar, como en el ejemplo).

Esto también significa que una función recibe el valor del argumento, no el argumento en sí. Esto es cierto para los valores escalares.

Vale la pena revisar cómo funciona esto con las listas (¿Recuerdas las peculiaridades de asignar rebanadas de listas en lugar de asignar la lista entera?)

El siguiente ejemplo arrojará luz sobre el asunto:



def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

La salida del código es:

Print #1: [2, 3]
Print #2: [2, 3]
Print #3: [0, 1]
Print #4: [2, 3]
Print #5: [2, 3]

Parece ser que se sigue aplicando la misma regla.


def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0]  # Presta atención a esta línea.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

No se modifica el valor del parámetro my_list_1 (ya se sabe que no afectará el argumento), en lugar de ello se modificará la lista identificada por el.

El resultado puede ser sorprendente. Ejecuta el código y verifícalo:

Print #1: [2, 3]
Print #2: [2, 3]
Print #3: [3]
Print #4: [3]
Print #5: [3]

¿Lo puedes explicar?

Intentémoslo:

si el argumento es una lista, el cambiar el valor del parámetro correspondiente no afecta la lista (recuerda: las variables que contienen listas son almacenadas de manera diferente que las escalares)
pero si se modifica la lista identificada por el parámetro (nota: ¡la lista, no el parámetro!), la lista reflejará el cambio.
Es tiempo de escribir algunos ejemplos de funciones. Lo harás en la siguiente sección.

"""


"""
4.4.4 RESUMEN DE SECCIÓN
1. Una variable que existe fuera de una función tiene alcance dentro del cuerpo de la función. (Ejemplo 1) al menos que la función defina una variable con el mismo nombre. (Ejemplo 2, y Ejemplo 3), por ejemplo:

Ejemplo 1:


var = 2
 
 
def mult_by_var(x):
    return x * var
 
 
print(mult_by_var(7)) # salida: 14
 
Ejemplo 2:


def mult(x):
    var = 5
    return x * var
 
 
print(mult(7)) # salida: 35
 
Ejemplo 3:


def mult(x):
    var = 7
    return x * var
 
 
var = 3
print(mult(7)) # salida: 49
 
2. Una variable que existe dentro de una función tiene un alcance solo dentro del cuerpo de la función (Ejemplo 4), por ejemplo:

Ejemplo 4:


def adding(x):
    var = 7
    return x + var
 
 
print(adding(4)) # salida: 11
print(var) # NameError
 
3. Se puede emplear la palabra clave reservada global seguida por el nombre de una variable para que el alcance de la variable sea global, por ejemplo:


var = 2
print(var) # salida: 2
 
 
def return_var():
    global var
    var = 5
    return var
 
 
print(return_var()) # salida: 5
print(var) # salida: 5"""