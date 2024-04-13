import pygame

class Health:
    def __init__(self, health):
        self.hp_sprite = pygame.image.load('objects/heart.png')
        self.hp_sprite = pygame.transform.scale(self.hp_sprite, (100, 100))
        self.health = health

    def change(self, health):
        self.health = health

    def draw(self, screen):
        screen.blit(self.hp_sprite, (10, 10))
        font = pygame.font.Font(None, 75)
        text_surface = font.render(str(self.health), False, (255, 255, 255))
        screen.blit(text_surface, (46, 42))
