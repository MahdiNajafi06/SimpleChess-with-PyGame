from pygame import image
from Game.move import rowcol_to_crd

def draw_board(screen,Board_var):
    for row in range(8):
        for cul in range(8):
            if Board_var[row][cul] != None:
                obj = Board_var[row][cul]
                obj.rect = obj.image.get_rect(center=(rowcol_to_crd((row, cul))))
                screen.blit(obj.image, obj.rect)

def draw_valid_moves(screen, piece_valid_moves, Board_var):
    valid_image = image.load('Assets/Valid_place.png')
    for tpl in piece_valid_moves:
        valid_rect = valid_image.get_rect(center=rowcol_to_crd(tpl))
        screen.blit(valid_image,valid_rect)