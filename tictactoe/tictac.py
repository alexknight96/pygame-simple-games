# Imports
import pygame

# Resolution & Display
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300
SCREEN = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

pygame.display.set_caption('Tic-Tac-Toe')

# Grid Settings
BLOCK_SIZE = 100

# RGB Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Game variables
active_player = 0 

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


def place_piece(pos):
    global active_player

    def place_x(position, a, b, c):
        if position in range(100, 0, -1):
            board[a] = active_player

        if position in range(200, 100, -1):
            board[b] = active_player

        if position in range(300, 200, -1):
            board[c] = active_player
    
    # For readability 
    x = 0 # x-axis
    y = 1 # y-axis

    # Finds out which square is clicked and places the active_player in the appropriate list element. 
    if pos[y] in range(100, 0, -1):
        place_x(pos[x], 0, 1, 2) 

    if pos[y] in range(200, 100, -1):
        place_x(pos[x], 3, 4, 5)

    if pos[y] in range(300, 200, -1):
        place_x(pos[x], 6, 7, 8)
    
    print(board)

    # Cycles between the X/O pieces each time a piece is placed
    if active_player == 0:
        active_player = 1

    else:
        active_player = 0

# Board set-up 
board = []

# Fill the board list with 9 (for each square on the grid) empty elements
for i in range(9):
    board.append('')

running = True

def game_display():
    draw_grid()
    pygame.display.flip()

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

    game_display()
