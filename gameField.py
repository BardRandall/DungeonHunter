import pygame  # for displaying grid
import json
from Managers import BlockManager


class Board:
    def __init__(self, level, screen):

        self.zoom = 0
        self.zoom_centre = None

        self.start_x = 0
        self.start_y = 0

        self.screen_width = 800
        self.screen_height = 600
        self.screen = screen

        with open('levels/level{}.json'.format(level)) as f:
            level_data = json.load(f)
        self.width = level_data['width']
        self.height = level_data['height']

        self.field = []
        self.load_level(level_data['board'])

        self.bm = BlockManager()

        self.left = (self.screen_width - self.width * 16) // 2
        self.top = (self.screen_height - self.height * 16) // 2
        self.cell_size = 16

    def load_level(self, lvl):
        for i in range(self.width):
            res = []
            for j in range(self.height):
                res.append(lvl[i][j]['block'])
            self.field.append(res)

    def make_zoom(self, k, pos):
        self.zoom += k
        self.cell_size += k
        if self.zoom == 0:
            self.zoom_centre = None
            self.start_x = 0
            self.start_y = 0
            self.left = (self.screen_width - self.width * 16) // 2
            self.top = (self.screen_height - self.height * 16) // 2
            return
        if self.zoom_centre is None and self.zoom != 0:
            self.zoom_centre = pos
        self.start_x += (self.zoom_centre[0] - 400) * k
        self.start_y += (self.zoom_centre[1] - 300) * k
        self.left = (self.screen_width - self.width * 16) // 2
        self.top = (self.screen_height - self.height * 16) // 2

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                texture = self.bm.get_texture(self.field[x][y])
                texture = pygame.transform.scale(texture, (16 + self.zoom, 16 + self.zoom))
                self.screen.blit(texture,
                                 (x * self.cell_size + self.left - self.start_x,
                                  y * self.cell_size + self.top - self.start_y))
                '''pygame.draw.rect(self.screen, pygame.Color('white'),
                                 (
                                     x * self.cell_size + self.left,
                                     y * self.cell_size + self.top,
                                     self.cell_size,
                                     self.cell_size
                                 ), 1
                                 )'''

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x >= self.width or cell_y < 0 or cell_y >= self.height:
            return None
        return cell_x, cell_y

    def on_click(self, cell):
        self.field[cell[1]][cell[0]] = (1 + self.field[cell[1]][cell[0]]) % 3

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell is not None:
            self.on_click(cell)
