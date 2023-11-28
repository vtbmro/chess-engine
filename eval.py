import chess

"""
The dicts under this comment cotain values that help the eval function accurately
assess the board using the position of each piece, the better positioned a piece is
the higher its value will be, the oppsite is also true.

The table information I got from: https://www.chessprogramming.org/Simplified_Evaluation_Function
"""

# PAWN

white_pawn = {
  'a8': 0, 'b8': 0, 'c8': 0, 'd8': 0, 'e8': 0, 'f8': 0, 'g8': 0, 'h8': 0, 
  'a7': 50, 'b7': 50, 'c7': 50, 'd7': 50, 'e7': 50, 'f7': 50, 'g7': 50, 'h7': 50, 
  'a6': 10, 'b6': 10, 'c6': 20, 'd6': 30, 'e6': 30, 'f6': 20, 'g6': 10, 'h6': 10, 
  'a5': 5, 'b5': 5, 'c5': 10, 'd5': 25, 'e5': 25, 'f5': 10, 'g5': 5, 'h5': 5, 
  'a4': 0, 'b4': 0, 'c4': 0, 'd4': 20, 'e4': 20, 'f4': 0, 'g4': 0, 'h4': 0, 
  'a3': 5, 'b3': -5, 'c3': -10, 'd3': 0, 'e3': 0, 'f3': -10, 'g3': -5, 'h3': 5, 
  'a2': 5, 'b2': 10, 'c2': 10, 'd2': -20, 'e2': -20, 'f2': 10, 'g2': 10, 'h2': 5, 
  'a1': 0, 'b1': 0, 'c1': 0, 'd1': 0, 'e1': 0, 'f1': 0, 'g1': 0, 'h1': 0
}

black_pawn = {
  'a8': 0, 'b8': 0, 'c8': 0, 'd8': 0, 'e8': 0, 'f8': 0, 'g8': 0, 'h8': 0, 
  'a7': 5, 'b7': 10, 'c7': 10, 'd7': -20, 'e7': -20, 'f7': 10, 'g7': 10, 'h7': 5, 
  'a6': 5, 'b6': -5, 'c6': -10, 'd6': 0, 'e6': 0, 'f6': -10, 'g6': -5, 'h6': 5, 
  'a5': 0, 'b5': 0, 'c5': 0, 'd5': 20, 'e5': 20, 'f5': 0, 'g5': 0, 'h5': 0, 
  'a4': 5, 'b4': 5, 'c4': 10, 'd4': 25, 'e4': 25, 'f4': 10, 'g4': 5, 'h4': 5, 
  'a3': 10, 'b3': 10, 'c3': 20, 'd3': 30, 'e3': 30, 'f3': 20, 'g3': 10, 'h3': 10, 
  'a2': 50, 'b2': 50, 'c2': 50, 'd2': 50, 'e2': 50, 'f2': 50, 'g2': 50, 'h2': 50, 
  'a1': 0, 'b1': 0, 'c1': 0, 'd1': 0, 'e1': 0, 'f1': 0, 'g1': 0, 'h1': 0
}

# KNIGHT

white_knight = {
  'a8': -50, 'b8': -40, 'c8': -30, 'd8': -30, 'e8': -30, 'f8': -30, 'g8': -40, 'h8': -50, 
  'a7': -40, 'b7': -20, 'c7': 0, 'd7': 0, 'e7': 0, 'f7': 0, 'g7': -20, 'h7': -40, 
  'a6': -30, 'b6': 0, 'c6': 10, 'd6': 15, 'e6': 15, 'f6': 10, 'g6': 0, 'h6': -30, 
  'a5': -30, 'b5': 5, 'c5': 15, 'd5': 20, 'e5': 20, 'f5': 15, 'g5': 5, 'h5': -30, 
  'a4': -30, 'b4': 0, 'c4': 15, 'd4': 20, 'e4': 20, 'f4': 15, 'g4': 0, 'h4': -30, 
  'a3': -30, 'b3': 5, 'c3': 10, 'd3': 15, 'e3': 15, 'f3': 10, 'g3': 5, 'h3': -30, 
  'a2': -40, 'b2': -20, 'c2': 0, 'd2': 5, 'e2': 5, 'f2': 0, 'g2': -20, 'h2': -40, 
  'a1': -50, 'b1': -40, 'c1': -30, 'd1': -30, 'e1': -30, 'f1': -30, 'g1': -40, 'h1': -50
  }

