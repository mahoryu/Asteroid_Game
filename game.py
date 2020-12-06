# /game.py

import pygame, sys
from pygame.locals import *
from pygame import draw

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

# setup a 300x300 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((300,300))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Testing the Evironment")

# Create Lines and Shapes
draw.line(DISPLAYSURF, BLUE, (150,130), (130,170))
draw.line(DISPLAYSURF, BLUE, (150,130), (170,170))
draw.line(DISPLAYSURF, GREEN, (130,170), (170,170))
draw.circle(DISPLAYSURF, BLACK, (100,50), 30)
draw.circle(DISPLAYSURF, BLACK, (200,50), 30)
draw.rect(DISPLAYSURF, RED, (100, 200, 100, 50), 2)
draw.rect(DISPLAYSURF, BLACK, (110, 260, 80, 5))

# Game loop
while True:
    pygame.display.update()
    for envent in pygame.event.get():
        if envent.type == QUIT:
            pygame.quit()
            sys.exit()

    FramePerSec.tick(FPS)
