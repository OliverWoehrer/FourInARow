import numpy as np
import pygame
import math
import time


BLUE = (0,0,255)
BLACK = (30,30,30)
RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)

ROW_COUNT = 6
COLUMN_COUNT = 7


WIDTH = 700
HEIGHT = 800
size = (WIDTH, HEIGHT)
FPS = 60

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FourInARow")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 32)

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
        self.posx=x
        self.posy=y
    
    def gravity(self):
        self.rect.y += 3.2
    
    def inRange(self, x):
        if x < WIDTH and x >= 0:
            return True
        else:
            return False
    
class Board(pygame.sprite.Sprite):
    array = np.zeros((ROW_COUNT,COLUMN_COUNT))
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Images/Brett.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def insert_piece(self,row, col, piece):
        self.array[row][col] = piece

    def is_valid_location(self, col):
	    return self.array[ROW_COUNT-1][col] == 0

    def get_next_open(self, col):
        for r in range(ROW_COUNT):
            if self.array[r][col] == 0:
                return r
        

    def print_array(self):
        print(np.flip(self.array, 0))


           
def main():
    
    all_sprites = pygame.sprite.Group()


    jeton = Jeton(RED,WIDTH-50, 50)
    all_sprites.add(jeton)

    board = Board(WIDTH/2, HEIGHT/2)
    all_sprites.add(board)

    board.print_array()
    running = True
    turn = 0
    while running:

        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if jeton.inRange(jeton.rect.x-100):
                        jeton.rect.x -= 100
                if event.key == pygame.K_RIGHT:
                    if jeton.inRange(jeton.rect.x+100):
                        jeton.rect.x += 100
                if event.key == pygame.K_RETURN:
                    if turn == 0:
                        col = int(math.floor(jeton.rect.x/100))
                        if board.is_valid_location(col):
                            row = board.get_next_open(col)
                            board.insert_piece(row , col, 1)
                            print("Sending Player 1 [row,col]: [" + str(row) + "," + str(col) + "]")
                    else:
                        col = int(math.floor(jeton.rect.x/100))
                        if board.is_valid_location(col):
                            row = board.get_next_open(col)
                            board.insert_piece(row , col, 2)
                            print("Sending Player 2 [row,col]: [" + str(row) + "," + str(col) + "]")
                            
                    turn += 1
                    turn = turn % 2
                        
        all_sprites.update()
        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()


def Menu():

    
    
    input_box = pygame.Rect(260, 320, 180, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill(BLACK)
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main()
    ##Menu()
    pygame.quit()