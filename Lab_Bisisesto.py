"""
4.3.2 Unas pocas palabras sobre None
Permítenos presentarte un valor muy curioso (para ser honestos, un valor que es ninguno) llamado None.

Sus datos no representan valor razonable alguno - en realidad, no es un valor en lo absoluto; por lo tanto, no debe participar en ninguna expresión.

Por ejemplo, un fragmento de código como el siguiente:


print(None + 2)
 
Causará un error de tiempo de ejecución, descrito por el siguiente mensaje de diagnóstico:

TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
Output
Nota: None es una palabra clave reservada.

Solo existen dos tipos de circunstancias en las que None se puede usar de manera segura:

cuando se le asigna a una variable (o se devuelve como el resultado de una función)
cuando se compara con una variable para diagnosticar su estado interno.
Al igual que aquí:


value = None
if value is None:
    print("Lo siento, no contienes ningún valor")
 
No olvides esto: si una función no devuelve un cierto valor utilizando una cláusula de expresión return, se asume que devuelve implícitamente None.

Vamos a probarlo.

Echa un vistazo al código en el editor.

def strange_function(n):
    if(n % 2 == 0):
        return True
print(strange_function(1))

Es obvio que la función strange_Function retorna True cuando su argumento es par.

¿Qué es lo que retorna de otra manera?

Podemos usar el siguiente código para verificarlo:


print(strange_function(2))
print(strange_function(1))
 
Esto es lo que vemos en la consola:

True
None
Output
No te sorprendas la próxima vez que veas None como el resultado de la función - puede ser el síntoma de un error sutil dentro de la función.


"""


"""4.3.3 Efectos y resultados: listas y funciones
Existen dos preguntas adicionales que deben responderse aquí.

La primera es: ¿Se puede enviar una lista a una función como un argumento?

¡Por supuesto que se puede! Cualquier entidad reconocible por Python puede desempeñar el papel de un argumento de función, aunque debes asegurarte de que la función sea capaz de hacer uso de él.

Entonces, si pasas una lista a una función, la función tiene que manejarla como una lista.

Una función como la siguiente:


def list_sum(lst):
    s = 0
 
    for elem in lst:
        s += elem
 
    return s
 
y se invoca así:


print(list_sum([5, 4, 3]))
 
retornará 12 como resultado, pero habrá problemas si la invocas de esta manera riesgosa:


print(list_sum(5))
 
La respuesta de Python será la siguiente:

TypeError: 'int' object is not iterable
Output
Esto se debe al hecho de que el bucle for no puede iterar un solo valor entero.

La segunda pregunta es: ¿Puede una lista ser el resultado de una función?

¡Si, por supuesto! Cualquier entidad reconocible por Python puede ser un resultado de función.

Observa el código en el editor. La salida del programa será así:


def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))

"""


"""Para determinar si un año es bisiesto, seguimos estas reglas:

Un año es bisiesto si es divisible por 4.
Excepto si es divisible por 100, a menos que también sea divisible por 400.
Ahora evaluamos cada caso:

1900: Divisible por 4 y por 100, pero no por 400 ❌ No es bisiesto
2000: Divisible por 4, por 100 y por 400 ✅ Es bisiesto
2016: Divisible por 4 y no por 100 ✅ Es bisiesto
1987: No es divisible por 4 ❌ No es bisiesto
Respuesta final:
✅ Bisiestos: 2000, 2016
❌ No bisiestos: 1900, 1987"""





def is_year_leap(year):
    if year % 4 != 0:
        return False  # No es divisible por 4, no es bisiesto
    elif year % 100 != 0:
        return True  # Es divisible por 4 pero no por 100, es bisiesto
    elif year % 400 == 0:
        return True  # Es divisible por 400, es bisiesto
    else:
        return False  # Es divisible por 100 pero no por 400, no es bisiesto

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")