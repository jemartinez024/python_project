def is_prime(num):
    for n in num:
        if n % 1 == 0 and n % num == 0:
            return True
        else:
            return False
    # Escribe tu código aquí.

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print(is_prime)