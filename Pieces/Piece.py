from abc import ABC,abstractmethod

class Piece(ABC):
    @abstractmethod
    def get_valid_moves(self):
        pass