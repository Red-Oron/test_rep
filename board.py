import pygame
from random import randint


class Board:
    def __init__(self):
        self.width = 16
        self.height = 9
        self.size = 100
        self.board = self.generate()
        self.lily = pygame.image.load('objects/lily.png')
        self.lily = pygame.transform.scale(self.lily, (self.size, self.size))

    def draw(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 1:
                    screen.blit(self.lily,(self.size*j, self.size*i))

    def generate(self):
        return [list(map(int, ['2', '2', '2'] + list(i)[:-1] + ['2', '2', '2'])) for i in open(f'levels/level_{randint(1, 7)}.txt').readlines()]

