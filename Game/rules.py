def is_check(board, king_position):
    king_row, king_col = king_position
    king = board.var[king_row][king_col]

    straight_directions = [
        (-1, 0),  # up
        (0, 1),   # right
        (1, 0),   # down
        (0, -1),  # left
    ]

    diagonal_directions = [
        (-1, 1),   # up-right
        (1, 1),    # down-right
        (1, -1),   # down-left
        (-1, -1),  # up-left
    ]

    jumps = [
        (2, -1),  # 2down/1left
        (2, 1),  # 2down/1right
        (1, 2),  # 1down/2right
        (1, -2),  # 1down/2left
        (-1, 2),  # 1up/2right
        (-1, -2),  # 1up/2left
        (-2, 1),  # 2up/1right
        (-2, -1)  # 2up/1left
    ]

    # rook / queen horizontal checks
    for row_dir, col_dir in straight_directions:
        current_row = king_row + row_dir
        current_col = king_col + col_dir

        while 0 <= current_row <= 7 and 0 <= current_col <= 7:
            target = board.var[current_row][current_col]
            if target is not None:
                if target.color != king.color and target.type in ('R', 'Q'):
                    return True
                break  # blocked — by a friendly piece, or a non-attacking enemy piece
            current_row += row_dir
            current_col += col_dir

    # bishop / queen along diagonals
    for row_dir, col_dir in diagonal_directions:
        current_row = king_row + row_dir
        current_col = king_col + col_dir

        while 0 <= current_row <= 7 and 0 <= current_col <= 7:
            target = board.var[current_row][current_col]
            if target is not None:
                if target.color != king.color and target.type in ('B', 'Q'):
                    return True
                break
            current_row += row_dir
            current_col += col_dir

    # knight jumps
    for row_jump, col_jump in jumps:
        current_row = king_row + row_jump
        current_col = king_col + col_jump

        if 0 <= current_row <= 7 and 0 <= current_col <= 7:
            target = board.var[current_row][current_col]
            if target is not None and target.color != king.color and target.type == 'N':
                return True

    # pawns — the two squares diagonally "ahead" of the king, from an attacker's point of view.
    # a white king is attacked by black pawns sitting one row above it (black pawns move down);
    # a black king is attacked by white pawns sitting one row below it (white pawns move up).
    pawn_row_dir = -1 if king.color == 'W' else 1
    for col_dir in (-1, 1):
        current_row = king_row + pawn_row_dir
        current_col = king_col + col_dir

        if 0 <= current_row <= 7 and 0 <= current_col <= 7:
            target = board.var[current_row][current_col]
            if target is not None and target.color != king.color and target.type == 'P':
                return True

    # king is safe
    return False


def is_checkmate(board, king, king_position):
    if is_check(board, king_position):
        king_valid_moves = king.get_valid_moves(board, king_position)
        if len(king_valid_moves) == 0:
            return True
    return False






