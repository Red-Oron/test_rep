import pygame
import sys
from random import randint
import json


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
        if self.hover_image is not None:
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

    def check_hover(self, cursor):
        self.is_hovered = self.text_rect.collidepoint(cursor) if self.image is None else self.rect.collidepoint(cursor)


class Board:
    def __init__(self):
        self.width = 16
        self.height = 9
        self.size = 100
        self.board = [list(map(int, ['3', '3', '3'] + list(i)[:-1] + ['2', '2', '2'])) for i in
                      open(f'data\\levels\\level_{randint(1, 15)}.txt').readlines()]
        self.lily = pygame.transform.scale(pygame.image.load('data\\Image\\objects\\lily.png'), (self.size, self.size))

    def draw(self, surface):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 1:
                    surface.blit(self.lily, (self.size * j, self.size * i))


def draw_health(surface, health):
    hp_sprite = pygame.transform.scale(pygame.image.load('data\\Image\\objects\\heart.png'), (100, 100))
    surface.blit(hp_sprite, (10, 10))
    font = pygame.font.Font(None, 75)
    text_surface = font.render(str(health), False, (255, 255, 255))
    surface.blit(text_surface, (46, 42))


def draw_score(surface, score):
    star = pygame.transform.scale(pygame.image.load('data\\Image\\objects\\star.png'), (100, 100))
    surface.blit(star, (110 + 10, 12))
    font = pygame.font.Font(None, 65)
    text_surface = font.render(str(score), False, (0, 0, 0))
    surface.blit(text_surface, (110 + 49, 41))


def draw_background(surface, image):
    background = pygame.transform.scale(pygame.image.load(image), (1600, 900))
    surface.blit(background, background.get_rect(bottomright=(1600, 900)))


def quit_any():
    pygame.quit()
    sys.exit()


def update_json(sl):
    with open("data\\data.json", "r+") as jsonFile:
        data = json.load(jsonFile)
        data.update(sl)
        jsonFile.seek(0)
        json.dump(data, jsonFile)
        jsonFile.truncate()


def get_json(arr):
    sp = []
    with open("data\\data.json", "r+") as jsonFile:
        with open("data\\data_const.json", 'r+') as jsonFile_const:
            data = json.load(jsonFile)
            data_const = json.load(jsonFile_const)
            for i in arr:
                sp.append(data.get(i, data_const[i]))
    return sp if len(sp) != 1 else sp[0]


def change_music(f):
    background_sound.play(-1).set_volume(0.2) if f else background_sound.stop()


pygame.init()
FPS = 100
background_sound = pygame.mixer.Sound('data\\music\\bg_music.mp3')
