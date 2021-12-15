#---------Variavel Global----------------#



#board

board = ["_","_","_",
         "_","_","_",
         "_","_","_"]

game_is_still_going=True
#display board

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])





#play game

def play_game():
    display_board()

    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

#handle turn
def handle_turn():
    position = int( input("Digite a posição de 1 a 9"))-1
    board[position] ="X"
    display_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()
#check win

def check_if_win():

    #check row
    #check collumns
    #check diagonals

#check tie

#flip Player
play_game()