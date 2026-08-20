from pygame import image
from Game.rules import is_check
from Pieces.Piece import Piece,BoardSnapshot,find_king

class King(Piece):
    def __init__(self,color):
        self.color = color
        self.type = 'K'
        self.is_moved = False
        self.image = image.load(f'./Assets/{color}_King.png')

    def get_valid_moves(self, board, position):
        candidate_moves = []
        row, col = position

        # (row_direction, col_direction)
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

        # normal valid moves
        for row_dir, col_dir in directions:
            new_row = row + row_dir
            new_col = col + col_dir

            if 0 <= new_row <= 7 and 0 <= new_col <= 7:
                target = board.var[new_row][new_col]

                # Can move if square is empty or has an enemy piece
                if target is None or target.color != self.color:
                        # check-option needed here
                        candidate_moves.append((new_row, new_col))

        # (row_direction, col_direction)
        castling_directions = [
            (0, -1),  # left
            (0, +1),  # right
        ]

        # castling valid moves
        if self.is_moved == False:
            for row_dir, col_dir in castling_directions:
                current_row = row + row_dir
                current_col = col + col_dir

                while 0 <= current_col <= 7:
                    target = board.var[current_row][current_col]

                    if target is not None:
                        if target.color != self.color:
                            break
                        else: # target.color == self.color
                            if target.type == 'R':
                                if target.is_moved == False:
                                    if target.dir == 'L':
                                        candidate_moves.append((row, col-2))
                                    else: candidate_moves.append((row, col+2))
                            else: break

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