black_knight = {
  'a8': -50, 'b8': -40, 'c8': -30, 'd8': -30, 'e8': -30, 'f8': -30, 'g8': -40, 'h8': -50, 
  'a7': -40, 'b7': -20, 'c7': 0, 'd7': 5, 'e7': 5, 'f7': 0, 'g7': -20, 'h7': -40, 
  'a6': -30, 'b6': 5, 'c6': 10, 'd6': 15, 'e6': 15, 'f6': 10, 'g6': 5, 'h6': -30, 
  'a5': -30, 'b5': 0, 'c5': 15, 'd5': 20, 'e5': 20, 'f5': 15, 'g5': 0, 'h5': -30, 
  'a4': -30, 'b4': 5, 'c4': 15, 'd4': 20, 'e4': 20, 'f4': 15, 'g4': 5, 'h4': -30, 
  'a3': -30, 'b3': 0, 'c3': 10, 'd3': 15, 'e3': 15, 'f3': 10, 'g3': 0, 'h3': -30, 
  'a2': -40, 'b2': -20, 'c2': 0, 'd2': 0, 'e2': 0, 'f2': 0, 'g2': -20, 'h2': -40, 
  'a1': -50, 'b1': -40, 'c1': -30, 'd1': -30, 'e1': -30, 'f1': -30, 'g1': -40, 'h1': -50
  }

#BISHOP

white_bishop = {
  'a8': -20, 'b8': -10, 'c8': -10, 'd8': -10, 'e8': -10, 'f8': -10, 'g8': -10, 'h8': -20, 
  'a7': -10, 'b7': 0, 'c7': 0, 'd7': 0, 'e7': 0, 'f7': 0, 'g7': 0, 'h7': -10, 
  'a6': -10, 'b6': 0, 'c6': 5, 'd6': 10, 'e6': 10, 'f6': 5, 'g6': 0, 'h6': -10, 
  'a5': -10, 'b5': 5, 'c5': 5, 'd5': 10, 'e5': 10, 'f5': 5, 'g5': 5, 'h5': -10, 
  'a4': -10, 'b4': 0, 'c4': 10, 'd4': 10, 'e4': 10, 'f4': 10, 'g4': 0, 'h4': -10, 
  'a3': -10, 'b3': 10, 'c3': 10, 'd3': 10, 'e3': 10, 'f3': 10, 'g3': 10, 'h3': -10, 
  'a2': -10, 'b2': 5, 'c2': 0, 'd2': 0, 'e2': 0, 'f2': 0, 'g2': 5, 'h2': -10, 
  'a1': -20, 'b1': -10, 'c1': -10, 'd1': -10, 'e1': -10, 'f1': -10, 'g1': -10, 'h1': -20
  }


black_bishop = {
  'a8': -20, 'b8': -10, 'c8': -10, 'd8': -10, 'e8': -10, 'f8': -10, 'g8': -10, 'h8': -20, 
  'a7': -10, 'b7': 5, 'c7': 0, 'd7': 0, 'e7': 0, 'f7': 0, 'g7': 5, 'h7': -10, 
  'a6': -10, 'b6': 10, 'c6': 10, 'd6': 10, 'e6': 10, 'f6': 10, 'g6': 10, 'h6': -10, 
  'a5': -10, 'b5': 0, 'c5': 10, 'd5': 10, 'e5': 10, 'f5': 10, 'g5': 0, 'h5': -10, 
  'a4': -10, 'b4': 5, 'c4': 5, 'd4': 10, 'e4': 10, 'f4': 5, 'g4': 5, 'h4': -10, 
  'a3': -10, 'b3': 0, 'c3': 5, 'd3': 10, 'e3': 10, 'f3': 5, 'g3': 0, 'h3': -10, 
  'a2': -10, 'b2': 0, 'c2': 0, 'd2': 0, 'e2': 0, 'f2': 0, 'g2': 0, 'h2': -10, 
  'a1': -20, 'b1': -10, 'c1': -10, 'd1': -10, 'e1': -10, 'f1': -10, 'g1': -10, 'h1': -20
  }

#ROOK

white_rook = {
  'a8': 0, 'b8': 0, 'c8': 0, 'd8': 0, 'e8': 0, 'f8': 0, 'g8': 0, 'h8': 0, 
  'a7': 5, 'b7': 10, 'c7': 10, 'd7': 10, 'e7': 10, 'f7': 10, 'g7': 10, 'h7': 5, 
  'a6': -5, 'b6': 0, 'c6': 0, 'd6': 0, 'e6': 0, 'f6': 0, 'g6': 0, 'h6': -5, 
  'a5': -5, 'b5': 0, 'c5': 0, 'd5': 0, 'e5': 0, 'f5': 0, 'g5': 0, 'h5': -5, 
  'a4': -5, 'b4': 0, 'c4': 0, 'd4': 0, 'e4': 0, 'f4': 0, 'g4': 0, 'h4': -5, 
  'a3': -5, 'b3': 0, 'c3': 0, 'd3': 0, 'e3': 0, 'f3': 0, 'g3': 0, 'h3': -5, 
  'a2': -5, 'b2': 0, 'c2': 0, 'd2': 0, 'e2': 0, 'f2': 0, 'g2': 0, 'h2': -5, 
  'a1': 0, 'b1': 0, 'c1': 0, 'd1': 5, 'e1': 5, 'f1': 0, 'g1': 0, 'h1': 0
  }

