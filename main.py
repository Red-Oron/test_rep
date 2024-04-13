import pygame
from menu import Menu
from player import Player
from board import Board


if __name__ == '__main__':
    menu = Menu()
    menu.display()
    menu_mod = True
    fin = False
    board, player = None, None
    screen = pygame.display.set_mode((1600, 900))
    while True:
        if menu_mod:
            menu.update_display(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if menu.Button1.pressed(pygame.mouse.get_pos()):
                        menu_mod = False
                    if menu.Button2.pressed(pygame.mouse.get_pos()):
                        pass
                    if menu.Button3.pressed(pygame.mouse.get_pos()):
                        pass
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


