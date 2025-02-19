
c0 = int(input("Ingresa el número entero: "))

if c0 > 0:
    count_print = 0

    while c0 != 1:
        if c0 % 2 == 0: # Si c0 es par 
            c0 //= 2 # Actualiza el valor de c0
        else: # Si c0 es impar
            c0 = (3 * c0) + 1 # Actualiza el valor de c0
        
        print(c0)
        count_print += 1
    
    print("Pasos: ", count_print)
else:
    c0 = int(input("Ingresa el número entero: "))
        
""" count_print += 1
        print("Pasos: ", count_print)"""