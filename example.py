import chess
import copy
import math
from eval import evaluate
from search import minimax_alphabeta

board = chess.Board("8/8/6pr/6p1/5pPk/5P1p/5P1K/R7")

print(board)
print("")

best_value, best_moves = minimax_alphabeta(board, 5, -math.inf, math.inf, True)


for move in best_moves:
    board.push_san(f"{move}")
    print(board)
    print("")

print(best_value)