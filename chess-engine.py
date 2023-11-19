
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
