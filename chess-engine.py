
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

# Added this to be able to traverse trough the board easily
algebraic_notation = [
'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1',
'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',
'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4',
'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5',
'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6',
'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7',
'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8'
]

def evaluate(board):
    position = 0

# Correctly iterates trough the board
    for square in algebraic_notation:
        piece = board.piece_at(chess.parse_square(f"{square}"))

# If square has a piece
        if hasattr(piece, "piece_type"):
            print(piece.symbol())

            


# White piece: add positive value to position acording to piece

# Black piece: add negative value to position according to piece

    return position

evaluate(board)