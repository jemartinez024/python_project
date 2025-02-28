"""4.1.4 Tu primera función

Es bastante sencillo, es un ejemplo de como transformar una parte de código que se está repitiendo en una función.

El mensaje enviado a la consola por la función print() es siempre el mismo. El código es funcional y no contiene errores, sin embargo imagina que tendrías que hacer si tu jefe pidiera cambiar el mensaje para que fuese más cortés, por ejemplo, que comience con la frase "Por favor,".

Tendrías que tomar algo de tiempo para cambiar el mensaje en todos los lugares donde aparece (podrías hacer uso de copiar y pegar, pero eso no lo haría más sencillo). Es muy probable que cometas errores durante el proceso de corrección, eso traería frustración a ti y a tu jefe.

¿Es posible separar ese código repetido, darle un nombre y hacerlo reutilizable? Significaría que el cambio hecho en un solo lugar será propagado a todos los lugares donde se utilice.

Para que esto funcione, dicho código debe ser invocado cada vez que se requiera.

Es posible, esto es exactamente para lo que existen las funciones.

Se necesita definirla. Aquí, la palabra definir es significativa.

Así es como se ve la definición más simple de una función:

def function_name():
    cuerpo de la función
 
Siempre comienza con la palabra reservada def (que significa definir)
después de def va el nombre de la función (las reglas para darle nombre a las funciones son las mismas que para las variables)
después del nombre de la función, hay un espacio para un par de paréntesis (ahorita no contienen algo, pero eso cambiará pronto)
la línea debe de terminar con dos puntos;
la línea inmediatamente después de def marca el comienzo del cuerpo de la función - donde varias o (al menos una) instrucción anidada, será ejecutada cada vez que la función sea invocada; nota: la función termina donde el anidamiento termina, se debe ser cauteloso.


A continuación se definirá la función. Se llamará message ‒ aquí está:


def message():
    print("Ingresar valor: ")
La función es muy sencilla, pero completamente utilizable. Se ha nombrado message, pero eso es opcional, tu puedes cambiarlo. Hagamos uso de ella.

El código ahora contiene la definición de la función:


def message():
    print("Ingresar valor: ")
 
print("Inicia aqui.")
print("Termina aqui.")
 
Nota: no se está utilizando la función - no se está invocando en el código.

Al correr el programa, se mostrará lo siguiente:

Inicia aqui.
Termina aqui.
Output
Esto significa que Python lee la definición de la función y la recuerda, pero no la ejecuta sin tu permiso.

Se ha modificado el código - se ha insertado la invocación de la función entre los dos mensajes:


def message():
    print("Ingresar valor: ")
 
print("Inicia aqui.")
message()
print("Termina aqui.")
La salida ahora se ve diferente:

Inicia aqui.
Ingresar valor:
Termina aqui.
Output
Prueba el código, modifícalo, experimenta con el.

"""


"""4.1.5 Cómo funcionan las funciones
Observa la imagen.

Intenta mostrarte el proceso completo:

cuando se invoca una función, Python recuerda el lugar donde esto ocurre y salta hacia dentro de la función invocada;
el cuerpo de la función es entonces ejecutado;
al llegar al final de la función, Python regresa al lugar inmediato después de donde ocurrió la invocación.

Existen dos consideraciones muy importantes, la primera de ella es:

No se debe invocar una función antes de que se haya definido.

Recuerda - Python lee el código de arriba hacia abajo. No va a adelantarse en el código para determinar si la función invocada está definida más adelante, (el lugar "correcto" para definirla es "antes de ser invocada".)

Se ha insertado un error en el siguiente código - ¿puedes notar la diferencia?


print("Inicia aqui.")
message()
print("Termina aqui.")
 
 
def message():
    print("Ingresar valor: ")
Se ha movido la función al final del código. ¿Podrá Python encontrarla cuando la ejecución llegue a la invocación?

No, no podrá. El mensaje de error dirá:

NameError: name 'message' is not defined
Output
No intentes forzar a Python a encontrar funciones que no están definidas en el lugar correcto.

La segunda consideración es más sencilla:

Una función y una variable no pueden compartir el mismo nombre.

El siguiente fragmento de código es erróneo:


def message():
    print("Ingresar valor: ")
 
message = 1
El asignar un valor al nombre message causa que Python olvide su rol anterior. La función con el nombre de message ya no estará disponible.

Afortunadamente, es posible combinar o mezclar el código con las funciones - no es forzoso colocar todas las funciones al inicio del archivo fuente.

Observa el siguiente código:


print("Comienza aqui.")
 
 
def message():
    print("Ingresar valor: ")
 
message()
 
print("Termina aqui.")
Puede verse extraño, pero es completamente correcto, y funciona como se necesita.

Regresemos al ejemplo inicial para implementar la función de manera correcta:


def message():
    print("Ingresar valor: ")
 
message()
a = int(input())
message()
b = int(input())
message()
c = int(input())
 
El modificar el mensaje de entrada es ahora sencillo - se puede hacer con solo modificar el código una única vez - dentro del cuerpo de la función.

Abre el editor, e inténtalo tu mismo."""


"""
4.1.6 RESUMEN DE SECCIÓN
1. Una función es un bloque de código que realiza una tarea especifica cuando la función es llamada (invocada). Las funciones son útiles para hacer que el código sea reutilizable, que este mejor organizado, y más legible. Las funciones contienen parámetros y pueden regresar valores.

2. Existen al menos cuatro tipos de funciones básicas en Python:

funciones integradas las cuales son partes importantes de Python (como lo es la función print()). Puedes ver una lista completa de las funciones integradas de Python en la siguiente liga https://docs.python.org/3/library/functions.html.
también están las que se encuentran en módulos pre-instalados (se hablará acerca de ellas en el curso Fundamentos de Python 2)
funciones definidas por el usuario las cuales son escritas por los programadores para los programadores - puedes escribir tus propias funciones y utilizarlas libremente en tu código,
las funciones lambda (aprenderás acerca de ellas en el curso Fundamentos de Python 2.)
3. Las funciones propias se pueden definir utilizando la palabra reservada def y con la siguiente sintaxis:

def your_function(optional parameters):
    # el cuerpo de la función
 
Se puede definir una función sin que haga uso de argumentos, por ejemplo:


def message(): # definiendo una función
    print("Hello") # cuerpo de la función
 
message() # invocación de la función
 
También es posible definir funciones con argumentos, como la siguiente que contiene un solo parámetro:


def hello(name): # definiendo una función
    print("Hello,", name) # cuerpo de la función
 
 
name = input("Ingresa tu nombre: ")
 
hello(name) # invocación de la función
 
Se hablará más sobre las funciones parametrizadas en la siguiente sección. No te preocupes."""


"""
4.1.7 PRUEBA DE SECCIÓN
Pregunta 1: La función input() es un ejemplo de:

a) una función definida por el usuario

b) una función integrada

Ocultar
b es una función integrada.

Pregunta 2: ¿Qué es lo que ocurre cuando se invoca una función antes de ser definida? Ejemplo:


hi()
 
def hi():
    print("hi!")
 
Ocultar
Se genera una excepción (la excepción NameError).

Pregunta 3: ¿Qué es lo que ocurrirá cuando se ejecute el siguiente código?


def hi():
    print("hi")
 
hi(5)
 
Ocultar
Se genera una excepción (la excepción TypeError) ‒ la función hi() no toma argumentos.

"""