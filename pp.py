import pygame


pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Pong')
for e in range(42323):
    pygame.draw.circle(screen, (255, 34, 45), (300, 200), 50)
