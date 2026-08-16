import pygame
from sys import exit
from Game.board import board
from Game.move import crd_to_rowcol
from Game.rules import is_check,is_checkmate,is_stalemate
from Pieces.Piece import find_king
from UI.board_renderer import draw_board, draw_valid_moves

pygame.init()
screen = pygame.display.set_mode(board.size)
pygame.display.set_caption('Chess')
clock = pygame.time.Clock()

# start turn
turn = 'W'

# click-state
selected_pos = None      # rowcol of the currently selected piece, or None
selected_piece = None    # the piece obj currently selected, or None
valid_moves = []         # cached valid moves for the selected piece

# main loop
while True:
    # single event pass — every click is handled right here, in order
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            click_crd = event.pos  # use the event's own pos, not a fresh mouse.get_pos()
            click_pos = crd_to_rowcol(click_crd)

            if selected_piece is None:
                # first click of a turn: try to select a piece
                piece = board.var[click_pos[0]][click_pos[1]]
                if piece is not None and piece.color == turn:
                    selected_pos = click_pos
                    selected_piece = piece
                    valid_moves = selected_piece.get_valid_moves(board, selected_pos)
            else:
                # second click: attempt the move
                if click_pos in valid_moves:
                    if selected_piece.type == 'K' and click_pos[1] - selected_pos[1] in [2, -2]:
                        board.variable_update(selected_pos, click_pos, True)  # castling
                    else:
                        board.variable_update(selected_pos, click_pos)
                    turn = 'B' if turn == 'W' else 'W'
                    # check, checkmate & stalemate state (informing state)
                    king_pos = find_king(board, turn)
                    if is_check(board, king_pos):
                        print(f'{turn} king is in check')
                    if is_checkmate(board, king_pos):
                        print(f'{turn} has been checkmated')
                    elif is_stalemate(board, king_pos):
                        print(f'its stalemate')

                    selected_pos = None
                    selected_piece = None
                    valid_moves = []
                else:
                    # clicked somewhere that isn't a valid destination:
                    # either re-select another one of your own pieces, or deselect
                    piece = board.var[click_pos[0]][click_pos[1]]
                    if piece is not None and piece.color == turn:
                        selected_pos = click_pos
                        selected_piece = piece
                        valid_moves = selected_piece.get_valid_moves(board, selected_pos)
                    else:
                        selected_pos = None
                        selected_piece = None
                        valid_moves = []

    # drawing funcs
    screen.blit(board.background, board.rect)
    draw_board(screen, board.var)
    if selected_piece is not None:
        draw_valid_moves(screen, valid_moves, board.var)

    pygame.display.update()
    clock.tick(60)