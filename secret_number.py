secret_number = 777
print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
user_number = int(input("Introduce el número secreto: "))
while user_number != 777:
    if user_number != secret_number:
        print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    user_number = int(input("Introduce el número secreto: "))
        
    user_number == secret_number

print("¡Bien hecho, muggle! Eres libre ahora.")