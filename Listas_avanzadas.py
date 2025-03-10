"""3.7.1 Listas dentro de listas
Las listas pueden constar de escalares (es decir, números) y elementos de una estructura mucho más compleja (ya has visto ejemplos como cadenas, booleanos o incluso otras listas en las lecciones del Resumen de la Sección anterior). Veamos más de cerca el caso en el que los elementos de una lista son listas.

A menudo encontramos estos arreglos en nuestras vidas. Probablemente el mejor ejemplo de esto sea un tablero de ajedrez.

Un tablero de ajedrez está compuesto de filas y columnas. Hay ocho filas y ocho columnas. Cada columna está marcada con las letras de la A a la H. Cada línea está marcada con un número del uno al ocho.

La ubicación de cada campo se identifica por pares de letras y dígitos. Por lo tanto, sabemos que la esquina inferior derecha del tablero (la que tiene la torre blanca) es A1, mientras que la esquina opuesta es H8.

Supongamos que podemos usar los números seleccionados para representar cualquier pieza de ajedrez. También podemos asumir que cada fila en el tablero de ajedrez es una lista.

Observa el siguiente código:


row = []
 
for i in range(8):
    row.append(WHITE_PAWN)
 
Crea una lista que contiene ocho elementos que representan la segunda fila del tablero de ajedrez: la que está llena de peones (supon que WHITE_PAWN es un símbolo predefinido que representa un peón blanco)."""


"""************************************************************************"""

"""Comprensión de lista
El mismo efecto se puede lograr mediante una comprensión de lista, la sintaxis especial utilizada por Python para completar o llenar listas masivas.

Una comprensión de lista es en realidad una lista, pero se creó sobre la marcha durante la ejecución del programa, y no se describe de forma estática.

Echa un vistazo al fragmento:


row = [WHITE_PAWN for i in range(8)]
 
La parte del código colocada dentro de los paréntesis especifica:

los datos que se utilizarán para completar la lista (WHITE_PAWN)
la cláusula que especifica cuántas veces se producen los datos dentro de la lista (for i in range(8))
Permítenos mostrarte otros ejemplos de comprensión de lista:

Ejemplo #1:


squares = [x ** 2 for x in range(10)]
 
El fragmento de código genera una lista de diez elementos y la rellena con cuadrados de diez números enteros que comienzan desde cero (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)

Ejemplo #2:


twos = [2 ** i for i in range(8)]
 
El fragmento crea un arreglo de ocho elementos que contiene las primeras ocho potencias del numero dos (1, 2, 4, 8, 16, 32, 64, 128)

Ejemplo #3:


odds = [x for x in squares if x % 2 != 0 ]
 
El fragmento crea una lista con solo los elementos impares de la lista squares."""

"""Arreglos de dos dimensiones
Supongamos también que un símbolo predefinido denominado EMPTY designa un campo vacío en el tablero de ajedrez.

Entonces, si queremos crear una lista de listas que representan todo el tablero de ajedrez, se puede hacer de la siguiente manera:


board = []
 
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
 
Nota:

la parte interior del bucle crea una fila que consta de ocho elementos (cada uno de ellos es igual a EMPTY) y lo agrega a la lista del board;
la parte exterior se repite ocho veces;
en total, la lista board consta de 64 elementos (todos iguales a EMPTY).
Este modelo imita perfectamente el tablero de ajedrez real, que en realidad es una lista de elementos de ocho elementos, todos ellos en filas individuales. Resumamos nuestras observaciones:

los elementos de las filas son campos, ocho de ellos por fila;
los elementos del tablero de ajedrez son filas, ocho de ellos por tablero de ajedrez.
La variable board ahora es un arreglo bidimensional. También se le llama, por analogía a los términos algebraicos, una matriz.

Como las listas de comprensión puede ser anidadas, podemos acortar la creación del tablero de la siguiente manera:


board = [[EMPTY for i in range(8)] for j in range(8)]
 
La parte interna crea una fila, y la parte externa crea una lista de filas.

El acceso al campo seleccionado del tablero requiere dos índices - el primero selecciona la fila; el segundo - el número del campo dentro de la fila, el cual es un número de columna.

Echa un vistazo al tablero de ajedrez. Cada campo contiene un par de índices que se deben dar para acceder al contenido del campo:"""

"""3.7.3 Naturaleza multidimensional de las listas: aplicaciones avanzadas
Profundicemos en la naturaleza multidimensional de las listas. Para encontrar cualquier elemento de una lista bidimensional, debes usar dos coordenadas:

Una vertical (número de fila).
Una horizontal (número de columna).
Imagina que desarrollas una pieza de software para una estación meteorológica automática. El dispositivo registra la temperatura del aire cada hora y lo hace durante todo el mes. Esto te da un total de 24 × 31 = 744 valores. Intentemos diseñar una lista capaz de almacenar todos estos resultados.

Primero, debes decidir qué tipo de datos sería adecuado para esta aplicación. En este caso, sería mejor un float, ya que este termómetro puede medir la temperatura con una precisión de 0.1 ℃.

Luego tomarás la decisión arbitraria de que las filas registrarán las lecturas cada hora exactamente (por lo que la fila tendrá 24 elementos) y cada una de las filas se asignará a un día del mes (supongamos que cada mes tiene 31 días, por lo que necesita 31 filas). Aquí está el par apropiado de comprensiones (h es para las horas, d para el día):"""

