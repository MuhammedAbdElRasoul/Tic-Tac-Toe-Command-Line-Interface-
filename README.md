# Tic-Tac-Toe (Command Line Interface)

A classic two-player Tic-Tac-Toe game built using Python, played entirely on the command line without a graphical user interface (GUI). This project focuses on fundamental programming concepts, including built-in data structures, control flow statements, functions, and user input handling.

---

## Game Rules
 The game is played on a 3x3 grid.
 Two players take turns placing their symbols (X or O) on the grid.
 The first player to get three in a row (horizontally, vertically, or diagonally) wins.
 If the grid is completely filled without any player getting three in a row, the game ends in a tie.

---

## Step-by-Step Logic & Architecture

1. Game Board Design: 
    Represented as a 3x3 list of lists.
    Each square is initialized as an empty string ("").
2. Display Board (print_board): 
    Iterates through the rows and columns to render the current state of the board in the console.
3. Player Moves (get_player_move): 
    Prompts the current player for their move using input().
    Updates the game board with the player's symbol at the specified location.
4. Check for Win (check_win): 
    Scans rows, columns, and diagonals to see if a player has three symbols in a row.
5. Check for Tie (check_tie): 
    Verifies if all squares are filled without an existing winner.
6. Main Game Loop (play_game): 
    Alternates turns between players, updates the board, prints the game state, and evaluates win/tie conditions until the game concludes.

---

## Testing & Debugging Checklist
 Verify that player moves correctly update the board.
 Test invalid moves (e.g., out-of-bounds or already occupied spots) to ensure robust handling.
 Confirm accurate win detection across rows, columns, and diagonals.
 Ensure ties are correctly detected when the grid is full.
