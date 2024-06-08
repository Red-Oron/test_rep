import pygame
import json


class Menu:
    def __init__(self, sprites, image):
        self.sprites, self.image = sprites, image

    def draw(self, screen, surface, size):
        from functions import draw_background, Button
        draw_background(surface, self.image)
        for sprite in self.sprites:
            if type(sprite) == Button:
                sprite.draw(surface)
            elif type(sprite) == tuple:
                surface.blit(sprite[0], sprite[1])
        scaled_surface = pygame.transform.scale(surface, size)
        screen.blit(scaled_surface, (0, 0))
        pygame.display.flip()

    def check_hovers(self, cursor):
        from functions import Button
        for sprite in self.sprites:
            if type(sprite) == Button:
                sprite.check_hover(cursor)


def main_menu(screen, clock):
    from functions import Button, quit_any, FPS, update_json, get_json
    from player import game
    font = pygame.font.Font(None, 75)
    text_surface = font.render("The path of water lilies", False, (255, 255, 255))
    button_game = Button(527, 287, 522, 93, 'New Game', 'data\\Image\\backgrounds\\button.png')
    button_settings = Button(527, 439, 522, 93, 'Settings', 'data\\Image\\backgrounds\\button.png')
    button_quit = Button(527, 587, 522, 93, 'Quit', 'data\\Image\\backgrounds\\button.png')
    main = Menu([button_game, button_settings, button_quit, (text_surface, (520, 130))],
                'data\\Image\\backgrounds\\menu.png')
    current_size = get_json(['size'])
    surface = pygame.Surface(current_size)
    while True:
        cursor_position = pygame.mouse.get_pos()
        main.check_hovers(cursor_position)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_any()
            elif event.type == pygame.VIDEORESIZE:
                current_size = event.size
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_quit.is_hovered:
                    quit_any()
                elif button_game.is_hovered:
                    update_json(size=current_size)
                    return game
                elif button_settings.is_hovered:
                    update_json(size=current_size)
                    return settings
        main.draw(surface, screen, current_size)
        clock.tick(FPS)


def settings(screen, clock):
    from functions import Button, quit_any, FPS, get_json, update_json, change_music
    font = pygame.font.Font(None, 120)
    text_surface = font.render('Settings', False, (255, 255, 255))
    button_sound = Button(527, 287, 522, 93, f'Sound {"on" if get_json(["sound"]) else "off"}',
                          'data\\Image\\backgrounds\\button.png')
    button_faq = Button(527, 439, 522, 93, 'FAQ', 'data\\Image\\backgrounds\\button.png')
    button_back = Button(527, 587, 522, 93, 'Back', 'data\\Image\\backgrounds\\button.png')
    sett = Menu([button_sound, button_faq, button_back, (text_surface, (620, 120))],
                'data\\Image\\backgrounds\\menu.png')
    current_size = get_json(['size'])
    surface = pygame.Surface(current_size)
    while True:
        cursor_position = pygame.mouse.get_pos()
        sett.check_hovers(cursor_position)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_any()
            elif event.type == pygame.VIDEORESIZE:
                current_size = event.size
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_back.is_hovered:
                    update_json(size=current_size)
                    return main_menu
                elif button_faq.is_hovered:
                    update_json(size=current_size)
                    return faq
                elif button_sound.is_hovered:
                    button_sound.text = button_sound.text[:6] + {'on': 'off', 'off': 'on'}[button_sound.text[6:]]
                    update_json(sound=not get_json(['sound']))
                    change_music(get_json(['sound']))
        sett.draw(surface, screen, current_size)
        clock.tick(FPS)


def faq(screen, clock):
    from functions import Button, quit_any, FPS, get_json, update_json
    font1 = pygame.font.Font(None, 120)
    font2 = pygame.font.Font(None, 30)
    text_surface = font1.render('FAQ', False, (255, 255, 255))
    text_surface1 = font2.render("Используйте WASD и стрелочки для управления", False, (255, 255, 255))
    text_surface2 = font2.render("Ваша задача - переправится через реку", False, (255, 255, 255))
    text_surface3 = font2.render("Остерегайтесь комаров", False, (255, 255, 255))
    button_back = Button(527, 717, 522, 93, 'Back', 'data\\Image\\backgrounds\\button.png')
    FAQ = Menu([button_back, (text_surface, (700, 120)), (text_surface1, (550, 400)), (text_surface2, (550, 450)),
                (text_surface3, (550, 500))], 'data\\Image\\backgrounds\\FAQ.png')
    current_size = get_json(['size'])
    surface = pygame.Surface(current_size)
    while True:
        cursor_position = pygame.mouse.get_pos()
        FAQ.check_hovers(cursor_position)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_any()
            elif event.type == pygame.VIDEORESIZE:
                current_size = event.size
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_back.is_hovered:
                    update_json(size=current_size)
                    return settings
        FAQ.draw(surface, screen, current_size)
        clock.tick(FPS)


def win_menu(screen, clock):
    from functions import Button, quit_any, FPS, update_json, get_json
    from player import game
    font = pygame.font.Font(None, 120)
    text_surface = font.render('You win', False, (255, 255, 255))
    score, current_size = get_json(['score', 'size'])
    text_surface1 = font.render(f'Score: {score}', False, (255, 255, 255))
    button_game = Button(527, 439, 522, 93, 'Play Again', 'data\\Image\\backgrounds\\button.png')
    button_menu = Button(527, 587, 522, 93, 'Return to main menu', 'data\\Image\\backgrounds\\button.png')
    win = Menu([button_game, button_menu, (text_surface, (650, 300)), (text_surface1, (620, 120))],
               'data\\Image\\backgrounds\\menu.png')
    surface = pygame.Surface(current_size)
    while True:
        cursor_position = pygame.mouse.get_pos()
        win.check_hovers(cursor_position)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_any()
            elif event.type == pygame.VIDEORESIZE:
                current_size = event.size
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_menu.is_hovered:
                    update_json(size=current_size, score=0)
                    return main_menu
                elif button_game.is_hovered:
                    update_json(size=current_size)
                    return game
        win.draw(surface, screen, current_size)
        clock.tick(FPS)


def defeat_menu(screen, clock):
    from functions import Button, quit_any, FPS, update_json, get_json
    from player import game
    font = pygame.font.Font(None, 120)
    text_surface = font.render('You lose', False, (255, 255, 255))
    score, current_size = get_json(['score', 'size'])
    update_json(score=0)
    text_surface1 = font.render(f'Score: {score}', False, (255, 255, 255))
    button_game = Button(527, 439, 522, 93, 'Play Again', 'data\\Image\\backgrounds\\button.png')
    button_menu = Button(527, 587, 522, 93, 'Return to main menu', 'data\\Image\\backgrounds\\button.png')
    defeat = Menu([button_game, button_menu, (text_surface, (650, 300)), (text_surface1, (620, 120))],
                  'data\\Image\\backgrounds\\menu.png')
    surface = pygame.Surface(current_size)
    while True:
        cursor_position = pygame.mouse.get_pos()
        defeat.check_hovers(cursor_position)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_any()
            elif event.type == pygame.VIDEORESIZE:
                current_size = event.size
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_menu.is_hovered:
                    update_json(size=current_size)
                    return main_menu
                elif button_game.is_hovered:
                    update_json(size=current_size)
                    return game
        defeat.draw(surface, screen, current_size)
        clock.tick(FPS)
