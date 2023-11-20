
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

white_pawn = [ 
0,  0,  0,  0,  0,  0,  0,  0,
50, 50, 50, 50, 50, 50, 50, 50,
10, 10, 20, 30, 30, 20, 10, 10,
 5,  5, 10, 25, 25, 10,  5,  5,
 0,  0,  0, 20, 20,  0,  0,  0,
 5, -5,-10,  0,  0,-10, -5,  5,
 5, 10, 10,-20,-20, 10, 10,  5,
 0,  0,  0,  0,  0,  0,  0,  0
 ]

white_knight = [
-50,-40,-30,-30,-30,-30,-40,-50,
-40,-20,  0,  0,  0,  0,-20,-40,
-30,  0, 10, 15, 15, 10,  0,-30,
-30,  5, 15, 20, 20, 15,  5,-30,
-30,  0, 15, 20, 20, 15,  0,-30,
-30,  5, 10, 15, 15, 10,  5,-30,
-40,-20,  0,  5,  5,  0,-20,-40,
-50,-40,-30,-30,-30,-30,-40,-50
]

white_bishop = [
-20,-10,-10,-10,-10,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  0,  5, 10, 10,  5,  0,-10,
-10,  5,  5, 10, 10,  5,  5,-10,
-10,  0, 10, 10, 10, 10,  0,-10,
-10, 10, 10, 10, 10, 10, 10,-10,
-10,  5,  0,  0,  0,  0,  5,-10,
-20,-10,-10,-10,-10,-10,-10,-20
]

white_rook = [
-20,-10,-10, -5, -5,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  0,  5,  5,  5,  5,  0,-10,
 -5,  0,  5,  5,  5,  5,  0, -5,
  0,  0,  5,  5,  5,  5,  0, -5,
-10,  5,  5,  5,  5,  5,  0,-10,
-10,  0,  5,  0,  0,  0,  0,-10,
-20,-10,-10, -5, -5,-10,-10,-20
]

white_king_middlegame = [
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-20,-30,-30,-40,-40,-30,-30,-20,
-10,-20,-20,-20,-20,-20,-20,-10,
 20, 20,  0,  0,  0,  0, 20, 20,
 20, 30, 10,  0,  0, 10, 30, 20
]

white_king_endgame = []

def evaluate(board):
    position = 0.0

# Correctly iterates trough the board
    for square in algebraic_notation:
        piece = board.piece_at(chess.parse_square(f"{square}"))

# Check if square has a piece
        if hasattr(piece, "piece_type"):

# Check if piece is white
            if piece.symbol().islower():
                
# Add value to position depending on piece

# White piece: add positive value to position acording to piece
                match piece.symbol():
                    case "p":
                        position += 100
                    case "n":
                        position += 320
                    case "b":
                        position += 330
                    case "r":
                        position += 500
                    case "q":
                        position += 900
                    case "k":
                        position += 2000

# Black piece: add negative value to position according to piece
            else:
                match piece.symbol():
                    case "P":
                        position -= 100
                    case "N":
                        position -= 320
                    case "B":
                        position -= 330
                    case "R":
                        position -= 500
                    case "Q":
                        position -= 900
                    case "K":
                        position -= 2000

    return position

"""
The problem is currently this evaluate function doesn't take into
account pieces position, for example a Knight located in the center
of the board controls more important squares than a kinght located at
the edge of the board
"""

print(evaluate(board))