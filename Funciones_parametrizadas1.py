"""4.2.1 Funciones parametrizadas
El potencial completo de una función se revela cuando puede ser equipada con una interface que es capaz de aceptar datos provenientes de la invocación. Dichos datos pueden modificar el comportamiento de la función, haciéndola más flexible y adaptable a condiciones cambiantes.

Un parámetro es una variable, pero existen dos factores que hacen a un parámetro diferente:

los parámetros solo existen dentro de las funciones en donde han sido definidos, y el único lugar donde un parámetro puede ser definido es entre los paréntesis después del nombre de la función, donde se encuentra la palabra clave reservada def;
la asignación de un valor a un parámetro de una función se hace en el momento en que la función se manda llamar o se invoca, especificando el argumento correspondiente.
def function(parameter):
    ###  

Recuerda que:

los parámetros solo existen dentro de las funciones (este es su entorno natural)
los argumentos existen fuera de las funciones, y son los que pasan los valores a los parámetros correspondientes.
Existe una clara división entre estos dos mundos.

Enriquezcamos la función anterior agregándole un parámetro - se utilizará para mostrar al usuario el valor de un número que la función pide.

Se tendrá que modificar la definición def de la función - así es como se ve ahora:

def message(number):
    ###
 
Esta definición especifica que nuestra función opera con un solo parámetro con el nombre de number. Se puede utilizar como una variable normal, pero solo dentro de la función - no es visible en otro lugar.

Ahora hay que mejorar el cuerpo de la función:

def message(number):
    print("Ingresa un número:", number)
 
Se ha hecho buen uso del parámetro. Nota: No se le ha asignado al parámetro algún valor. ¿Es correcto?

Si, lo es.

Un valor para el parámetro llegará del entorno de la función.

Recuerda: especificar uno o más parámetros en la definición de la función es un requerimiento, y se debe de cumplir durante la invocación de la misma. Se debe proveer el mismo número de argumentos como haya parámetros definidos.

El no hacerlo provocará un error.

Intenta ejecutar el código en el editor.


def message(number):
    print("Ingresa un número:", number)

message()

Esto es lo que aparecerá en consola:

TypeError: message() missing 1 required positional argument: 'number'
Output
Aquí está ya de manera correcta:


def message(number):
    print("Ingresa un número:", number)
 
message(1)
 
De esta manera ya está correcto. El código producirá la siguiente salida:

Ingresa un número: 1
Output
¿Puedes ver cómo funciona? El valor del argumento utilizado durante la invocación (1) ha sido pasado a la función, dándole un valor inicial al parámetro con el nombre de number.

Existe una circunstancia importante que se debe mencionar.

Es posible tener una variable con el mismo nombre del parámetro de la función.

El siguiente código muestra un ejemplo de esto:


def message(number):
    print("Ingresa un número:", number)
 
number = 1234
message(1)
print(number)
 
Una situación como la anterior activa un mecanismo denominado sombreado:

el parámetro x sombrea cualquier variable con el mismo nombre, pero...
... solo dentro de la función que define el parámetro.
El parámetro llamado number es una entidad completamente diferente de la variable llamada number.

Esto significa que el código anterior producirá la siguiente salida:

Ingresa un número: 1
1234


Una función puede tener tantos parámetros como se desee, pero entre más parámetros, es más difícil memorizar su rol y propósito.

Modifiquemos la función- ahora tiene dos parámetros:

def message(what, number):
    print("Ingresa", what, "número", number)
 
Esto significa que para invocar la función se necesitan dos argumentos.

El primer parámetro va a contener el nombre del valor deseado.

Aquí está:


def message(what, number):
    print("Ingresa", what, "número", number)
 
message("teléfono", 11)
message("precio", 5)
message("número", "number")
 
Esta es la salida del código anterior:

Ingresa teléfono número 11
Ingresa precio número 5
Ingresa número número número
Output
Ejecuta el código, modifícalo, agrega más parámetros, y ve cómo esto afecta la salida.

"""


"""4.2.2 Paso de parámetros posicionales






def message(what, number):
    print("Ingresa", what, "número", number)

message("teléfono", 11)
message("precio", 5)
message("número", "number")
"""



