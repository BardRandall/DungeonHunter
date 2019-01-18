import pygame


class StandartHandler:

    def __init__(self, board):
        self.board = board
        self.max_k = 16

    def handle(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                if self.board.zoom < self.max_k:
                    self.board.make_zoom(1, event.pos)
            elif event.button == 5:
                if self.board.zoom > 0:
                    self.board.make_zoom(-1, event.pos)
