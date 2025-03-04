"""4.5.2 Ejemplos de funciones: Triángulos
Ahora trabajaremos con triángulos. Comenzaremos con una función que verifique si tres lados de ciertas longitudes pueden formar un triángulo.

En la escuela aprendimos que la suma arbitraria de dos lados tiene que ser mayor que la longitud del tercer lado.

No será algo difícil. La función tendrá tres parámetros - uno para cada lado.

Regresará True si todos los lados pueden formar un triángulo, y False de lo contrario. En este caso, is_a_triangle es un buen nombre para dicha función.

Observa el código en el editor. Ahí se encuentra la función. Ejecuta el programa.


def is_a_triangle(a, b, c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

Parece que funciona perfectamente - estos son los resultados:

True
False

def is_a_triangle(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return False
    return True


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))


def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


print(is_a_triangle(1, 1, 1))
print(is_a_triangle(1, 1, 3))

Se ha negado la condición (se invirtieron los operadores relacionales y se reemplazaron los ors con ands, obteniendo una expresión universal para probar triángulos).

Coloquemos la función en un programa más grande. Se le pedirá al usuario los tres valores y se hará uso de la función.

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


a = float(input('Ingresa la longitud del primer lado: '))
b = float(input('Ingresa la longitud del segundo lado: '))
c = float(input('Ingresa la longitud del tercer lado: '))

if is_a_triangle(a, b, c):
    print('Si, si puede ser un triángulo.')
else:
    print('No, no puede ser un triángulo.')
    
Output: 
Ingresa la longitud del primer lado: 5
Ingresa la longitud del segundo lado: 6
Ingresa la longitud del tercer lado: 6
Si, si puede ser un triángulo."""


"""En el segundo paso, intentaremos verificar si un triángulo es un triángulo rectángulo.

Para ello haremos uso del Teorema de Pitágoras:

c2 = a2 + b2

¿Cómo saber cual de los tres lados es la hipotenusa?

La hipotenusa es el lado más largo.

Aquí esta el código:

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2   
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))


Observa como se establece la relación entre la hipotenusa y los dos catetos - se eligió el lado más largo y se aplico el Teorema de Pitágoras para verificar que todo estuviese en orden. Esto requiere tres revisiones en total.

Evaluando el área de un triángulo
También es posible evaluar el área de un triángulo. La Formula de Heron será útil aquí:


Vamos a emplear el operador de exponenciación para calcular la raíz cuadrada - puede ser extraño, pero funciona.


Este es el código resultante:

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def area_of_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return None
    return heron(a, b, c)


print(area_of_triangle(1., 1., 2. ** .5))

Lo probaremos con un triángulo rectángulo la mitad de un cuadrado y con un lado igual a 1. Esto significa que su área debe ser igual a 0.5.

Es extraño - pero el código produce la siguiente salida:

0.49999999999999983
Output
Es muy cercano a 0.5, pero no es exactamente 0.5. ¿Qué significa? ¿Es un error?

No, no lo es. Son solo los cálculos de valores punto flotantes. Pronto se discutirá el tema.

"""


