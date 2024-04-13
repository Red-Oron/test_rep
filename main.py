import sys

import pygame
from menu import Menu, Settings, FAQ, Result_Bad, Result_Good
from player import Player
from board import Board
from health import Health
from score import Score


def draw_background(screen, image):
    background = pygame.transform.scale(pygame.image.load(image), (1600, 900))
    screen.blit(background, background.get_rect(bottomright=(1600, 900)))


if __name__ == '__main__':
    menu = Menu()
    menu.display()
    score = 0
    menu_mod = 1
    fin = False
    sett = False
    fa = False
    end_bad = False
    end_good = False
    status_music = True
    board, player, settings, health, faq, bad, good = None, None, None, None, None, None, None
    screen = pygame.display.set_mode((1600, 900))
    while True:
        if menu_mod == 1:
            score = 0
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
            settings.update_display(screen, status_music)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if menu.Button1.pressed(pygame.mouse.get_pos()):
                        status_music = not status_music

                    if menu.Button2.pressed(pygame.mouse.get_pos()):
                        menu_mod = 3
                    if menu.Button3.pressed(pygame.mouse.get_pos()):
                        menu_mod = 1
                        sett = False

            pygame.display.flip()
        elif menu_mod == 3:
            if not fa:
                fa = True
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
                        fa = False
        elif menu_mod == 4:
            if not end_bad:
                end_bad = True
                bad = Result_Bad()
            draw_background(screen, 'backgrounds/menu.png')
            bad.update_display(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if bad.Button1.pressed(pygame.mouse.get_pos()):
                        menu_mod = 0
                        end_bad = False
                    elif bad.Button2.pressed(pygame.mouse.get_pos()):
                        menu_mod = 1
                        end_bad = False
        elif menu_mod == 5:
            if not end_good:
                end_good = True
                good = Result_Good(score)
            draw_background(screen, 'backgrounds/menu.png')
            good.update_display(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if good.Button1.pressed(pygame.mouse.get_pos()):
                        menu_mod = 0
                        end_good = False
                    elif good.Button2.pressed(pygame.mouse.get_pos()):
                        menu_mod = 1
                        end_good = False

        else:
            if not fin:
                board = Board()
                player = Player()
                health = Health(player.health)
                score_f = Score(score)
                fin = True
            draw_background(screen, 'backgrounds/river.jpg')
            board.draw(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                player.move(event, board.board)
                health.change(player.health)
                if player.cordX >= 13:
                    fin = False
                    score += 1
                    menu_mod = 5
                if player.death():
                    fin = False
                    score = 0
                    menu_mod = 4
            player.draw(screen)
            health.draw(screen)
            score_f.draw(screen)
            pygame.display.flip()