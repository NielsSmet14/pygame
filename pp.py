import pygame
import sys
from pygame.locals import *

#start game
pygame.init()
running = True
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Pong')

#variabelen
x = 200
y = 200
vel = 10
width = 20
height = 20

#Game loop begins
while True:
    #om bal te kunnen bewegen
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 1280 - width:
        x += vel

    if keys[pygame.K_UP] and y > 0:
        y -= vel

    if keys[pygame.K_DOWN] and y < 720 - height:
        y += vel
    pygame.draw.circle(screen, (255, 144, 0), (x, y, width, height), 50)
    #exitgamedinges
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #zodat game werkt
    pygame.display.update()