"""4.2.2 Paso de parámetros posicionales

La técnica que asigna cada argumento al parámetro correspondiente, es llamada paso de parámetros posicionales, los argumentos pasados de esta manera son llamados argumentos posicionales.

Ya se ha utilizado, pero Python ofrece mucho más. Se abordará este tema a continuación.

def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, 3)

Nota: el paso de parámetros posicionales es usado de manera intuitiva por las personas en muchas situaciones. Por ejemplo, es generalmente aceptado que cuando nos presentamos mencionamos primero nuestro nombre(s) y después nuestro apellido, por ejemplo, "Me llamo Juan Pérez."

Sin embargo, En Hungría se hace al revés.

Ahora imaginemos que la función esta siendo utilizada en Hungría. En este caso, el código sería de la siguiente manera:


def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)
 
introduction("Luke", "Skywalker")
introduction("Jesse", "Quick")
introduction("Clark", "Kent")
 
¿Puedes predecir la salida? Ejecuta el código y verifícalo por ti mismo.

Ahora imaginemos que la función esta siendo utilizada en Hungría. En este caso, el código sería de la siguiente manera:


def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)
 
introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")
 
La salida será diferente. ¿La puedes predecir?

Ejecuta el código para comprobar tu respuesta. ¿Es lo que esperabas?

¿Puedes construir más funciones de este tipo ?

"""


"""4.2.3 Paso de argumentos de palabra clave
Python ofrece otra manera de pasar argumentos, donde el significado del argumento está definido por su nombre, no su posición - a esto se le denomina paso de argumentos con palabra clave.

Observa el siguiente código:

def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")

El concepto es claro - los valores pasados a los parámetros son precedidos por el nombre del parámetro al que se le va a pasar el valor, seguido por el signo de =.

La posición no es relevante aquí - cada argumento conoce su destino con base en el nombre utilizado.

Debes de poder predecir la salida. Ejecuta el código y verifica tu respuesta.

Por supuesto que no se debe de utilizar el nombre de un parámetro que no existe.

El siguiente código provocará un error de ejecución:

def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction(surname="Skywalker", first_name="Luke")

"""


"""4.2.4 Mezclando argumentos posicionales y de palabras clave
Es posible combinar ambos tipos si se desea - solo hay una regla inquebrantable: se deben colocar primero los argumentos posicionales y después los de palabra clave.

Piénsalo por un momento, entenderás el porque.

Para mostrarte como funciona, se utilizará la siguiente función de tres parámetros:


def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)
 
Su propósito es el de evaluar y presentar la suma de todos sus argumentos.

La función, al ser invocada de la siguiente manera:


adding(1, 2, 3)
 
dará como salida:

1 + 2 + 3 = 6
Output
Hasta ahorita es un ejemplo solo de argumentos posicionales.

También, se puede reemplazar la invocación actual por una con palabras clave, como la siguiente:


adding(c = 1, a = 2, b = 3)
 
El programa dará como salida lo siguiente:

2 + 3 + 1 = 6
Output
Ten presente el orden de los valores.

Ahora intentemos mezclar ambas formas.

Observa la siguiente invocación de la función:


adding(3, c = 1, b = 2)
 
Vamos a analizarla:

el argumento (3) para el parámetro a es pasado utilizando la forma posicional;
los argumentos para c y b son especificados con palabras clave.
Esto es lo que se verá en la consola:

3 + 2 + 1 = 6
Output
Sé cuidadoso, ten cuidado de no cometer errores. Si se intenta pasar mas de un valor a un argumento, ocurrirá un error y se mostrará lo siguiente.

Observa la siguiente invocación - se le esta asignando dos veces un valor al parámetro a:


adding(3, a = 1, b = 2)
 
La respuesta de Python es:

TypeError: adding() got multiple values for argument 'a'
Output
Observa el siguiente código. Es un código completamente correcto y funcional, pero no tiene mucho sentido:


adding(4, 3, c = 2)
 
Todo es correcto, pero el dejar solo un argumento con palabra clave es algo extraño - ¿Qué es lo que opinas?"""


