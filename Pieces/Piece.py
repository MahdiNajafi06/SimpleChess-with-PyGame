from abc import ABC,abstractmethod

class Piece(ABC):
    @abstractmethod
    def get_valid_moves(self):
        pass

    @abstractmethod
    def move_causes_self_check(self):
        pass

    def find_king(self, board):
        for row in range(8):
            for col in range(8):
                if board.var[row][col]:
                    if board.var[row][col].type == 'K' and board.var[row][col].color == self.color:
                        #print((row, col))
                        return (row, col)

class BoardSnapshot:
    '''the reason of this class is that we cant simply get a copy from board.var and check
    that move would cause self discovering-check or not, we need to take the copy independently so the
    independent copy would no longer be a Board class instance. so we need to simulate this class
    to call copy.var'''
    def __init__(self, var):
        self.var = var
