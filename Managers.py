import json
from PIL import Image
import pygame.image as pim


class BlockManager:

    def __init__(self):
        with open('assets/blocks.json') as f:
            self.blocks = json.load(f)
        self.textures = {}
        for name in self.blocks.keys():
            block_texture = self.blocks[name]['texture']
            texture_x, texture_y, cid = block_texture['x'], block_texture['y'], block_texture['catalog_id']
            image = Image.open('imgs/blocks/tiles{}.png'.format(cid))
            x, y = texture_x * 16, texture_y * 16
            image = image.crop((x, y, x + 16, y + 16))
            self.textures[name] = pim.fromstring(image.tobytes('raw', 'RGBA'), (16, 16), 'RGBA')

    def get_texture(self, name):
        return self.textures[name]
