import pygame
from sys import exit
from Game.board import board
from Game.move import crd_to_rowcol
from Game.rules import is_check,is_checkmate,is_stalemate
from Pieces.Piece import find_king
from UI.board_renderer import draw_board, draw_valid_moves, set_on_mouse_hover


pygame.init()
screen = pygame.display.set_mode(board.size)
pygame.display.set_caption('Chess')
clock = pygame.time.Clock()

def give_second_MOUSEBUTTONDOWN():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_crd = pygame.mouse.get_pos()
                return pos_crd
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

# start turn
turn = 'W'


# click-state
selected_pos = None      # rowcol of the currently selected piece, or None
selected_piece = None    # the piece obj currently selected, or None
valid_moves = []         # cached valid moves for the selected piece
#TOTAL_TIME = 300  # total time in seconds (5 minutes)
#start_time = pygame.time.get_ticks()


# main loop
while True:
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # origin setup
            origin_crd = pygame.mouse.get_pos()
            origin_pos = crd_to_rowcol(origin_crd)

            if board.var[origin_pos[0]][origin_pos[1]] != None and board.var[origin_pos[0]][origin_pos[1]].color == turn:
                # origin valid_moves setup
                origin_piece = board.var[origin_pos[0]][origin_pos[1]]
                origin_valid_moves = origin_piece.get_valid_moves(board,origin_pos)
                draw_valid_moves(screen, origin_valid_moves, board.var)
                draw_board(screen, board.var)
                pygame.display.update()
                # destination setup
                destination_crd = give_second_MOUSEBUTTONDOWN()
                destination_pos = crd_to_rowcol(destination_crd)

                # move validation
                if destination_pos in origin_valid_moves:
                    # check for castling
                    if origin_piece.type == 'K':
                        if destination_pos[1] - origin_pos[1] not in [2, -2]:
                            # regular move
                            board.variable_update(origin_pos, destination_pos)
                        else:
                            # castling move
                            board.variable_update(origin_pos, destination_pos, True)

                    # regular move
                    else: board.variable_update(origin_pos, destination_pos)
                    turn = 'B' if turn == 'W' else 'W'

    # drawing funcs
    screen.blit(board.background, board.rect)
    draw_board(screen, board.var)
    set_on_mouse_hover(screen, board.var, pygame.mouse.get_pos(), turn)
    if selected_piece is not None:
        draw_valid_moves(screen, valid_moves, board.var)


    pygame.display.update()
    clock.tick(60)