black_rook = {
  'a8': 0, 'b8': 0, 'c8': 0, 'd8': 5, 'e8': 5, 'f8': 0, 'g8': 0, 'h8': 0, 
  'a7': -5, 'b7': 0, 'c7': 0, 'd7': 0, 'e7': 0, 'f7': 0, 'g7': 0, 'h7': -5, 
  'a6': -5, 'b6': 0, 'c6': 0, 'd6': 0, 'e6': 0, 'f6': 0, 'g6': 0, 'h6': -5, 
  'a5': -5, 'b5': 0, 'c5': 0, 'd5': 0, 'e5': 0, 'f5': 0, 'g5': 0, 'h5': -5, 
  'a4': -5, 'b4': 0, 'c4': 0, 'd4': 0, 'e4': 0, 'f4': 0, 'g4': 0, 'h4': -5, 
  'a3': -5, 'b3': 0, 'c3': 0, 'd3': 0, 'e3': 0, 'f3': 0, 'g3': 0, 'h3': -5, 
  'a2': 5, 'b2': 10, 'c2': 10, 'd2': 10, 'e2': 10, 'f2': 10, 'g2': 10, 'h2': 5, 
  'a1': 0, 'b1': 0, 'c1': 0, 'd1': 0, 'e1': 0, 'f1': 0, 'g1': 0, 'h1': 0}

# QUEEN

white_queen= {
  'a8': -20, 'b8': -10, 'c8': -10, 'd8': -5, 'e8': -5, 'f8': -10, 'g8': -10, 'h8': -20, 
  'a7': -10, 'b7': 0, 'c7': 0, 'd7': 0, 'e7': 0, 'f7': 0, 'g7': 0, 'h7': -10, 
  'a6': -10, 'b6': 0, 'c6': 5, 'd6': 5, 'e6': 5, 'f6': 5, 'g6': 0, 'h6': -10, 
  'a5': -5, 'b5': 0, 'c5': 5, 'd5': 5, 'e5': 5, 'f5': 5, 'g5': 0, 'h5': -5, 
  'a4': 0, 'b4': 0, 'c4': 5, 'd4': 5, 'e4': 5, 'f4': 5, 'g4': 0, 'h4': -5, 
  'a3': -10, 'b3': 5, 'c3': 5, 'd3': 5, 'e3': 5, 'f3': 5, 'g3': 0, 'h3': -10, 
  'a2': -10, 'b2': 0, 'c2': 5, 'd2': 0, 'e2': 0, 'f2': 0, 'g2': 0, 'h2': -10, 
  'a1': -20, 'b1': -10, 'c1': -10, 'd1': -5, 'e1': -5, 'f1': -10, 'g1': -10, 'h1': -20
   }

black_queen = {
  'a8': -20, 'b8': -10, 'c8': -10, 'd8': -5, 'e8': -5, 'f8': -10, 'g8': -10, 'h8': -20, 
  'a7': -10, 'b7': 0, 'c7': 5, 'd7': 0, 'e7': 0, 'f7': 0, 'g7': 0, 'h7': -10, 
  'a6': -10, 'b6': 5, 'c6': 5, 'd6': 5, 'e6': 5, 'f6': 5, 'g6': 0, 'h6': -10, 
  'a5': 0, 'b5': 0, 'c5': 5, 'd5': 5, 'e5': 5, 'f5': 5, 'g5': 0, 'h5': -5, 
  'a4': -5, 'b4': 0, 'c4': 5, 'd4': 5, 'e4': 5, 'f4': 5, 'g4': 0, 'h4': -5, 
  'a3': -10, 'b3': 0, 'c3': 5, 'd3': 5, 'e3': 5, 'f3': 5, 'g3': 0, 'h3': -10, 
  'a2': -10, 'b2': 0, 'c2': 0, 'd2': 0, 'e2': 0, 'f2': 0, 'g2': 0, 'h2': -10, 
  'a1': -20, 'b1': -10, 'c1': -10, 'd1': -5, 'e1': -5, 'f1': -10, 'g1': -10, 'h1': -20
  }


# KING

