from pygame import image
from Pieces.Bishop import Bishop
from Pieces.King import King
from Pieces.Knight import Knight
from Pieces.Pawn import Pawn
from Pieces.Queen import Queen
from Pieces.Rook import Rook

# piece instances
WP = Pawn('W')
WB = Bishop('W')
WN = Knight('W')
WK = King('W')
WQ = Queen('W')
WRL = Rook('W','L')
WRR = Rook('W','R')
BP = Pawn('B')
BB = Bishop('B')
BN = Knight('B')
BK = King('B')
BQ = Queen('B')
BRL = Rook('B','L')
BRR = Rook('B','R')


class Board:
    def __init__(self,image_id=0):
        self.size = (800,800)  # sample size
        self.center = (400, 400)
        self.background = image.load(f'Assets/Board/{image_id}.png')
        self.rect = self.background.get_rect(center = self.center)
        self.var = [
        [BRL , BN , BB , BQ , BK , BB , BN , BRR],
        [ BP , BP , BP , BP , BP , BP , BP , BP ],
        [None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None],
        [ WP , WP , WP , WP , WP , WP , WP , WP ],
        [WRL , WN , WB , WQ , WK , WB , WN , WRR]
        ]

    # address in tuple or list like (0,2) --> var[0][2]
    def variable_update(self,origin,destination,castling = False):
        # castling Rook move func
        def move_castling_rook():
            # castling direction extraction
            castling_direction = 'R' if destination[1] - origin[1] > 0 else 'L'

            # castling Rook's origin setup
            if castling_direction == 'L':
                crook_origin = (origin[0], 0)
            else:
                crook_origin = (origin[0], 7)

            # castling Rook's destination setup
            if castling_direction == 'L':
                crook_destination = (destination[0], destination[1] + 1)
            else:
                crook_destination = (destination[0], destination[1] - 1)

            # objects extraction
            king_piece = self.var[origin[0]][origin[1]]
            Rook_piece = self.var[crook_origin[0]][crook_origin[1]]
            # is_moved attributes update
            king_piece.is_moved = True
            Rook_piece.is_moved = True

            # move castling Rook
            self.var[crook_destination[0]][crook_destination[1]] = self.var[crook_origin[0]][crook_origin[1]]
            self.var[crook_origin[0]][crook_origin[1]] = None

        # castling move     
        if castling:
            # move castling Rook
            move_castling_rook()
            # move King
            self.var[destination[0]][destination[1]] = self.var[origin[0]][origin[1]]
            self.var[origin[0]][origin[1]] = None

        
        # regular move
        else:
            piece = self.var[origin[0]][origin[1]]
            if piece.type == 'K' or piece.type == 'R':
                piece.is_moved = True
            self.var[destination[0]][destination[1]] = self.var[origin[0]][origin[1]]
            self.var[origin[0]][origin[1]] = None

board = Board(image_id=1)
