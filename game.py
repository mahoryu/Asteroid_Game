# /game.py

import pygame, sys
from pygame.locals import *
from pygame import draw
from flyingObject import FlyingObject

# initialize the program
pygame.init()

# set a FPS value
FPS = 30
FramePerSec = pygame.time.Clock()

# Set up color constants
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# set object images
char = pygame.image.load("/home/tech_chef/Projects/Asteroid_Game/Images/ship.png")
bg = pygame.image.load("/home/tech_chef/Projects/Asteroid_Game/Images/stars_bg.jpg")

# Set a display size constant
HIGHT = 800
WIDTH = 800

# setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((WIDTH,HIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Testing the Evironment")


def redrawGameWindow():
    DISPLAYSURF.blit(bg, (0,0))
    ship.draw(DISPLAYSURF, char)

    pygame.display.update()

# Game loop
ship = FlyingObject()
while True:
    pygame.display.update()
    for envent in pygame.event.get():
        if envent.type == QUIT:
            pygame.quit()
            sys.exit()

    ship.advance()

    redrawGameWindow()

    FramePerSec.tick(FPS)