"""4.5.3 Ejemplos de funciones: Factoriales
La siguiente función a definir calcula factoriales. ¿Recuerdas cómo se calcula un factorial?

0! = 1 (¡Si!, es verdad)
1! = 1
2! = 1 * 2
3! = 1 * 2 * 3
4! = 1 * 2 * 3 * 4
:
:
n! = 1 * 2 * 3 * 4 * ... * n-1 * n

Se expresa con un signo de exclamación, y es igual al producto de todos los números naturales previos al argumento o número dado.

Escribamos el código. Creemos una función con el nombre factorial_function. Aquí esta el código:


def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
 
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
 
 
for n in range(1, 6): # probando
    print(n, factorial_function(n))
 
Observa como se sigue el procedimiento matemático, y como se emplea el bucle for para encontrar el producto.

Estos son los resultados obtenidos del código de prueba:

1 1
2 2
3 6
4 24
5 120
Output
4.5.4 Números Fibonacci
¿Estás familiarizado con la serie Fibonacci?

Son una secuencia de números enteros los cuales siguen una regla sencilla:

el primer elemento de la secuencia es igual a uno (Fib1 = 1)
el segundo elemento también es igual a uno (Fib2 = 1)
cada número después de ellos son la suman de los dos números anteriores (Fibi = Fibi-1 + Fibi-2)
Aquí están algunos de los primeros números en la serie Fibonacci:

fib_1 = 1 fib_2 = 1 fib_3 = 1 + 1 = 2 fib_4 = 1 + 2 = 3 fib_5 = 2 + 3 = 5 fib_6 = 3 + 5 = 8 fib_7 = 5 + 8 = 13

¿Que opinas acerca de implementarlo como una función?

Creemos nuestra propia función fib y probémosla, aquí esta:


def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
 
    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum
 
 
for n in range(1, 10): # probando
    print(n, "->", fib(n))
 
Analiza el codigo del bucle for cuidadosamente, descifra como se mueven las variables elem_1 y elem_2 a través de los números subsecuentes de la serie Fibonacci.

Al probar el código, se generan los siguientes resultados:

1 -> 1
2 -> 1
3 -> 2
4 -> 3
5 -> 5
6 -> 8
7 -> 13
8 -> 21
9 -> 34
Output
4.5.5 Recursividad
Existe algo más que se desea mostrar: es la recursividad.

Este termino puede describir muchos conceptos distintos, pero uno de ellos, hace referencia a la programación computacional.

Aquí, la recursividad es una técnica donde una función se invoca a si misma.

Tanto el factorial como la serie Fibonacci, son las mejores opciones para ilustrar este fenómeno.

La serie de Fibonacci es un claro ejemplo de recursividad. Ya te dijimos que:

Fibi = Fibi-1 + Fibi-2

El número i se refiere al número i-1, y así sucesivamente hasta llegar a los primeros dos.

¿Puede ser empleado en el código? Por supuesto que puede. Puede hacer el código más corto y claro.

La segunda versión de la función fib() hace uso directo de la recursividad:


def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)
 
El código es mucho más claro ahora.

¿Pero es realmente seguro? ¿Implica algún riesgo?

Si, existe algo de riesgo. Si no se considera una condición que detenga las invocaciones recursivas, el programa puede entrar en un bucle infinito. Se debe ser cuidadoso.

El factorial también tiene un lado recursivo. Observa:

n! = 1 × 2 × 3 × ... × n-1 × n

Es obvio que:

1 × 2 × 3 × ... × n-1 = (n-1)!

Entonces, finalmente, el resultado es:

n! = (n-1)! × n

Esto se empleará en nuestra nueva solución.

Aquí esta:


def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)
 
¿Funciona? Claro que si. Pruébalo por ti mismo.

Nuestro viaje funcional esta por terminar. La siguiente sección abordara dos tipos de datos en Python: tuplas y diccionarios.

def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):
    print(n, "->", fib(n))




def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):  # probando
    print(n, "->", fib(n))



"""


def fib(n):
    if n < 1:
         return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):
    print(n, "->", fib(n))



"""
4.5.6 RESUMEN DE SECCIÓN
1. Una función puede invocar otras funciones o incluso a sí misma. Cuando una función se invoca a si misma, se le conoce como recursividad, y la función que se invoca a si misma y contiene una condición de terminación (la cual le dice a la función que ya no siga invocándose a si misma) es llamada una función recursiva.

2. Se pueden emplear funciones recursivas en Python para crear funciones limpias, elegantes, y dividir el código en trozos más pequeños. Sin embargo, se debe tener mucho cuidado ya que es muy fácil cometer un error y crear una función la cual nunca termine. También se debe considerar que las funciones recursivas consumen mucha memoria, y por lo tanto pueden ser en ocasiones ineficientes.

Al emplear la recursividad, se deben de tomar en cuenta tanto sus ventajas como desventajas.

La función factorial es un ejemplo clásico de como se puede implementar el concepto de recursividad:



# Implementación recursiva de la función factorial.
 
def factorial(n):
    if n == 1: # El caso base (condición de terminación).
        return 1
    else:
        return n * factorial(n - 1)
 
 
print(factorial(4)) # 4 * 3 * 2 * 1 = 24
 """
 
 
"""
4.5.6 RESUMEN DE SECCIÓN
1. Una función puede invocar otras funciones o incluso a sí misma. Cuando una función se invoca a si misma, se le conoce como recursividad, y la función que se invoca a si misma y contiene una condición de terminación (la cual le dice a la función que ya no siga invocándose a si misma) es llamada una función recursiva.

2. Se pueden emplear funciones recursivas en Python para crear funciones limpias, elegantes, y dividir el código en trozos más pequeños. Sin embargo, se debe tener mucho cuidado ya que es muy fácil cometer un error y crear una función la cual nunca termine. También se debe considerar que las funciones recursivas consumen mucha memoria, y por lo tanto pueden ser en ocasiones ineficientes.

Al emplear la recursividad, se deben de tomar en cuenta tanto sus ventajas como desventajas.

La función factorial es un ejemplo clásico de como se puede implementar el concepto de recursividad:



# Implementación recursiva de la función factorial.
 
def factorial(n):
    if n == 1: # El caso base (condición de terminación).
        return 1
    else:
        return n * factorial(n - 1)
 
 
print(factorial(4)) # 4 * 3 * 2 * 1 = 24
 
4.5.7 PRUEBA DE SECCIÓN
Pregunta 1: ¿Qué ocurrirá al intentar ejecutar el siguiente fragmento de código y por qué?


def factorial(n):
    return n * factorial(n - 1)
 
 
print(factorial(4))
 
Ocultar
La función no tiene una condición de terminación, por lo tanto Python arrojara una excepción (RecursionError: maximum recursion depth exceeded)

Pregunta 2: ¿Cuál es la salida del siguiente fragmento de código?


def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)
 
 
print(fun(25))
 
Ocultar
56
"""