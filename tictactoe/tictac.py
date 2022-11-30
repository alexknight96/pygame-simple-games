# Imports
import pygame

# Resolution & Display
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300
SCREEN = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

# Grid Settings
BLOCK_SIZE = 100

# RGB Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Import pygame.locals for easier access to key coordinates
from pygame.locals import (
        K_q,
        K_ESCAPE,
        QUIT,
)

# Functions
def draw_grid():
    for x in range(0, WINDOW_WIDTH, BLOCK_SIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

# Board stuff
board = []

for i in range(9):
    board.append('')

print(board)

running = True

# Main loop
while running: 
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key in [K_ESCAPE, K_q]:
                running = False

    draw_grid()

    pygame.display.flip()

