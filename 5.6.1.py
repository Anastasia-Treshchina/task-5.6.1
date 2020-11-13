print("""Игра крестики-нолики""")
a=3
b=3

def draw_board():
    for i in range(a):
        print()
        print("-" * 13)
        print("| ", end="")
        for j in range(b):
            print(board[i][j], end=" | ")
    print()
    print("-" * 13)

    
    
# Тут делаем проверку на то, выиграл ли кто-то
def check_win(board):
    win_cord =(((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2,0), (2, 1), (2, 2)),
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

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]]

for i in range(9):
    draw_board()
    print("Номера строк и столбцов от 0 до 2.")
    if i % 2 == 0:
        print("Ходит крестик")
    else:
        print("Ходит нолик")
        # В зависимости от чётности i выводим сообщение, о том, кто сейчас ходит (крестик или нолик)
    x = int(input("Введите номер строки: "))
    y = int(input("Введите номер столбца: "))
    if i % 2 == 0:# Тут тоже в зависимости от чётности ставим либо "X" либо "O"
        board[x][y] = "X"
    else:
        board[x][y] = "0"
    
    if check_win(board):
        break
