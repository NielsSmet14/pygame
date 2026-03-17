import pygame
import sys
from pygame.locals import *

#variabelen
x = 200
y = 200
vel = 1
radius = 5
reswidth=1280
resheight=720

#start game
pygame.init()
running = True

screen = pygame.display.set_mode((reswidth, resheight))
pygame.display.set_caption('Pong')

#Game loop begins
while True:
    #om bal te kunnen bewegen
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
        x -= vel
        pygame.draw.circle(screen, (255, 144, 0), (x, y), radius)

    if keys[pygame.K_RIGHT] and x < 1280 - radius:
        pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
        x += vel
        pygame.draw.circle(screen, (255, 144, 0), (x, y), radius)

    if keys[pygame.K_UP] and y > 0:
        pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
        y -= vel
        pygame.draw.circle(screen, (255, 144, 0), (x, y), radius)

    if keys[pygame.K_DOWN] and y < 720 - radius:
        pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
        y += vel
        pygame.draw.circle(screen, (255, 144, 0), (x, y), radius)
    if keys[pygame.K_SPACE]:
        pygame.draw.rect(screen, (0, 0, 0), (0, 0,reswidth,resheight))
        pygame.draw.circle(screen, (255, 144, 0), (x, y), radius)
    #exitgamedinges
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #zodat game werkt
    pygame.display.update()