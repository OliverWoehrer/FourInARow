import numpy as np
import pygame
import sys

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)

SIZE = 800
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = SIZE / COLUMN_COUNT
RADIUS = int(SQUARESIZE/2-5)

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def insert_piece(board,row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
	return board[ROW_COUNT-1][col] == 0

def get_next_open(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))


def draw_board(board):
    pygame.draw.rect(screen,BLUE, (0,SQUARESIZE, SIZE,SIZE-SQUARESIZE))
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2),int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),RADIUS)

    pygame.display.update()


board = create_board()
print_board(board)
turn = 0
game_over = False

pygame.init()

screen = pygame.display.set_mode((SIZE,SIZE))
draw_board(board)
pygame.display.update()

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen,BLACK,(0,0,SIZE,SQUARESIZE))
            posx = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen,RED,(posx,int(SQUARESIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen,YELLOW,(posx,int(SQUARESIZE/2)), RADIUS)

        pygame.display.update()


