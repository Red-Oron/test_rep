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
        screen.fill((30, 144, 255))
        self.Button1.create_button(screen, (107, 142, 35), 700, 300, 200, 100, 0, "New game", (255, 255, 255))
        self.Button2.create_button(screen, (107, 142, 35), 700, 500, 200, 100, 0, "Settings", (255, 255, 255))
        self.Button3.create_button(screen, (107, 142, 35), 700, 700, 200, 100, 0, "Exit", (255, 255, 255))
        pygame.display.flip()



