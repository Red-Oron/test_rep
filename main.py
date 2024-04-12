import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()
pygame.quit()
