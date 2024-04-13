import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('objects/mosquito.png'), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1600)
        self.rect.y = 900
        self.vel = random.randint(1, 3)

    def update(self):
        self.rect.y -= self.vel
