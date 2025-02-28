"""4.3.1 Efectos y resultados: la instrucción return

Todas las funciones presentadas anteriormente tienen algún tipo de efecto - producen un texto y lo envían a la consola.

Por supuesto, las funciones - al igual que las funciones matemáticas - pueden tener resultados.

Para lograr que las funciones devuelvan un valor (pero no solo para ese propósito) se utiliza la instrucción return (regresar o retornar).

Esta palabra nos da una idea completa de sus capacidades. Nota: es una palabra clave reservada de Python.

La instrucción return tiene dos variantes diferentes - considerémoslas por separado.

return sin una expresión
Consideremos la siguiente función:


def happy_new_year(wishes = True):
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not wishes:
        return
 
    print("¡Feliz año nuevo!")
 
Cuando se invoca sin ningún argumento:


happy_new_year()
 
La función produce un poco de ruido - la salida se verá así:

Tres...
Dos...
Uno...
¡Feliz año nuevo!
Output
Al proporcionar False como argumento:


happy_new_year(False)
 
Se modificará el comportamiento de la función - la instrucción return provocará su terminación justo antes de los deseos - esta es la salida actualizada:

Tres...
Dos...
Uno...
Output
return con una expresión
La segunda variante de return está extendida con una expresión:


def function():
    return expression
 
Existen dos consecuencias de usarla:

provoca la terminación inmediata de la ejecución de la función (nada nuevo en comparación con la primer variante)
además, la función evaluará el valor de la expresión y lo devolverá (de ahí el nombre una vez más) como el resultado de la función.
Si, este ejemplo es sencillo:


def boring_function():
    return 123
 
x = boring_function()
 
print("La función boring_function ha devuelto su resultado. Es:", x)
 
El fragmento de código escribe el siguiente texto en la consola:

La función boring_function ha devuelto su resultado. Es: 123
Output
Vamos a investigarlo.

Analiza la siguiente figura:

La instrucción return, enriquecida con la expresión (la expresión es muy simple aquí), "transporta" el valor de la expresión al lugar donde se ha invocado la función.

El resultado se puede usar libremente aquí, por ejemplo, para ser asignado a una variable.

También puede ignorarse por completo y perderse sin dejar rastro.

Tenga en cuenta que no estamos siendo demasiado educados aquí: la función devuelve un valor y lo ignoramos (no lo usamos de ninguna manera):


def boring_function():
    print("'Modo aburrimiento' ON.")
    return 123
 
print("¡Esta lección es interesante!")
boring_function()
print("Esta lección es aburrida...")
El programa produce el siguiente resultado:

¡Esta lección es interesante!
'Modo aburrimiento' ON.
Esta lección es aburrida...
Output
¿Está mal? De ninguna manera.

La única desventaja es que el resultado se ha perdido irremediablemente.

No olvides:

siempre se te permite ignorar el resultado de la función y estar satisfecho con el efecto de la función (si la función tiene alguno)
si una función intenta devolver un resultado útil, debe contener la segunda variante de la instrucción return.
Espera un segundo - ¿significa esto que también hay resultados inútiles? Sí, en cierto sentido.


"""

def boring_function():
    return 123

x = boring_function()

print("La función boring_function ha devuelto su resultado. Es:", x)

