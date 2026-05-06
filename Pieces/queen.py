from pygame import image
from Pieces.Piece import Piece

class Queen(Piece):
    def __init__(self,color):
        self.color = color
        self.type = 'Q'
        self.image = image.load(f'Assets/{color}_Queen.png')

    def get_valid_moves(self, board, position):
        valid_moves = []
        row, col = position

        # Queen = Rook directions + Bishop directions
        directions = [
            (-1, 0),  # up
            (+1, 0),  # down
            (0, -1),  # left
            (0, +1),  # right
            (-1, -1),  # up-left
            (-1, +1),  # up-right
            (+1, -1),  # down-left
            (+1, +1),  # down-right
        ]

        for row_dir, col_dir in directions:
            current_row = row + row_dir
            current_col = col + col_dir

            while 0 <= current_row <= 7 and 0 <= current_col <= 7:
                target = board.var[current_row][current_col]

                if target is None:
                    valid_moves.append((current_row, current_col))

                elif target.color != self.color:
                    valid_moves.append((current_row, current_col))  # capture
                    break

                else: break  # blocked by friendly piece

                current_row += row_dir
                current_col += col_dir

        return valid_moves