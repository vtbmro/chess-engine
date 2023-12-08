# SIMPLE CHESS ENGINE
### Video Demo: <URL HERE>
### Description: 
this is a simple a chess engine using the python chess module, it has 2 main files
search ande eval. The eval file contains an evaluation function that takes as input
a chess board and returns a integer, the more positive the better for white the more
negative the better for black

Also you will find a lot of dicts, for each of the pieces and color that was added
to help the search function make better and more natural moves, valuing better positioned pieces higher.

The search file contains a minimax function based on alpha beta pruning, that
basically finds the best move for the inputted player in that position by returning the best sequence of moves and a value for the evaluation of the final position.

Notes: this engine lack the complexity of major chess engines, it can solve simple problmes like a mate in 3, and make generally positional sensible moves, but it falls apart some times. There are notes on possible improvement in the seach.py file. 