def is_prime(num): # función llamada is_prime que toma un parámetro num 
    for i in range(2, int(1 + num ** 0.5)): # Se inicia un bucle for que itera sobre los números desde 2 hasta int(1 + num ** 0.5). num ** 0.5 calcula la raíz cuadrada de num. int(1 + num ** 0.5) redondea hacia abajo y suma 1 para asegurarse de que el rango cubra todos los divisores potenciales.Por ejemplo, si num = 10, int(1 + 10 ** 0.5) = int(1 + 3.162) = 4, por lo que el bucle iterará sobre 2, 3.
        
        if num % i == 0: # En cada iteración del bucle, se verifica si num es divisible por i (es decir, si num % i == 0). Si num es divisible por i, significa que i es un divisor de num, por lo que num no es primo.
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()