my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.insert(0, i + 1) # va a insertar i + 1 a la derecha [5, 4, 3, 2, 1]

print(my_list)

#Deberías obtener la misma secuencia, pero en orden inverso (este es el mérito de usar el método insert()).