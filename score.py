import pygame
class Score():
    def __init__(self,score):
        self.score = score
        self.star = pygame.image.load('objects/star.png')
        self.star = pygame.transform.scale(self.star,(100,100))

    def draw(self,screen):
        screen.blit(self.star, (110+10, 12))
        font = pygame.font.Font(None, 65)
        text_surface = font.render(str(self.score), False, (0, 0, 0))
        screen.blit(text_surface, (110+49, 41))