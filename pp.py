import pygame
import sys
from pygame.locals import *


pygame.init()
running = True
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Pong')
x = 200
y = 200
vel = 10
#Game loop begins
while True:
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 500 - width:
        x += vel

    if keys[pygame.K_UP] and y > 0:
        y -= vel

    if keys[pygame.K_DOWN] and y < 500 - height:
        y += vel
    pygame.draw.circle(screen, (255, 144, 0), (x, y), 50)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()