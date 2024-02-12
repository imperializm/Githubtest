from random import randrange

def print_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def check_win(board, sign):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == sign for j in range(3)) or all(board[j][i] == sign for j in range(3)):
            return True
    if all(board[i][i] == sign for i in range(3)) or all(board[i][2 - i] == sign for i in range(3)):
        return True
    return False

def check_tie(board):
    # Check if the board is full (no free squares left)
    return all(square.isdigit() is False for row in board for square in row)

def user_move(board):
    while True:
        try:
            move = int(input("Enter your move: "))
            if 1 <= move <= 9 and board[(move - 1) // 3][(move - 1) % 3].isdigit():
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

def computer_move(board):
    while True:
        move = randrange(1, 10)
        if board[(move - 1) // 3][(move - 1) % 3].isdigit():
            return move

def tic_tac_toe():
    board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]
    print_board(board)

    for _ in range(4):  # 4 moves for each player
        user = user_move(board)
        board[(user - 1) // 3][(user - 1) % 3] = 'O'
        print_board(board)

        if check_win(board, 'O'):
            print("You won!")
            return

        if check_tie(board):
            print("It's a tie!")
            return

        computer = computer_move(board)
        board[(computer - 1) // 3][(computer - 1) % 3] = 'X'
        print_board(board)

        if check_win(board, 'X'):
            print("Computer won!")
            return

        if check_tie(board):
            print("It's a tie!")
            return

tic_tac_toe()
