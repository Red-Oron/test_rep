import pygame
import button

pygame.init()


class Menu:
    def __init__(self):
        self.main()

    def display(self):
        self.screen = pygame.display.set_mode((800, 900))
        pygame.display.set_caption("Game")

    def update_display(self):
        self.screen.fill((30, 144, 255))
        self.Button1.create_button(self.screen, (107, 142, 35), 300, 300, 200, 100, 0, "New game", (255, 255, 255))
        self.Button2.create_button(self.screen, (107, 142, 35), 300, 500, 200, 100, 0, "Settings", (255, 255, 255))
        self.Button3.create_button(self.screen, (107, 142, 35), 300, 700, 200, 100, 0, "Exit", (255, 255, 255))
        pygame.display.flip()

    def main(self):
        self.Button1 = button.Button()
        self.Button2 = button.Button()
        self.Button3 = button.Button()
        self.display()
        while True:
            self.update_display()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.Button1.pressed(pygame.mouse.get_pos()):
                        pass
                    if self.Button2.pressed(pygame.mouse.get_pos()):
                        pass
                    if self.Button3.pressed(pygame.mouse.get_pos()):
                        pass


if __name__ == '__main__':
    obj = Menu()
