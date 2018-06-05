#comptible for python 3
#first let' create a board
from IPython.display import clear_output

def display_board(board):
    """This is a square board with 9 boxs"""
    clear_output
    print(" {} | {} | {} ".format(*board[1:4]))
    print("---|---|---")
    print(" {} | {} | {} ".format(*board[4:7]))
    print("---|---|---")
    print(" {} | {} | {} ".format(*board[7:10]))
    
#below is the function, which asks the player to choose 'X' or 'O'

def player_input():
    '''asks the player to select x or o.
    output = player1,player2'''
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('player1 is X or O: ').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
player1,player2 = player_input()

#this function moves the position in the board

def place_marker(board,marker,position):
    board[position]=marker
    
#below is the function to check who has won

def win_check(board,mark):
    '''if 3 boxs in a row are equal or 3 boxs in a column are equal or also diagnolly equal, then that player is the winner'''
    return ((board[1]==board[2]==board[3]==mark) or (board[4]==board[5]==board[6]==mark) or (board[7]==board[8]==board[9]==mark) or
    (board[1]==board[4]==board[7]==mark) or (board[2]==board[5]==board[8]==mark) or (board[3]==board[6]==board[9]==mark) or
    (board[1]==board[5]==board[9]==mark) or (board[7]==board[5]==board[3]==mark) )

#this function randomly chooses the first turn, either player1 or player2

import random

def choose_first():
    '''this function randomly chooses the first turn, either player1 or player2'''
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'player1'
    else:
        return 'player2'
    
    #function which checks for blank box 
    
def space_check(board,position):
    '''This is a function which checks for blank box in the game'''
    return board[position] == ' '

def full_board_check(board):
    
    #this function is for full board check of blank box
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True 

#below function asks for the players next position

def player_choice(board):
    '''OUTPUT = POSITION OF THE PLAYER'''
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('choose a position (1,9): '))
        
    return position

#Below function asks the player to play again

def replay():
    choice = input("Do u want to play?yes or no")
    return choice == 'yes'

  #last set of code using above function
    
print('Welcome to tic tactoe game')

#using while loop to continue with the game

while True:
    
    #first set everything up board,choose marker,who's first
    
    the_board = [' ']*10
    
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    
    print(turn + ' will go first')
    
    play_game = input('ready to play?y or n')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        if turn == 'player1':
            #show the board
            display_board(the_board)
            #chooose position
            position = player_choice(the_board)
            #place the marker on the position
            place_marker(the_board,player1_marker,position)
            #win check
            
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Player1 has won')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game!")
                    game_on = False
                else:
                    turn = 'player2'
        else:
            #show the board
            display_board(the_board)
            #chooose position
            position = player_choice(the_board)
            #place the marker on the position
            place_marker(the_board,player2_marker,position)
            #win check
            
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('Player2 has won')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game!")
                    game_on = False
                else:
                    turn = 'player1'
    if not replay():
        break    
