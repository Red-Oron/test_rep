import pygame


def draw(sp, screen):
    for i in range(len(sp)):
        for j in range(len(sp[i])):
            if sp[i][j] == 0:
                pygame.draw.rect(screen,(0,0,255),(20*j,20*i,20,20))
            if sp[i][j] == 1:
                pygame.draw.rect(screen,(255,0,0),(20*j,20*i,20,20))
