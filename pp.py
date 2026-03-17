import pygame


pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Pong')

pygame.draw.circle(screen, (255, 0, 0), (300, 200), 50)