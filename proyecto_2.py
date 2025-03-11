import random

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    print(f"{tablero[0]} | {tablero[1]} | {tablero[2]}")
    print("--+---+--")
    print(f"{tablero[3]} | {tablero[4]} | {tablero[5]}")
    print("--+---+--")
    print(f"{tablero[6]} | {tablero[7]} | {tablero[8]}")

# Función para verificar si hay un ganador
def verificar_ganador(tablero, jugador):
    # Combinaciones ganadoras
    combinaciones_ganadoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    for combinacion in combinaciones_ganadoras:
        if tablero[combinacion[0]] == tablero[combinacion[1]] == tablero[combinacion[2]] == jugador:
            return True
    return False

# Función para verificar si el tablero está lleno (empate)
def verificar_empate(tablero):
    return all(celda != ' ' for celda in tablero)

# Función para obtener el movimiento de la máquina
def movimiento_maquina(tablero):
    movimientos_disponibles = [i for i, celda in enumerate(tablero) if celda == ' ']
    return random.choice(movimientos_disponibles)

# Función principal del juego
def jugar_tres_en_raya():
    # Inicializar el tablero
    tablero = [' ' for _ in range(9)]
    # La máquina siempre empieza en el centro
    tablero[4] = 'X'
    imprimir_tablero(tablero)

    while True:
        # Turno del usuario
        try:
            movimiento_usuario = int(input("Elige un número del 1 al 9 para tu movimiento: ")) - 1
            if movimiento_usuario < 0 or movimiento_usuario > 8:
                print("Número fuera de rango. Por favor, elige un número entre 1 y 9.")
                continue
            if tablero[movimiento_usuario] != ' ':
                print("Esa casilla ya está ocupada. Por favor, elige otra.")
                continue
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número.")
            continue

        tablero[movimiento_usuario] = 'O'
        imprimir_tablero(tablero)

        # Verificar si el usuario ha ganado
        if verificar_ganador(tablero, 'O'):
            print("¡Felicidades! ¡Has ganado!")
            break

        # Verificar si hay un empate
        if verificar_empate(tablero):
            print("¡Es un empate!")
            break

        # Turno de la máquina
        print("Turno de la máquina...")
        movimiento_maq = movimiento_maquina(tablero)
        tablero[movimiento_maq] = 'X'
        imprimir_tablero(tablero)

        # Verificar si la máquina ha ganado
        if verificar_ganador(tablero, 'X'):
            print("¡La máquina ha ganado!")
            break

        # Verificar si hay un empate
        if verificar_empate(tablero):
            print("¡Es un empate!")
            break

# Iniciar el juego
jugar_tres_en_raya()