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

def mouse_pos():
    # Takes the mouse position and, if over a tile, returns the tile index relative to the board list
    pos = pygame.mouse.get_pos()
    print(pos)
    x = pos[0] // BLOCK_SIZE
    y = pos[1] // BLOCK_SIZE

    return x, y

def check_winstate(player):
    # Check the board horizontally for a winstate. 
    for row in board:
        if all(cell == player for cell in row):
            print('win')
            return True

def modify_board():
    global active_player
    
    x, y = mouse_pos()

    if board[y][x] == '':
        board[y][x] = active_player

    # If a piece is already placed it is removed
    else:
        board[y][x] = ''

    check_winstate(active_player)
    
    # Cycles through the X and O piece each turn
    if active_player == 0:
        active_player = 1

    else:
        active_player = 0


    print(board)

# Board set-up 
board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]

running = True

def game_display():
    draw_grid()
    pygame.display.flip()

# Main loop
while running: 
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            modify_board() 

        if event.type == pygame.KEYDOWN:
            if event.key in [K_ESCAPE, K_q]:
                running = False

    game_display()
