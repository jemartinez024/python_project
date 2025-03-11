def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    for row in board:
        print("+---+---+---+")
        print("|", " | ".join(row), "|")
    print("+---+---+---+")

def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    while True:
        try:
            move = int(input("Ingresa tu movimiento (1-9): "))
            if move < 1 or move > 9:
                print("Por favor, ingresa un número entre 1 y 9.")
                continue
            row = (move - 1) // 3
            col = (move - 1) % 3
            if board[row][col] == ' ':
                board[row][col] = 'O'
                break
            else:
                print("Esa casilla ya está ocupada. Intenta de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")

def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    free_fields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                free_fields.append((i, j))
    return free_fields

def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    # Verificar filas y columnas
    for i in range(3):
        if all([board[i][j] == sign for j in range(3)]) or all([board[j][i] == sign for j in range(3)]):
            return True
    # Verificar diagonales
    if all([board[i][i] == sign for i in range(3)]) or all([board[i][2 - i] == sign for i in range(3)]):
        return True
    return False

def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    from random import choice
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = choice(free_fields)
        board[row][col] = 'X'

# Inicialización del tablero
board = [[' ' for _ in range(3)] for _ in range(3)]

# Ejemplo de uso
if __name__ == "__main__":
    display_board(board)
    while True:
        enter_move(board)
        display_board(board)
        if victory_for(board, 'O'):
            print("¡Has ganado!")
            break
        draw_move(board)
        display_board(board)
        if victory_for(board, 'X'):
            print("¡La máquina ha ganado!")
            break
        if not make_list_of_free_fields(board):
            print("¡Es un empate!")
            break