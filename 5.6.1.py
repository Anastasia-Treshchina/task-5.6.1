print("""Игра крестики-нолики""")
a = 3
b = 3

def draw_board():
    for i in range(a):
        print()
        print("-" * 13)
        print("| ", end="")
        for j in range(b):
            print(board[i][j], end=" | ")
    print()
    print("-" * 13)

def check_win(board):
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(board[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False

def check_cord(board, x, y):
    if x >= 0 and y >= 0 and x <= 2 and y <= 2:
        if board[x][y] != "X" and board[x][y] != "0":
            return True
        else:
            print("Точка занята!")
            return False
    else:
        print("Координаты вне диапазона!")
        return False

def ask_cord(board):
    while True:
        x = int(input("Введите номер строки: "))
        y = int(input("Введите номер столбца: "))
        if check_cord(board, x, y):
            return x, y

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]]

for i in range(9):
    draw_board()
    if i % 2 == 0:
        print("Ходит крестик")
    else:
        print("Ходит нолик")
    x, y = ask_cord(board)
    if i % 2 == 0:
        board[x][y] = "X"
    else:
        board[x][y] = "0"

    if check_win(board):
        break
