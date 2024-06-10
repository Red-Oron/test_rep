import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, speed):
        super(Enemy, self).__init__()
        self.image = pygame.transform.scale(pygame.image.load('data\\Image\\objects\\mosquito.png'), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 900
        self.speed = speed

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

    def draw(self, surface):
        surface.blit(self.image, self.rect)
