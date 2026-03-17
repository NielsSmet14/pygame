import pygame
import sys
from pygame.locals import *


pygame.init()
running = True
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Pong')

#Game loop begins
while True:
    pygame.draw.circle(screen, (255, 144, 45), (300, 200), 50)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()