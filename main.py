import sys

import pygame
from menu import Menu, Settings
from player import Player
from board import Board


if __name__ == '__main__':
    menu = Menu()
    menu.display()
    menu_mod = 1
    fin = False
    sett = False
    board, player = None, None
    screen = pygame.display.set_mode((1600, 900))
    while True:
        if menu_mod == 1:
            menu.update_display(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if menu.Button1.pressed(pygame.mouse.get_pos()):
                        menu_mod = 0
                    if menu.Button2.pressed(pygame.mouse.get_pos()):
                        menu_mod = 2
                    if menu.Button3.pressed(pygame.mouse.get_pos()):
                        pygame.quit()
                        sys.exit()
        elif menu_mod == 2:
            if not sett:
                sett = True
                settings = Settings()

        else:
            if not fin:
                board = Board()
                player = Player()
                fin = True
            board.draw(screen)
            #player.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                player.move(event)
                player.death()
            pygame.display.flip()


