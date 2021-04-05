import numpy as np
import pygame
import random


BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)

ROW_COUNT = 6
COLUMN_COUNT = 7


WIDTH = 600
HEIGHT = 900
size = (WIDTH, HEIGHT)
FPS = 60

class Jeton(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        if color == RED:
            self.image = pygame.image.load("Images/JetonRot.png")
        if color == BLUE:
            self.image = pygame.image.load("Images/JetonBlau.png")
        if color == YELLOW:
            self.image = pygame.image.load("Images/JetonGelb.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def gravity(self):
        self.rect.y += 3.2
    
class Board(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Brett.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)




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
           
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FourInARow")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()


jeton = Jeton(RED,50, 150)
all_sprites.add(jeton)

board = Board(WIDTH/2, HEIGHT/2)
all_sprites.add(board)



running = True
while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                jeton.rect.y -= 100
            if event.key == pygame.K_DOWN:
                jeton.rect.y += 100
            if event.key == pygame.K_LEFT:
                jeton.rect.x -= 100
            if event.key == pygame.K_RIGHT:
                jeton.rect.x += 100


    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
