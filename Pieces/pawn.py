from pygame import image
from Pieces.Piece import Piece

class Pawn(Piece):
    def __init__(self,color):
        self.color = color
        self.type = 'P'
        self.image = image.load(f'Assets/{color}_Pawn.png')

    def get_valid_moves(self, board, position):
        valid_moves = []
        row, col = position

        # White pawns move UP (row decreases), Black pawns move DOWN (row increases)
        direction = -1 if self.color == 'W' else 1
        start_row = 6 if self.color == 'W' else 1

        # Forward move (1 square)
        new_row = row + direction
        if 0 <= new_row <= 7 and board.var[new_row][col] is None:
            valid_moves.append((new_row, col))

            # Forward move (2 squares) only from starting row
            new_row2 = row + 2 * direction
            if row == start_row and board.var[new_row2][col] is None:
                valid_moves.append((new_row2, col))

        # Diagonal captures
        for col_dir in [-1, 1]:
            capture_row = row + direction
            capture_col = col + col_dir
            if 0 <= capture_row <= 7 and 0 <= capture_col <= 7:
                target = board.var[capture_row][capture_col]

                if target is not None and target.color != self.color:
                    valid_moves.append((capture_row, capture_col))

        return valid_moves