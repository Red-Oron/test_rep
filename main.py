import sys

import pygame
from menu import Menu, Settings, FAQ
from player import Player
from board import Board


def draw_background(screen, image):
    background = pygame.transform.scale(pygame.image.load(image), (1600, 900))
    screen.blit(background, background.get_rect(bottomright=(1600, 900)))


if __name__ == '__main__':
    menu = Menu()
    menu.display()
    menu_mod = 1
    fin = False
    sett = False
    board, player, settings = None, None, None
    screen = pygame.display.set_mode((1600, 900))
    while True:
        if menu_mod == 1:
            draw_background(screen, 'backgrounds/menu.png')
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
            pygame.display.flip()

        elif menu_mod == 2:
            if not sett:
                sett = True
                settings = Settings()
            draw_background(screen, 'backgrounds/menu.png')
            settings.update_display(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if menu.Button1.pressed(pygame.mouse.get_pos()):
                        pass
                    if menu.Button2.pressed(pygame.mouse.get_pos()):
                        menu_mod = 3
                    if menu.Button3.pressed(pygame.mouse.get_pos()):
                        menu_mod = 1
                        sett = False

            pygame.display.flip()
        elif menu_mod == 3:
            faq = FAQ()
            draw_background(screen, 'backgrounds/FAQ.png')
            faq.update_display(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if faq.Button1.pressed(pygame.mouse.get_pos()):
                        menu_mod = 2
        elif menu_mod == 4:
            pass
        else:
            if not fin:
                board = Board()
                player = Player()
                fin = True
            draw_background(screen, 'backgrounds/river.jpg')
            board.draw(screen)
            player.draw(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                player.move(event, board.board)
                if player.death():
                    fin = False
                    menu_mod = 4
            pygame.display.flip()