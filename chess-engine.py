import chess
import eval

board = chess.Board()

# Function need to takes as input a chess booard. Iterate trough 
# the board and check if piece is black/white after, that add to 
# position value depending on the piece position.

algebraic_notation = [
'a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8',
'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7',
'a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6', 
'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5',
'a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4',
'a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3',
'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2',
'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1'
]

"""
P = 100
N = 320
B = 330
R = 500
Q = 900
K = 2000
"""

def evaluate(board):
  position = 0

# TODO: add a check to see if the position is either a draw or checkmate.

# Iterate trough board
  for square in algebraic_notation:
    piece = board.piece_at(chess.parse_square(f"{square}"))

# Check if there is a piece in the square
    if hasattr(piece, "piece_type"):
      print(position)

# Piece is black   
      if piece.symbol().islower():
        if piece.symbol() == "p":
          position -= (100 + eval.black_pawn[square])
        elif piece.symbol() == "n":
          position -= (320 + eval.black_knight[square])
        elif piece.symbol() == "b":
          position -= (330 + eval.black_bishop[square])
        elif piece.symbol() == "r":
          position -= (500 + eval.black_rook[square])
        elif piece.symbol() == "q":
          position -= (900 + eval.black_queen[square])
        elif piece.symbol() == "k":
          position -= (2000 + eval.black_king[square])

# Piece is white
      elif piece.symbol().isupper():
        if piece.symbol() == "P":
          position += (100 + eval.white_pawn[square])
        elif piece.symbol() == "N":
          position += (320 + eval.white_knight[square])
        elif piece.symbol() == "B":
          position += (330 + eval.white_bishop[square])
        elif piece.symbol() == "R":
          position += (500 + eval.white_rook[square])
        elif piece.symbol() == "Q":
          position += (900 + eval.white_queen[square])
        elif piece.symbol() == "K":
          position += (2000 + eval.white_king[square])
        
# Return positive integer if position is favorable for white, negative if position is favorable for black
  return position


print(evaluate(board))



