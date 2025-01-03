"""
This file will contain display code to create the board and GUI using tkinter.
Author: Josh Pearlson
"""
"""
This file will contain display code to create the board and GUI using tkinter.
Author: Josh Pearlson
"""
import chess
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

# Initialize the main window
window = tk.Tk()
window.title('joshFish')
window.geometry('800x600')

# Define the size of the chessboard
BOARD_SIZE = 800
CELL_SIZE = BOARD_SIZE // 8

# Create a canvas for the chessboard
board_canvas = tk.Canvas(window, width=BOARD_SIZE, height=BOARD_SIZE, bg="white")
board_canvas.grid(row=0, column=0, padx=10, pady=10)

# Store the current board state
current_board = chess.Board()
selected_square = None

# Dictionary to store the PhotoImage objects
piece_images = {}
PIECE_PNG_PATH = "pieces_chess.com_neo"

def load_piece_images():
    """Load and resize all piece images from the specified directory"""
    piece_mapping = {
        'r': 'br', 'n': 'bn', 'b': 'bb', 'q': 'bq', 'k': 'bk', 'p': 'bp',
        'R': 'wr', 'N': 'wn', 'B': 'wb', 'Q': 'wq', 'K': 'wk', 'P': 'wp'
    }
    
    for piece_char, filename_prefix in piece_mapping.items():
        try:
            image_path = os.path.join(PIECE_PNG_PATH, f"{filename_prefix}.png")
            image = Image.open(image_path)
            # Resize the image to fit the cell size
            image = image.resize((CELL_SIZE, CELL_SIZE), Image.Resampling.LANCZOS)
            # Convert to PhotoImage and store in dictionary
            piece_images[piece_char] = ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Error loading image for {piece_char}: {e}")
            # Fallback to text if image loading fails
            pieces = {
                "r": "♜", "n": "♞", "b": "♝", "q": "♛", "k": "♚", "p": "♟",
                "R": "♖", "N": "♘", "B": "♗", "Q": "♕", "K": "♔", "P": "♙"
            }
            return pieces

# Function to draw the chessboard
def draw_chessboard():
    board_canvas.delete("all")
    for row in range(8):
        for col in range(8):
            color = "#D18B47" if (row + col) % 2 == 0 else "#FFCE9E"
            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            board_canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

def draw_pieces():
    """Draw pieces using PNG images"""
    for square, piece in current_board.piece_map().items():
        row = 7 - (square // 8)
        col = square % 8
        x = col * CELL_SIZE
        y = row * CELL_SIZE
        piece_char = str(piece)
        
        if piece_char in piece_images:
            board_canvas.create_image(
                x, y,
                image=piece_images[piece_char],
                anchor="nw"
            )
       

# Highlight possible moves
def highlight_moves(square):
    moves = list(current_board.legal_moves)
    for move in moves:
        if move.from_square == square:
            row = 7 - (move.to_square // 8)
            col = move.to_square % 8
            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            board_canvas.create_rectangle(x1, y1, x2, y2, outline="blue", width=3)

# Handle click events
def on_square_click(event):
    global selected_square
    col = event.x // CELL_SIZE
    row = event.y // CELL_SIZE
    clicked_square = (7 - row) * 8 + col
    
    if selected_square is None:
        # Select a piece and highlight moves
        if current_board.piece_at(clicked_square):
            selected_square = clicked_square
            highlight_moves(selected_square)
    else:
        # Attempt to move the piece
        move = chess.Move(selected_square, clicked_square)
        if move in current_board.legal_moves:
            current_board.push(move)
            selected_square = None
            draw_chessboard()
            draw_pieces()
        else:
            selected_square = None
            draw_chessboard()
            draw_pieces()

# Load the piece images before starting
load_piece_images()

# Bind the click event
board_canvas.bind("<Button-1>", on_square_click)

# Draw the chessboard and pieces
draw_chessboard()
draw_pieces()

# Create a frame on the right for controls and text boxes
control_frame = tk.Frame(window, width=200, height=BOARD_SIZE, bg="lightgray")
control_frame.grid(row=0, column=1, sticky="nsew")
control_frame.grid_propagate(False)

# Add sample text boxes and buttons to the control frame
text_box1 = tk.Text(control_frame, height=5, width=25)
text_box1.pack(pady=10)
text_box2 = tk.Text(control_frame, height=5, width=25)
text_box2.pack(pady=10)
button1 = ttk.Button(control_frame, text="Button 1")
button1.pack(pady=5)
button2 = ttk.Button(control_frame, text="Button 2")
button2.pack(pady=5)

# Run the Tkinter event loop
window.mainloop()