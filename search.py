import chess
import eval
from eval import evaluate

"""
After thinking about a brute search approach to find the best move and arriving to the
conclussion of how brutally inneficient that would be. I found an algorithm online
called Minimax, which I will implement using alpha, beta pruning as well

Information for the function found at:
https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning#:~:text=Alpha%E2%80%93beta%20pruning%20is%20a,Connect%204%2C%20etc.).
"""

def minimax_alphabeta(node, depth, alpha, beta, isMaximizingPlayer):

# Base case OR game is over
    if depth == 0 or node.gameisover():
        return evaluate(node)

# Player is white
    if isMaximizingPlayer == True:
        value = -10000

# Iterate trough legal moves
        for move in node.legalmoves():
            value = max(value, minimax_alphabeta(move, depth -1, alpha, beta, False))
            
            if value > beta:
                break

            alpha = max(alpha, value)

        return value

# Player is black 
    else:
        value = 10000

# Iterate trough legal moves
        for move in node.legalmoves():
            value = min(value, minimax_alphabeta(move, depth -1, alpha, beta, True)) 

            if value < alpha:
                break

            beta = min(beta, value)

        return value      
    

# First call:

origin = chess.Board()

minimax_alphabeta(origin, 3, -100000, 100000, True)

