"""
This file will be a very simple implementation of a chess game using the python-chess library to get a good feel for how things work. This will be well commented if you are interested in working with this library in the future it could be a good starting point. 
Author: Josh Pearlson
"""
import chess as ch

# Frist thing I am going to do there is figure out how the chess library works by playing a game with myself using input() in the CLI and all the built in functions 

def startGame():
    """
    This method will actually play a game of chess using the chess library along with user inputs
    """
    board = ch.Board()

    while not board.is_game_over():
        print(board)

        uci_resp = input("Make your move in UCI:")

        try:    
            uci_move = ch.Move.from_uci(uci_resp)
        except ValueError:
            print("You have made a non valid UCI move. please try again")
            continue 
        
        print(uci_move, end = '\n\n')

        # NOTE: Board.push() expects UCI and makes psuedo legal moves we need to check legalMoveGenerator if we want to make only legal moves
        if uci_move not in board.legal_moves:
            print(f"{uci_move} is not a legal move.")
            continue

        board.push(uci_move)

 
while True:
    resp = input("Welcome to ChessBot, play a game? (y,n)") 

    if resp == 'y':
        startGame()
    elif resp == 'n':
        print("Thanks for using ChessBot, goodbye!")
        break
    else:
        print("Failed to recognize input, please answer from the following choices ('y','n').\n")

   
