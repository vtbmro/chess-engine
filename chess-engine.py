
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

'''

import chess

board = chess.Board()

print(board)
