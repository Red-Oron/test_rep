import pygame
from random import randint


class Board:
    def __init__(self):
        self.width = 16
        self.height = 9
        self.size = 100
        self.board = self.generate()

    def draw(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 0:
                    pygame.draw.rect(screen, (0, 0, 255), (self.size * j, self.size * i, self.size, self.size))
                if self.board[i][j] == 1:
                    pygame.draw.rect(screen, (255, 0, 0), (self.size * j, self.size * i, self.size, self.size))

    def generate(self):
        return [list(map(int, ['1'] + list(i)[:-1] + ['2'])) for i in open(f'levels/level_{randint(1, 5)}.txt').readlines()]

