# SIMPLE CHESS ENGINE
#### Video Demo: https://www.youtube.com/watch?v=ODaDx3Qb0Yg
#### Description: 
My name is Vicente Bravo Miranda, I'am from Haro la Rioja Spain and this is my final project for CS50x. My idea was to build a chess engine, basically a program that calculates the best move for a player given a X chess position.

My reason to build the program using python instead of C, was to abstract away the more complex problems, such as board representation, move generation for each piece castling etc... And just be able to focus on the higher level implementaions that are basically 2 files: search.py and eval.py.

Eval.py consists of 2 parts, the first is a long list of dicts for each piece and color, that basically allows the program to make natural moves and position its pieces better in the chess board. Centering the pawns, kinghts, keeping the king tucked away in the corners.

Then the evaluate function takes as input a chess board, it iterates trough every square in the board, taking into account all the pieces and their position using the dicts. Finally returning an integer, the higher this integer is the better the position is for white, and the more negative it is the beter is the position is for black the more negative the integer will be. There is also a +2000 evaluation meaning that white has mate and -2000 if black has mate.

The second part is the search.py file, this file basically contains a alphabeta minimax algorithm that iterates trough all the legal moves in the position for N depth when desired depth is reached the function evaluates the position.It returns the best sequence of moves in the position (n long), and also the final evaluation of the position.

Notes, the engine lacks the complexity of bigger chess engines like stockfish, some major improvements would be the addition of a opening book, so the engine would have a better time during openings, also pruning based of captures, and checks. It also run relatively slow if the minimax alphabeta algo is given an depth value 6 or bigger, maybe rewritting the program in a language that is more efficient (Java, C, C++) would greatly benefit the speed of the program.

