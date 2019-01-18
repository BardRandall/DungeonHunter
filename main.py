from gameField import *
from Handlers import StandartHandler

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

with open('levels/level1.json') as f:
    print(f.read())

clock = pygame.time.Clock()

board = Board(1, screen)
handler = StandartHandler(board)

while pygame.event.wait().type != pygame.QUIT:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        handler.handle(event)
    board.render()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
