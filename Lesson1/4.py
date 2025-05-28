def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, player):
    # Проверка строк, столбцов и диагоналей
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False


def is_full(board):
    return all([cell in ['X', 'O'] for row in board for cell in row])


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Ход игрока {current_player}")

        try:
            row = int(input("Введите номер строки (0-2): "))
            col = int(input("Введите номер столбца (0-2): "))
            if board[row][col] != " ":
                print("Это место уже занято. Попробуйте снова.")
                continue
        except (ValueError, IndexError):
            print("Неверный ввод. Введите числа от 0 до 2.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Игрок {current_player} победил!")
            break
        elif is_full(board):
            print_board(board)
            print("Ничья!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()

