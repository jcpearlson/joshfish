"""
This will use python-chess module to create a custom chess engine!
Author: Josh Pearlson
"""
import chess

class engine:
    def __init__(self):
        self.board = chess.Board()

    def eval_function(self, board):
        # simple eval function that just simply counts white-black pieces
        white_pieces = sum(len(board.pieces(pt, chess.WHITE)) for pt in chess.PIECE_TYPES)
        black_pieces = sum(len(board.pieces(pt, chess.BLACK)) for pt in chess.PIECE_TYPES)

        return white_pieces - black_pieces

    def iterative_deepening(self,depth=4, alpha=-float('inf'),beta=float('inf')):
        """
        This function will use iterative deepening to find the best move for the current board state.
        """
        return NotImplemented

    def alpha_beta_search(self, depth, alpha, beta):    
        """
        This function will use alpha-beta pruning to find the best move for the current board state.
        """
        return NotImplemented


if __name__ == "__main__":
    board = engine()

