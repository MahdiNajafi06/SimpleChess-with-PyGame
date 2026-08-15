from pygame import image
from Game.rules import is_check
from Pieces.Piece import Piece,BoardSnapshot

class Knight(Piece):
    def __init__(self, color):
        self.color = color
        self.type = 'N'
        self.image = image.load(f'./Assets/{color}_Knight.png')

    def get_valid_moves(self, board, position):
        candidate_moves = []
        row, col = position

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
                    candidate_moves.append((new_row, new_col))

        # keep only the candidates that don't leave your own king in check
        valid_moves = []
        for move in candidate_moves:
            if not self.move_causes_self_check(board, position, move):
                valid_moves.append(move)

        return valid_moves

    def move_causes_self_check(self, board, origin, destination):
        # simulate on a copy of the grid only — real board is never touched
        var_copy = [row[:] for row in board.var] # taking the copy
        var_copy[destination[0]][destination[1]] = var_copy[origin[0]][origin[1]]
        var_copy[origin[0]][origin[1]] = None

        snapshot = BoardSnapshot(var_copy)
        king_pos = self.find_king(snapshot)
        return is_check(snapshot, king_pos)