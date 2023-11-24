import chess
import eval
from eval import evaluate


"""
"""

def minimax(node, depth, isMaximizingPlayer, alpha, beta):
    if depth == 0 or game.isover() == true:
        return evaluate(node)

    # White 
    if isMaximizingPlayer:
        bestVal = -10000 
        for move in legalmoves:
            value = minimax(node, depth+1, false, alpha, beta)
            bestVal = max( bestVal, value) 
            alpha = max( alpha, bestVal)
            if beta <= alpha:
                break
        return bestVal

    else:
        bestVal = 1000
        for move in legalmoves:
            value = minimax(node, depth+1, true, alpha, beta)
            bestVal = min( bestVal, value) 
            beta = min( beta, bestVal)
            if beta <= alpha:
                break
        return bestVal