white_king = {
  'a8': -30, 'b8': -40, 'c8': -40, 'd8': -50, 'e8': -50, 'f8': -40, 'g8': -40, 'h8': -30, 
  'a7': -30, 'b7': -40, 'c7': -40, 'd7': -50, 'e7': -50, 'f7': -40, 'g7': -40, 'h7': -30, 
  'a6': -30, 'b6': -40, 'c6': -40, 'd6': -50, 'e6': -50, 'f6': -40, 'g6': -40, 'h6': -30, 
  'a5': -30, 'b5': -40, 'c5': -40, 'd5': -50, 'e5': -50, 'f5': -40, 'g5': -40, 'h5': -30, 
  'a4': -20, 'b4': -30, 'c4': -30, 'd4': -40, 'e4': -40, 'f4': -30, 'g4': -30, 'h4': -20, 
  'a3': -10, 'b3': -20, 'c3': -20, 'd3': -20, 'e3': -20, 'f3': -20, 'g3': -20, 'h3': -10, 
  'a2': 20, 'b2': 20, 'c2': 0, 'd2': 0, 'e2': 0, 'f2': 0, 'g2': 20, 'h2': 20, 
  'a1': 20, 'b1': 30, 'c1': 10, 'd1': 0, 'e1': 0, 'f1': 10, 'g1': 30, 'h1': 20
  }

black_king = {
  'a8': 20, 'b8': 30, 'c8': 10, 'd8': 0, 'e8': 0, 'f8': 10, 'g8': 30, 'h8': 20, 
  'a7': 20, 'b7': 20, 'c7': 0, 'd7': 0, 'e7': 0, 'f7': 0, 'g7': 20, 'h7': 20, 
  'a6': -10, 'b6': -20, 'c6': -20, 'd6': -20, 'e6': -20, 'f6': -20, 'g6': -20, 'h6': -10, 
  'a5': -20, 'b5': -30, 'c5': -30, 'd5': -40, 'e5': -40, 'f5': -30, 'g5': -30, 'h5': -20, 
  'a4': -30, 'b4': -40, 'c4': -40, 'd4': -50, 'e4': -50, 'f4': -40, 'g4': -40, 'h4': -30, 
  'a3': -30, 'b3': -40, 'c3': -40, 'd3': -50, 'e3': -50, 'f3': -40, 'g3': -40, 'h3': -30, 
  'a2': -30, 'b2': -40, 'c2': -40, 'd2': -50, 'e2': -50, 'f2': -40, 'g2': -40, 'h2': -30, 
  'a1': -30, 'b1': -40, 'c1': -40, 'd1': -50, 'e1': -50, 'f1': -40, 'g1': -40, 'h1': -30
  }

"""
Under this funtion I implemented a evaluate function that takes as input a board
and returns a integer, positive if the position favors white and negative if the position 
favor black.
"""

board = chess.Board()

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

# Function to get each pieces value
def piece_value(square, board):

  piece = board.piece_at(chess.parse_square(f"{square}"))
  
  if hasattr(piece, "piece_type"):
      
# Piece is black   
    if piece.symbol().islower():

      if piece.symbol() == "p":
        return -(100 + black_pawn[square])

      elif piece.symbol() == "n":
        return -(320 + black_knight[square])

      elif piece.symbol() == "b":
        return -(330 + black_bishop[square])

      elif piece.symbol() == "r":
        return -(500 + black_rook[square])

      elif piece.symbol() == "q":
        return -(900 + black_queen[square])

      elif piece.symbol() == "k":
        return -(2000 + black_king[square])

# Piece is white
    elif piece.symbol().isupper():

      if piece.symbol() == "P":
        return (100 + white_pawn[square])

      elif piece.symbol() == "N":
        return (320 + white_knight[square])

      elif piece.symbol() == "B":
        return (330 + white_bishop[square])

      elif piece.symbol() == "R":
        return (500 + white_rook[square])

      elif piece.symbol() == "Q":
        return (900 + white_queen[square])

      elif piece.symbol() == "K":
        return (2000 + white_king[square])

  else: 
    return 0

# Function that evaluates the board
def evaluate(board):
  position = 0

# Check if position is mate
  if board.is_checkmate():

# White mate
    if board.turn == True:
      position = -2000
      return position
    
# Black mate
    elif board.turn == False:
      postion = 2000
      return postion
    
# Draw of stalemate
  elif board.is_stalemate() or board.is_insufficient_material():
    position = 0
    return position

# Iterate trough board and get value for each piece
  for square in algebraic_notation:
    position += piece_value(square, board)
      
  return position 

"""
Looking back it would have made more sense to code this in C since it would have been
10x faster, but at the same time coding it in python in python with the module does 
allow me to focues on the higher level implemantation.
"""

board = chess.Board()
print(evaluate(board))