#first let' create a board

def display_board(board):
    """This is a square board with 9 boxs"""
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
    
