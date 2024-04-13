import pygame
class Score():
    def __init__(self,score):
        self.score = score

    def draw(self,screen):
        font = pygame.font.Font(None, 75)
        text_surface = font.render(str(self.score), False, (255, 255, 255))
        screen.blit(text_surface, (110+46, 42))