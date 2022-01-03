
board = ["_","_","_",
         "_","_","_",
         "_","_","_"]

game_still_going=True

winner = None

current_player="X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():

    display_board()

    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner=="X" or winner=="O":

        print(winner + " won.")

    elif winner == None:

        print("Tie")



def handle_turn(player):
    print("Turno do "+ player)
    position = input("Digite a posição de 1 a 9: ")
    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Digite a posição de 1 a 9: ")
        position = int(position)-1
        if board[position]=="_":
            valid = True
        else:
            print("Invalido, tente outra posicao")
    board[position] =player
    display_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    global winner
    row_winner=check_rows()
    column_winner=check_columns()
    diagonal_winner=check_diagonals()
    if row_winner:
        winner=row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner=None

    return


def check_rows():
    global game_still_going
    row_1 = board[0]==board[1]==board[2]!= "_"
    row_2 = board[3]==board[4]==board[5]!= "_"
    row_3 = board[6]==board[7]==board[8]!= "_"
    if row_1 or row_2 or row_3:
        game_still_going=False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None


def check_columns():
    global game_still_going
    columns_1 = board[0]==board[3]==board[6] != "_"
    columns_2 = board[1]==board[4]==board[7]!= "_"
    columns_3 = board[2]==board[5]==board[8]!= "_"
    if columns_1 or columns_2 or columns_3:
        game_still_going=False
    if columns_1:
        return board[0]
    elif columns_2:
        return board[1]
    elif columns_3:
        return board[2]
    else:
        return None


def check_diagonals():
    global game_still_going

    diagonals_1 = board[0] == board[4] == board[8] != "_"
    diagonals_2 = board[2] == board[4] == board[6] != "_"
    if diagonals_1 or diagonals_2 :
        game_still_going = False
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[2]
    else:
        return None


def check_if_tie():
    global game_still_going
    if "_" not in board:
        game_still_going= False
    return
def flip_player():
    global current_player
    if current_player=="X":
        current_player="O"
    elif current_player=="O":
        current_player="X"
    return



play_game()
