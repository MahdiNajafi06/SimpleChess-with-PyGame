def is_check(board, king, king_cordinate):
        current_row, current_col = king_cordinate

        Straight_directions = [
            (-1, 0)  # up
            (0, 1)  # right
            (1, 0)  # down
            (0, -1)  # left
        ]

        Diagonal_directions = [
            (-1, 1)  # up/right
            (1, 1)  # down/right
            (1, -1)  # down/left
            (-1, -1)  # up/left
        ]

        jumps = [
            (2, -1)  # 2down/1left
            (2, 1)  # 2down/1right
            (1, 2)  # 1down/2right
            (1, -2)  # 1down/2left
            (-1, 2)  # 1up/2right
            (-1, -2)  # 1up/2left
            (-2, 1)  # 2up/1right
            (-2, -1)  # 2up/1left
        ]

        pawn_directions = [
            (-1, 1)  # up/right
            (-1, -1)  # up/left
            (1, -1)  # down/left
            (1, 1)  # down/right
        ]


        for direction in Straight_directions:
            current_row += direction[0]
            current_col += direction[1]

            while 0 <= current_col <= 7 and 0 <= current_col <= 7:
                target = board[current_row][current_col]
                if target != None:
                    if target.color != king.color:
                        if target.type == 'R' or target.type == 'Q':
                            return True
                    else:
                        break
                current_row += direction[0]
                current_col += direction[1]

        for direction in Diagonal_directions:
            current_row += direction[0]
            current_col += direction[1]

            while 0 <= current_col <= 7 and 0 <= current_col <= 7:
                target = board[current_row][current_col]
                if target != None:
                    if target.color != king.color:
                        if target.type == 'B' or target.type == 'Q':
                            return True
                    else:
                        break
                current_row += direction[0]
                current_col += direction[1]

        for jump in jumps:
            current_row += direction[0]
            current_col += direction[1]

            if 0 <= current_col <= 7 and 0 <= current_col <= 7:
                target = board[current_row][current_col]
                if target != None:
                    if target.color != king.color:
                        if target.type == 'N':
                            return True

        count = 0
        for direction in pawn_directions:
            count += 1
            if (count <= 2 and king.color == 'W') or (count > 2 and king.color == 'B'):
                current_row += direction[0]
                current_col += direction[1]

                if 0 <= current_col <= 7 and 0 <= current_col <= 7:
                    target = board[current_row][current_col]
                    if target != None:
                        if target.color != king.color:
                            if target.type == 'P':
                                return True

def is_checkmate(board, king, king_cordinate):
        if is_check(board, king_cordinate, king) == True:
            king_valid_moves = king.get_valid_moves()
            n = len(king_valid_moves)
            out = 0
            for king_move in king_valid_moves:
                out = (out + 1) if check(board, king_move, king) == True else out
            if out == n:
                return True
        return False







