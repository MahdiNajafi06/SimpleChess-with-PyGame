from pygame import image
from Game.rules import is_check
from Pieces.Piece import Piece,BoardSnapshot,find_king

class Rook(Piece):
    def __init__(self,color,direction = None):
        self.color = color
        self.type = 'R'
        self.dir = direction
        self.is_moved = False
        self.image = image.load(f'./Assets/{color}_Rook.png')

    def get_valid_moves(self, board, position):
        candidate_moves = []
        row, col = position

        # (row_direction, col_direction)
        directions = [
            (-1, 0),  # up
            (+1, 0),  # down
            (0, -1),  # left
            (0, +1),  # right
        ]

        for row_dir, col_dir in directions:
            current_row = row + row_dir
            current_col = col + col_dir

            # Keep going in this vertical & horizontal directions until out of the bounds
            while 0 <= current_row <= 7 and 0 <= current_col <= 7:
                target = board.var[current_row][current_col]
                if target is None:
                    candidate_moves.append((current_row, current_col))
                elif target.color != self.color:
                    candidate_moves.append((current_row, current_col))  # capture
                    break
                else: break  # blocked by friendly piece

                current_row += row_dir
                current_col += col_dir

        # keep only the candidates that don't leave your own king in check
        valid_moves = []
        for move in candidate_moves:
            if not self.move_causes_self_check(board, position, move):
                valid_moves.append(move)

        return valid_moves

    def move_causes_self_check(self, board, origin, destination):
        # simulate on a copy of the grid only — real board is never touched
        var_copy = [row[:] for row in board.var]  # taking the copy
        var_copy[destination[0]][destination[1]] = var_copy[origin[0]][origin[1]]
        var_copy[origin[0]][origin[1]] = None

        snapshot = BoardSnapshot(var_copy)
        king_pos = find_king(snapshot, self.color)
        return is_check(snapshot, king_pos)