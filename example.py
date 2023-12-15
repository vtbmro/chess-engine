import chess
import copy
import math
from eval import evaluate
from search import minimax_alphabeta

chess_board = input("Enter a valid chess board FEN:")


board = chess.Board(f"{chess_board}")
print(board, "\n")


best_value, best_moves = minimax_alphabeta(board, 5, -math.inf, math.inf, True)

for move in best_moves:
    board.push_san(f"{move}")
    print(board)
    print("")

print(f"Board evaluation: {best_value}")