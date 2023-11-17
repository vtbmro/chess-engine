
'''
My idea is to combine both my final project of CS50x and CS50w by building an
engine in python and the building a interactive web page where users can use 
the engine to analyze postions

1. A engine comes with two functions: a Search function and an Evaluate function, 
While evaluating, a chess engine looks at all pieces and ascertains the position 
that would be better for each. During this process, all chess engines display 
something called an eval.

The first question is quite simple, how do we represent a chess board while we could
use a bitboard for a more efficient aproach I found a chess module that already comes 
with a built in function to represent the function, if in the future the program
becomes too slow I might have to switch to a bitboard

The board looks like this:

r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R

Now that we have the module at our disposal we have plenty of built in functionality
like moving pieces, or checking if the board is stalemate. Still we need to build
a function that takes as an argument a chess board and returns an evaluation as well
as the correct move to play
'''

import chess

# Represent a chess board
board = chess.Board()

# Function takes as input a board
def evaluate (board):

# White mates: positive integer    
    if board.white_mated():
        return 1000
    
# Black mates: negative integer
    if board.black_mated():
        return -1000
    
# Draw = 0
    if board.is_draw():
        return 0

    pass

'''
But this cases above are quite simple (The game is basically over)
Yet how can we evaluate more complex and less clear positions we could start by 
asiging values for each of the pieces, using the standard values
like pawn:1, knight:3, bishop: 3.15 (fisher value), rook:5, queen: 9.

Than we could add up all the white pieces and the black pieces and substract each other
getting a score
'''

# TODO: each function should return a total of the material of each player taking
# as input a chess board

def black_material(board):

    # Store the pieces
    black_pieces = []

    # Iterate trough the board
    for piece in board.items():
        print(piece)

    return print(black_pieces)

def white_material(board):
    return 0

black_material(board)

