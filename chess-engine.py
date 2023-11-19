
'''
My idea is to combine both my final project of CS50x and CS50w by building an
engine in python and the building a interactive web page where users can use 
the engine to analyze postions

I will be using chessprogramming.org as a guide.  

Generally the first step in building a chess engine is board representation, 
Basically the back end of this program, a way to keep track of the board and the 
rules of the game. But since we are using python I think it is appropriate to 
just focus on the higher level program and just use the chess module for simplication 
'''


import chess

board = chess.Board()
print(board.legal_moves)


"""
Now we need to create a function that evaluates the board, basically 
a function that takes as input a chess board and returns a positive
integer is the position is favorable for white or a negative integer
if the position is favorable for black (or near 0 if equal)
"""



def evaluate(board):
    position = 0
    # Iterate trough the board

    # If piece white add positive integer 

    # 

    return position