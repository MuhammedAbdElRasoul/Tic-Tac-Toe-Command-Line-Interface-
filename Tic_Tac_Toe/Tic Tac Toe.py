def print_board(board):
    for row in board:
        print("|".join(row))

def handle_move(board, player):
    while True:
        row = int(input("Enter the row number (0-2): "))
        col = int(input("Enter the column number (0-2): "))
        if board[row][col] == "":
            board[row][col] = player
            break
        else:
            print("Invalid move! Try again.")

def check_win(board, player):
    # Check rows
    for row in board:
        if row.count(player) == 3:
            return True
    # Check columns
    for col in range(3):
        if [board[row][col] for row in range(3)].count(player) == 3:
            return True
    # Check diagonals
    if [board[i][i] for i in range(3)].count(player) == 3:
        return True
    if [board[i][2-i] for i in range(3)].count(player) == 3:
        return True
    return False

def check_tie(board):
    for row in board:
        if "" in row:
            return False
    return True

def play_game():
    board = [[""] * 3 for _ in range(3)]
    players = ["X", "O"]
    current_player = 0
    print("Welcome to Tic Tac Toe!")

    while True:
        print_board(board)
        handle_move(board, players[current_player])
        if check_win(board, players[current_player]):
            print_board(board)
            print("Player", players[current_player], "wins!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = (current_player + 1) % 2

play_game()