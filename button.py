import pygame


class Button:
    def __init__(self, x, y, wight, height, text, image=None, hover_image=None, sound=None):
        self.colors = {'WHITE': (255, 255, 255)}
        self.x, self.y, self.wight, self.height, self.text = x, y, wight, height, text
        self.image = pygame.image.load(image) if image is not None else None
        if self.image is not None:
            self.image = pygame.transform.scale(self.image, (wight, height))
            self.rect = self.image.get_rect(topleft=(x, y))
        font = pygame.font.Font(None, 36)
        self.text_surface = font.render(self.text, True, self.colors['WHITE'])
        self.text_rect = self.text_surface.get_rect(center=(self.wight // 2 + self.x, self.height // 2 + self.y))
        self.hover_image = pygame.image.load(hover_image) if hover_image is not None else None
        if self.image is not None:
            self.hover_image = pygame.transform.scale(self.hover_image, (wight, height))
        self.sound = sound if sound is not None else None
        self.is_hovered = False

    def draw(self, surface):
        current_image = self.hover_image if self.is_hovered and self.hover_image is not None else self.image
        if current_image is not None:
            surface.blit(current_image, self.rect)
            font = pygame.font.Font(None, 36)
            self.text_surface = font.render(self.text, True, self.colors['WHITE'])
            self.text_rect = self.text_surface.get_rect(center=self.rect.center)
        surface.blit(self.text_surface, self.text_rect)

    def check_hover(self, cursor_position):
        self.is_hovered = self.text_rect.collidepoint(cursor_position) if self.image is None else self.rect.collidepoint(cursor_position)
