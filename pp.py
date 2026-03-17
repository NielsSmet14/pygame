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
vel = 1
width = 20
height = 20

#Game loop begins
while True:
    #om bal te kunnen bewegen
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 50)
        x -= vel
        pygame.draw.circle(screen, (255, 144, 0), (x, y), 50)

    if keys[pygame.K_RIGHT] and x < 1280 - width:
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 50)
        x += vel
        pygame.draw.circle(screen, (255, 144, 0), (x, y), 50)

    if keys[pygame.K_UP] and y > 0:
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 50)
        y -= vel
        pygame.draw.circle(screen, (255, 144, 0), (x, y), 50)

    if keys[pygame.K_DOWN] and y < 720 - height:
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 50)
        y += vel
        pygame.draw.circle(screen, (255, 144, 0), (x, y), 50)

    #exitgamedinges
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #zodat game werkt
    pygame.display.update()