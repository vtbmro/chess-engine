import chess
import copy
import math
from eval import evaluate
from search import minimax_alphabeta

chess_board = chess.Board()
board = chess.Board()

print(board)
print("")

best_value, best_moves = minimax_alphabeta(board, 5, -math.inf, math.inf, True)

for move in best_moves:
    board.push_san(f"{move}")
    print(board)
    print("")

print(best_value)