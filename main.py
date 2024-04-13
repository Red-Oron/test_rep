import pygame
from random import randint


class Board:
    def __init__(self):
        self.width = 8
        self.height = 5
        self.board = self.generate()
        for i in self.board:
            print(*i)

    def generate(self):
        return [list(map(int, ['1'] + list(i)[:-1] + ['1'])) for i in open(f'levels/level_{randint(1, 2)}.txt').readlines()]

board = Board()
