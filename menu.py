import pygame
import button

pygame.init()


class Menu:
    def __init__(self):
        self.Button1 = button.Button()
        self.Button2 = button.Button()
        self.Button3 = button.Button()

    def display(self):
        pygame.display.set_caption("Game")

    def update_display(self, screen):
        self.Button1.create_button(screen, (107, 142, 35), 700, 300, 200, 70, 0, "New game", (255, 255, 255))
        self.Button2.create_button(screen, (107, 142, 35), 700, 452, 200, 70, 0, "Settings", (255, 255, 255))
        self.Button3.create_button(screen, (107, 142, 35), 700, 600, 200, 70, 0, "Exit", (255, 255, 255))
        font = pygame.font.Font(None, 75)
        text_surface = font.render("The path of water lilies", False, (255, 255, 255))
        screen.blit(text_surface, (520, 130))
        pygame.display.flip()


class Settings(Menu):
    def __init__(self):
        super().__init__()

    def update_display(self, screen):
        self.Button1.create_button(screen, (107, 142, 35), 700, 300, 200, 70, 0, "Sound", (255, 255, 255))
        self.Button2.create_button(screen, (107, 142, 35), 700, 453, 200, 70, 0, "FAQ", (255, 255, 255))
        self.Button3.create_button(screen, (107, 142, 35), 700, 600, 200, 70, 0, "Back", (255, 255, 255))
        font = pygame.font.Font(None, 120)
        text_surface = font.render("Settings", False, (255, 255, 255))
        screen.blit(text_surface, (620, 120))
        pygame.display.flip()

class FAQ(Menu):
    def __init__(self):
        super().__init__()

    def update_display(self, screen):
        self.Button1.create_button(screen, (107, 142, 35), 690, 600, 200, 70, 0, "Back", (255, 255, 255))
        font1 = pygame.font.Font(None, 120)
        text_surface = font1.render("FAQ", False, (255, 255, 255))
        screen.blit(text_surface, (700, 120))

        font2 = pygame.font.Font(None, 30)
        text_surface = font2.render("Используйте WASD и стрелочки для управления", False, (255, 255, 255))
        text_surface2 = font2.render("Ваша задача - переправится через реку",False, (255, 255, 255))
        text_surface3 = font2.render("Остерегайтесь комаров", False, (255, 255, 255))
        screen.blit(text_surface, (550, 400))
        screen.blit(text_surface2, (550, 450))
        screen.blit(text_surface3, (550, 500))
        pygame.display.flip()

class Result_Bad(Menu):
    def __init__(self):
        super().__init__()

    def update_display(self, screen):
        self.Button1.create_button(screen, (107, 142, 35), 700, 453, 200, 70, 0, "Play again", (255, 255, 255))
        self.Button2.create_button(screen, (107, 142, 35), 700, 600, 200, 70, 0, "Return to menu", (255, 255, 255))
        font = pygame.font.Font(None, 120)
        text_surface = font.render(f"Score: 0", False, (255, 255, 255))
        screen.blit(text_surface, (700, 300))
        font = pygame.font.Font(None, 120)
        text_surface = font.render("Defeat", False, (255, 255, 255))
        screen.blit(text_surface, (620, 120))
        pygame.display.flip()

class Result_Good(Menu):
    def __init__(self, score):
        super().__init__()
        self.score = score

    def update_display(self, screen):
        self.Button1.create_button(screen, (107, 142, 35), 700, 453, 200, 70, 0, "Play again", (255, 255, 255))
        self.Button2.create_button(screen, (107, 142, 35), 700, 600, 200, 70, 0, "Return to menu", (255, 255, 255))
        font = pygame.font.Font(None, 120)
        text_surface = font.render(f"Score: {self.score}", False, (255, 255, 255))
        screen.blit(text_surface, (700, 300))
        font = pygame.font.Font(None, 120)
        text_surface = font.render("You win", False, (255, 255, 255))
        screen.blit(text_surface, (620, 120))
        pygame.display.flip()