"""4.2.5 Funciones parametrizadas - más detalles
En ocasiones ocurre que algunos valores de ciertos argumentos son más utilizados que otros. Dichos argumentos tienen valores predefinidos los cuales pueden ser considerados cuando los argumentos correspondientes han sido omitidos.


Uno de los apellidos más comunes en Latinoamérica es González. Tomémoslo para el ejemplo.

El valor por predeterminada para el parámetro se asigna de la siguiente manera:


def introduction(first_name, last_name="Smith"):
     print("Hola, mi nombre es", first_name, last_name)
 
Solo se tiene que colocar el nombre del parámetro seguido del signo de = y el valor por predeterminada.

Invoquemos la función de manera normal:


introduction("Jorge", "Pérez")
 
¿Puedes predecir la salida del programa? Ejecútalo y revisa si era lo esperado.

¿Y? No parece haber cambiado algo, pero cuando se invoca la función de una manera inusual, como esta:


introduction("Enrique")
 
o así:


introduction(first_name="Guillermo")
 
no habrá errores, ambas invocaciones funcionarán, la consola mostrará los siguientes resultados:

Hola, mi nombre es Enrique González
Hola, mi nombre es Guillermo González
Output
Pruébalo.

Puedes hacerlo con más parámetros, si te resulta útil. Ambos parámetros tendrán sus valores por predeterminada, observa el siguiente código:


def introduction(first_name="Juan", last_name="González"):
    print("Hola, mi nombre es", first_name, last_name)
 
Esto hace que la siguiente invocación sea completamente valida:


introduction()
 
Y esta es la salida esperada:

Hola, mi nombre es Juan González
Output
Si solo se especifica un argumento de palabra clave, el restante tomará el valor por predeterminada:


introduction(last_name="Rodríguez")
 
La salida es:

Hola, mi nombre es Juan Rodríguez
Output
Pruébalo.

Felicidades - has aprendido las técnicas básicas de comunicación con funciones."""

"""
4.2.6 RESUMEN DE SECCIÓN

1. Se puede pasar información a las funciones utilizando parámetros. Las funciones pueden tener tantos parámetros como sean necesarios.

Un ejemplo de una función con un parámetro:


def hi(name):
    print("Hola,", name)
 
hi("Greg")
 
Un ejemplo de una función de dos parámetros:


def hi_all(name_1, name_2):
    print("Hola,", name_2)
    print("Hola,", name_1)
 
hi_all("Sebastián", "Konrad")
 
Un ejemplo de una función de tres parámetros:


def address(street, city, postal_code):
    print("Tu dirección es:", street,"St.,", city, postal_code)
 
s = input("Calle: ")
p_c = input("Código Postal: ")
c = input("Ciudad: ")
address(s, c, p_c)
 
2. Puedes pasar argumentos a una función utilizando las siguientes técnicas:

paso de argumentos posicionales en la cual el orden de los parámetros es relevante (Ejemplo 1)
paso de argumentos con palabras clave en la cual el orden de los argumentos es irrelevante (Ejemplo 2)
una mezcla de argumentos posicionales y con palabras clave (Ejemplo 3).

Ejemplo 1
def subtra(a, b):
    print(a - b)
 
subtra(5, 2) # salida: 3
subtra(2, 5) # salida: -3
 
 
Ejemplo 2
def subtra(a, b):
    print(a - b)
 
subtra(a=5, b=2) # salida: 3
subtra(b=2, a=5) # salida: 3
 
Ex. 3
def subtra(a, b):
    print(a - b)
 
subtra(5, b=2) # salida: 3
subtra(5, 2) # salida: 3
 
Es importante recordar que primero se especifican los argumentos posicionales y después los de palabras clave. Es por esa razón que si se intenta ejecutar el siguiente código:


def subtra(a, b):
    print(a - b)
 
subtra(5, b=2) # salida: 3
subtra(a=5, 2) # Syntax Error
 
Python no lo ejecutará y marcará un error de sintaxis SyntaxError.

3. Se puede utilizar la técnica de argumentos con palabras clave para asignar valores predefinidos a los argumentos:


def name(first_name, last_name="Pérez"):
    print(first_name, last_name)
 
name("Andy") # salida: Andy Pérez
name("Bety", "Rodríguez") # salida: Bety Rodríguez (el argumento de palabra clave es reemplazado por "Rodríguez")
 



"""



def add_numbers(a, c, b=2):
    print(a + b + c)

add_numbers(a=1, c=3)


