tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
current_player = 1


def is_space_empty(row, col):
    return tablero[row][col] == 0


def switch_player():
    global current_player
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1


def checkWinner():
    global tablero
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != 0:
            return tablero[i][0]
        elif tablero[0][i] == tablero[1][i] == tablero[2][i] != 0:
            return tablero[0][i]
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != 0:
        return tablero[0][0]
    elif tablero[0][2] == tablero[1][1] == tablero[2][0] != 0:
        return tablero[0][2]
    else:
        return 0


def isDraw():
    global tablero
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == 0:
                return False
    return True
