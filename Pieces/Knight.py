from pygame import image
from Pieces.Piece import Piece

class Knight(Piece):
    def __init__(self,color):
        self.color = color
        self.type = 'N'
        self.image = image.load(f'Assets/{color}_Knight.png')

    def get_valid_moves(self, board, position):
        valid_moves = []
        row, col = position

        # (row_direction, col_direction)
        jumps = [
            (-2, -1), (-2, +1),  # 2 up,   1 left/right
            (+2, -1), (+2, +1),  # 2 down, 1 left/right
            (-1, -2), (-1, +2),  # 1 up,   2 left/right
            (+1, -2), (+1, +2),  # 1 down, 2 left/right
        ]

        for row_jump, col_jump in jumps:
            new_row = row + row_jump
            new_col = col + col_jump

            if 0 <= new_row <= 7 and 0 <= new_col <= 7:
                target = board.var[new_row][new_col]

                # Can move if square is empty or has an enemy piece
                if target is None or target.color != self.color:
                    valid_moves.append((new_row, new_col))

        return valid_moves