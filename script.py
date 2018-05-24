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
    
    
