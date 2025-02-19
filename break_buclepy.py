secret_code = ("chupacabra")
"""print(

+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
"""
user_code = (input("Introduce la palabra secreta: "))
while True:
    if user_code != secret_code:
        print("¡No has ingresado la palabra secreta!")
    user_code = (input("Introduce la palabra secreta nuevamente: "))
        
    if user_code == secret_code:
        break

print("Has dejado el bucle con éxito.")