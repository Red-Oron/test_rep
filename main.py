import pygame


if __name__ == '__main__':
    from menu import main_menu
    from functions import change_music, update_json
    update_json(size=(1600, 900), sound=True, score=0)
    pygame.init()
    screen = pygame.display.set_mode((1600, 900), pygame.RESIZABLE)
    pygame.display.set_caption('The path of water lilies')
    scene = main_menu
    clock = pygame.time.Clock()
    change_music(True)
    while scene is not None:
        scene = scene(screen, clock)
