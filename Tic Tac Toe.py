board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

winner = None
game_over = False
current_turn = 1
current_player = "X" #Player X moves first

def start_game():

    print_instructions()
    print_turn()
    print_board()

    while not game_over:
        do_turn(current_player)
        check_if_game_over()
        change_turn()

    # Print result 
    if winner == "X" or winner == "O":
        print("Player " + winner + " wins!")
    else:
        print("It's a tie!")
    print()

    # Ask players if they would like to play another game
    continue_game = input("Press Y to start a new game or any other key to quit: ")
    if continue_game == "Y" or continue_game == "y":
        print()
        reset_game()
        start_game()
    else:
        print()
        print("Thank you for playing :)")

# Creates a "new" game
def reset_game():
    global board
    global winner 
    global game_over 
    global current_turn
    global current_player

    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    winner = None
    game_over = False
    current_turn = 1
    current_player = "X"

# Prints instructions
def print_instructions():
    print("The positions of the cells are numbered in this format:\n")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")
    print()

# Prints turn number
def print_turn():
    global current_turn
    print("---------------------------------------")
    print("Turn " + str(current_turn) + "\n")
    current_turn += 1

# Prints board state
def print_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

# Perform actions for a turn
def do_turn(current_player):
    valid = False
    num = input("Player " + current_player + ", please choose a position from 1-9: ")

    # Check validity of user input
    while not valid:
        while num not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            num = input("Invalid input. Please choose a position from 1-9: ")
        num = int(num) - 1 # Convert to array element
        if board[num] == "-":
          valid = True

    board[num] = current_player
    print_turn()
    print_board()

# Switches control to the other player
def change_turn():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

# Check if the game is over
def check_if_game_over():
    check_for_winner()
    check_tie()

# Check for a winner
def check_for_winner():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

# Check for a tie
def check_tie():
    global game_over
    if "-" not in board:
        game_over = True
        return True
    else:
        return False

# Check rows
def check_rows():
    global game_over
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_over = True
        if row_1:
            return board[0] 
        elif row_2:
            return board[3] 
        elif row_3:
            return board[6] 
        else:
            return None

# Check columns
def check_columns():
    global game_over
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    if col_1 or col_2 or col_3:
        game_over = True
        if col_1:
            return board[0] 
        elif col_2:
            return board[1] 
        elif col_3:
            return board[2] 
        else:
            return None

# Check diagonals
def check_diagonals():
    global game_over
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"
    if diag_1 or diag_2:
        game_over = True
        if diag_1:
            return board[0] 
        elif diag_2:
            return board[2]
        else:
            return None

# Starts game
start_game()
