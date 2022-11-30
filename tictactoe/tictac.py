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

# Game variables
active_player = 0 

running = True

def place_piece(pos):
    x = 0 # x-axis
    y = 1 # y-axis
    
    # I should find a cleaner way to do this
    if pos[y] in range(100, 0, -1):
        if pos[x] in range(100, 0, -1):
            board[0] = active_player

        if pos[x] in range(200, 100, -1):
            board[1] = active_player

        if pos[x] in range(300, 200, -1):
            board[2] = active_player

    if pos[y] in range(200, 100, -1):
        if pos[x] in range(100, 0, -1):
            board[3] = active_player

        if pos[x] in range(200, 100, -1):
            board[4] = active_player

        if pos[x] in range(300, 200, -1):
            board[5] = active_player

    if pos[y] in range(300, 200, -1):
        if pos[x] in range(100, 0, -1):
            board[6] = active_player

        if pos[x] in range(200, 100, -1):
            board[7] = active_player

        if pos[x] in range(300, 200, -1):
            board[8] = active_player
    print(board) 

def check_winner():
    pass

# Main loop
while running: 
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            print(pos)
            place_piece(pos)            

        if event.type == pygame.KEYDOWN:
            if event.key in [K_ESCAPE, K_q]:
                running = False

    draw_grid()

    pygame.display.flip()

