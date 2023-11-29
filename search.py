import chess
import eval
from eval import evaluate
import copy
import math

"""
After thinking about a brute search approach to find the best move and arriving to the
conclussion of how brutally inneficient that would be. I found an algorithm online
called Minimax, which I will implement using alpha, beta pruning as well

Information for the function found at:
https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning#:~:text=Alpha%E2%80%93beta%20pruning%20is%20a,Connect%204%2C%20etc.).
"""

def minimax_alphabeta(node, depth, alpha, beta, isMaximizingPlayer):

# Base case OR game is over
    if depth == 0 or node.is_checkmate():
        
        return evaluate(node)

# Player is white
    if isMaximizingPlayer == True:
        value = -math.inf
        
# Iterate trough legal moves
        for child in list(node.legal_moves):

# Makes a deepcopy of the board, and then makes the move on the board
            temp = copy.deepcopy(node)
            temp.push_san(f"{child}")

            value = max(value, minimax_alphabeta(temp, depth -1, alpha, beta, False))

            if value > beta:
                break 

            alpha = max(alpha, value)

        return value

# Player is black 
    else:
        value = math.inf

# Iterate trough legal moves
        for child in list(node.legal_moves):

# Makes a deepcopy of the board, and then makes the move on the board
            temp = copy.deepcopy(node)
            temp.push_san(f"{child}")

            value = min(value, minimax_alphabeta(temp, depth -1, alpha, beta, True)) 

            if value < alpha:
                break

            beta = min(beta, value)

        return value      
    
# First call:
origin = chess.Board()
print(minimax_alphabeta(origin, 7, -math.inf, math.inf, True))

"""
I can think of some ways to improve efficiency: 
- Looking out for captures and checks increasing the chace for early cut offs
- Storing common positions, such as keeping a book of opening.
- The eval function could be optimized.
"""

"""
TODO: make it so that the function returns the line of moves, that leads to the
"best position" instead of the evaluation of the final position
"""