import chess
import copy
import math
from eval import evaluate
from search import minimax_alphabeta

print("Input chess board FEN:")
chess_board = input()
board = chess.Board(f"{chess_board}")

print(board)
print("")

best_value, best_moves = minimax_alphabeta(board, 5, -math.inf, math.inf, True)


for move in best_moves:
    board.push_san(f"{move}")
    print(board)
    print("")

print(best_value)