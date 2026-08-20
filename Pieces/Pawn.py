from pygame import image
from Game.rules import is_check
from Pieces.Piece import Piece,BoardSnapshot,find_king

class Pawn(Piece):
    def __init__(self,color):
        self.color = color
        self.type = 'P'
        self.image = image.load(f'./Assets/{color}_Pawn.png')

    def get_valid_moves(self, board, position):
        candidate_moves = []
        row, col = position

        # White pawns move UP (row decreases), Black pawns move DOWN (row increases)
        direction = -1 if self.color == 'W' else 1
        start_row = 6 if self.color == 'W' else 1

        # Forward move (1 square)
        new_row = row + direction
        if 0 <= new_row <= 7 and board.var[new_row][col] is None:
            candidate_moves.append((new_row, col))

            # Forward move (2 squares) only from starting row
            new_row2 = row + 2 * direction
            if row == start_row and board.var[new_row2][col] is None:
                candidate_moves.append((new_row2, col))

        # Diagonal captures
        for col_dir in [-1, 1]:
            capture_row = row + direction
            capture_col = col + col_dir
            if 0 <= capture_row <= 7 and 0 <= capture_col <= 7:
                target = board.var[capture_row][capture_col]

                if target is not None and target.color != self.color:
                    candidate_moves.append((capture_row, capture_col))

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