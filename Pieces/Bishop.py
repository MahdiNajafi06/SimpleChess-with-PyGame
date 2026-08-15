from pygame import image
from Game.rules import is_check
from Pieces.Piece import Piece,BoardSnapshot

class Bishop(Piece):
    def __init__(self,color):
        self.color = color # must be 'W' or 'B'
        self.type = 'B'
        self.image = image.load(f'./Assets/{color}_Bishop.png')

    def get_valid_moves(self, board, position):
        candidate_moves = []
        row, col = position

        # (row_direction, col_direction)
        directions = [
            (-1, -1),  # up-left
            (-1, +1),  # up-right
            (+1, -1),  # down-left
            (+1, +1),  # down-right
        ]

        for row_dir, col_dir in directions:
            current_row = row + row_dir
            current_col = col + col_dir

            # Keep going in this diagonal direction until out of bounds
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
        king_pos = self.find_king(snapshot)
        return is_check(snapshot, king_pos)