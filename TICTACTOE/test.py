# ____________global variables

board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

game_still_going = True

winner = None

current_player = "X"

def display_board():

    print(board[0] + " | " +board[1] + " | " + board[2] )
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():
    display_board()


    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        # Flip to the other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner+ " won.")
    elif winner == None:
        print("Tie.")

# Handle a single turn of an arbitrary player
def handle_turn(player):


    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Choose a position from 1-9:")
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Position has been taken. Go again.")


    board[position] = player

    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():

    global  winner

    #check rows,columns,diagonals
    row_winner = check_rows()

    column_winner = check_coulmns()

    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner

    elif column_winner:
        winner = column_winner

    elif diagonal_winner:
        winner = diagonal_winner
    return

def check_rows():

    global board
    global game_still_going

    row_1 = board[0]== board[1]==board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return

def check_coulmns():

    global board
    global game_still_going

    col_1 = board[0]== board[3]==board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    if col_1 or col_2 or col_3:
        game_still_going = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return
def check_diagonals():

    global board
    global game_still_going

    dia_1 = board[0]== board[4]==board[8] != "-"
    dia_2 = board[2] == board[4] == board[6] != "-"


    if dia_1 or dia_2 :
        game_still_going = False
    if dia_1:
        return board[0]
    elif dia_2:
        return board[2]

    return
def check_if_tie():
    global  game_still_going
    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


play_game()
