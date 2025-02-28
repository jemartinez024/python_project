"""3.5.2 Ordenando una lista
¿Cuántos pases necesitamos para ordenar la lista completa?

Resolvamos este problema de la siguiente manera: introducimos otra variable, su tarea es observar si se ha realizado algún intercambio durante el pase o no. Si no hay intercambio, entonces la lista ya está ordenada, y no hay que hacer nada más. Creamos una variable llamada swapped, y le asignamos un valor de False para indicar que no hay intercambios. De lo contrario, se le asignará True."""


my_list = [8, 10, 6, 2, 4]  # lista a ordenar
 
for i in range(len(my_list) - 1):  # necesitamos (5 - 1) comparaciones
    if my_list[i] > my_list[i + 1]:  # compara elementos adyacentes
        my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Si terminamos aquí, tenemos que intercambiar elementos.
 
# Deberías poder leer y comprender este programa sin ningún problema:


my_list = [8, 10, 6, 2, 4]  # lista a ordenar
swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.
 
while swapped:
    swapped = False  # no hay intercambios hasta ahora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # ¡ocurrió el intercambio!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 
print(my_list)
 
 
"""1️⃣ Inicialización de variables

my_list = []
swapped = True

my_list: Crea una lista vacía donde se guardarán los números que el usuario ingrese.
swapped: Bandera (booleano) que controla cuándo detener el bucle de ordenamiento. Si no hay cambios (no se intercambió nada en una pasada), el ciclo se detiene.

2️⃣ Ingreso de datos por el usuario

num = int(input("¿Cuántos elementos deseas ordenar?: "))
Pide al usuario que indique cuántos elementos quiere ingresar.
int() convierte la entrada en un número entero.

3️⃣ Llenar la lista con números ingresados

for i in range(num):
    val = float(input("Ingresa un elemento de la lista: "))
    my_list.append(val)
Un bucle for que se repite num veces.
Cada número ingresado se convierte a tipo float() (para admitir decimales).
my_list.append(val): Agrega el número a la lista.

4️⃣ Ordenar la lista usando Bubble Sort

while swapped:
    swapped = False
Inicia un bucle que se ejecuta hasta que no se realicen más intercambios (es decir, la lista esté ordenada).
Se reinicia swapped en False al principio de cada iteración.

5️⃣ Comparar e intercambiar elementos adyacentes

    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
Compara pares de elementos adyacentes en la lista.
Si el elemento actual (my_list[i]) es mayor que el siguiente (my_list[i + 1]), intercambia sus posiciones.
El intercambio ocurre con:

my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
swapped = True: Indica que hubo un intercambio, por lo que el ciclo se repetirá para revisar nuevamente la lista.

6️⃣ Mostrar la lista ordenada

print("\nOrdenada:")
print(my_list)
Imprime la lista una vez que ha sido completamente ordenada.
"""

"""
3.5.4 RESUMEN DE SECCIÓN
1. Puedes usar el método sort() para ordenar los elementos de una lista, por ejemplo:


lst = [5, 3, 1, 2, 4]
print(lst)
 
lst.sort()
print(lst)  # output: [1, 2, 3, 4, 5]
 
2.También hay un método de lista llamado reverse(), que puedes usar para invertir la lista, por ejemplo:


lst = [5, 3, 1, 2, 4]
print(lst)
 
lst.reverse()
print(lst)  # output: [4, 2, 1, 3, 5]
 """