"""temps = [[0.0 for h in range(24)] for d in range(31)]
 
Toda la matriz está llena de ceros ahora. Puede suponer que se actualiza automáticamente utilizando agentes de hardware especiales. Lo que tienes que hacer es esperar a que la matriz se llene con las mediciones.

Ahora es el momento de determinar la temperatura promedio mensual del mediodía. Suma las 31 lecturas registradas al mediodía y divida la suma por 31. Puedes suponer que la temperatura de medianoche se almacena primero. Aquí está el código:


temps = [[0.0 for h in range(24)] for d in range(31)]
#
# La matriz se actualiza aquí.
#
 
total = 0.0
 
for day in temps:
    total += day[11]
 
average = total / 31
 
print("Temperatura promedio al mediodía:", average)
 
Nota: La variable day utilizada por el bucle for no es un escalar - cada paso a través de la matriz temps lo asigna a la siguiente fila de la matriz; Por lo tanto, es una lista. Se debe indexar con 11 para acceder al valor de temperatura medida al mediodía.

Ahora encuentra la temperatura más alta durante todo el mes - analiza el código:


temps = [[0.0 for h in range(24)] for d in range(31)]
#
# La matriz se actualiza aquí.
#
 
highest = -100.0
 
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
 
print("La temperatura más alta fue:", highest)
 
Note:

la variable day itera en todas las filas de la matriz temps;
la variable temp itera a través de todas las mediciones tomadas en un día.
Ahora cuenta los días en que la temperatura al mediodía fue de al menos 20 ℃:


temps = [[0.0 for h in range(24)] for d in range(31)]
#
# La matriz se actualiza aquí.
#
 
hot_days = 0
 
for day in temps:
    if day[11] > 20.0:
        hot_days += 1
 
print(hot_days, "fueron los días calurosos.")
 
Python no limita la profundidad de la inclusión lista en lista. Aquí puedes ver un ejemplo de un arreglo tridimensional:


rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
 
Imagina un hotel. Es un hotel enorme que consta de tres edificios, de 15 pisos cada uno. Hay 20 habitaciones en cada piso. Para esto, necesitas un arreglo que pueda recopilar y procesar información sobre las habitaciones ocupadas/libres.

Primer paso - El tipo de elementos del arreglo. En este caso, sería un valor Booleano (True/False).

Paso dos - análisis de la situación. Resume la información disponible: tres edificios, 15 pisos, 20 habitaciones.

Ahora puedes crear el arreglo:


rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]
 
El primer índice (0 a 2) selecciona uno de los edificios; el segundo (0 a 14) selecciona el piso, el tercero (0 a 19) selecciona el número de habitación. Todas las habitaciones están inicialmente desocupadas.

Ahora ya puedes reservar una habitación para dos recién casados: en el segundo edificio, en el décimo piso, habitación 14:


rooms[1][9][13] = True
 
y desocupar el segundo cuarto en el quinto piso ubicado en el primer edificio:


rooms[0][4][1] = False
 
Verifica si hay disponibilidad en el piso 15 del tercer edificio:


vacancy = 0
 
for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
 
La variable vacancy contiene 0 si todas las habitaciones están ocupadas, o en dado caso el número de habitaciones disponibles.

¡Felicitaciones! Has llegado al final del módulo. ¡Sigue con el buen trabajo!"""


"""3.7.4 RESUMEN DE SECCIÓN
1. La comprensión de listas te permite crear nuevas listas a partir de las existentes de una manera concisa y elegante. La sintaxis de una comprensión de lista es la siguiente:

[expresión para el elemento en la lista si es condicional]
 
El cual es un equivalente del siguiente código:

for element in list:
    if conditional:
        expression
 
Este es un ejemplo de una comprensión de lista - el código siguiente crea una lista de cinco elementos con los primeros cinco números naturales elevados a la potencia de 3:


cubed = [num ** 3 for num in range(5)]
print(cubed) # output: [0, 1, 8, 27, 64]
 

2. Puedes usar listas anidadas en Python para crear matrices (es decir, listas bidimensionales). Por ejemplo:

# Una tabla de cuatro columnas y cuatro filas: un arreglo bidimensional (4x4)

table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

print(table)
print(table[0][0])  # output: ':('
print(table[0][3])  # output: ':)'


# Cubo - un arreglo tridimensional (3x3x3)

cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cube)
print(cube[0][0][0])  # output: ':('
print(cube[2][2][0])  # output: ':)'



"""

my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0])







