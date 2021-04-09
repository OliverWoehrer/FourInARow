import numpy as np
import pygame
import math
import time
import sys

from pygame.constants import WINDOWHITTEST
from pygame.font import Font


# import socket

# HOST = '10.232.11.194'  # The server's hostname or IP address
# PORT = 65432        # The port used by the server

# def main() :
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.connect((HOST, PORT))
#         print ('Test')
#         s.sendall(b'Hello, world')
#         data = s.recv(3)
#         print('Received', repr(data))
#         exit()


# if __name__ == "__main__":
#     main()#

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
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
FONT = pygame.font.Font(None, 32)
TITLEFONT = pygame.font.Font(None, 100)
error = False

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
            
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if  self.txt_surface.get_width() < self.w-10:
                        self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.color = COLOR_ACTIVE
            else:
                self.color = COLOR_INACTIVE 

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

class button():
    def __init__(self, x,y,width,height, text=''):
        self.color =COLOR_INACTIVE
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.rect = pygame.Rect(x, y, width, height)
        self.active = False

    def draw(self,win):
        self.txt_surface = FONT.render(self.text, True, self.color)
        screen.blit(self.txt_surface, (self.rect.x+self.width/2-self.txt_surface.get_width()/2, self.rect.y+self.height/2-self.txt_surface.get_height()/2))
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),2)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.color = YELLOW
                return True
            else:
                self.color = COLOR_INACTIVE
        if event.type == pygame.MOUSEBUTTONUP:
            self.color = COLOR_INACTIVE
        if event.type == pygame.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.color = COLOR_ACTIVE
            else:
                self.color = COLOR_INACTIVE 
        return False   
    


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
   

def game():
    
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
                if event.key == pygame.K_ESCAPE:
                    Menu()
                    pygame.quit()
                    sys.exit()
        all_sprites.update()
        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()


def Menu():

    input_button1 = button((2*WIDTH)/6,450 ,WIDTH/3,35, 'Play')
    input_button2 = button((2*WIDTH)/6,500 ,WIDTH/3,35, 'Quit')
    input_buttons = [input_button1, input_button2]
    input_box1 = InputBox((2*WIDTH)/6, 300, WIDTH/3, 35)
    input_box2 = InputBox((2*WIDTH)/6, 400, WIDTH/3, 35)
    input_boxes = [input_box1, input_box2]
    title = TITLEFONT.render("FourInARow", False, COLOR_INACTIVE)
    comment1 = FONT.render("Name:", False, COLOR_INACTIVE)
    comment2 = FONT.render("GameID:", False, COLOR_INACTIVE)
    errormsg = FONT.render("Error", False, RED)
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)
            
            if input_button1.handle_event(event):
                print("Sending Data")
                print("Waiting for server repsoned")
                game()
                pygame.quit()
                sys.exit()
            if input_button2.handle_event(event):
                pygame.quit()
                sys.exit()        

        screen.fill(BLACK)
        screen.blit(title, ((WIDTH/2)-(title.get_width()/2), 100))
        screen.blit(comment1,((2*WIDTH)/6,275))
        screen.blit(comment2,((2*WIDTH)/6,375))
        if error == True:
            screen.blit(errormsg,((WIDTH/2)-(errormsg.get_width()/2),600))

        for box in input_boxes:
            box.draw(screen)
        for but in input_buttons:
            but.draw(screen)

        pygame.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    Menu()
    pygame.quit()