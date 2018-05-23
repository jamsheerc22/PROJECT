
def display_board(board):
    """This is a square board with 9 boxs"""
    print(" {} | {} | {} ".format(*board[1:3]))
    print("---|---|---")
    print(" {} | {} | {} ".format(*board[3:6]))
    print("---|---|---")
    print(" {} | {} | {} ".format(*board[6:9]))
    
