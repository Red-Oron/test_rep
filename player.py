import sys
import pygame


class Player:
    def __init__(self):
        self.health = 6
        self.cordX = 0
        self.cordY = 2

    def death(self):
        if self.health == 0:
            return True
        else:
            return False

    def move(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.cordX += 1
            elif event.key == pygame.K_LEFT:
                self.cordX -= 1
            elif event.key == pygame.K_UP:
                self.cordY += 1
            elif event.key == pygame.K_DOWN:
                self.cordY -= 1

    def location(self, mass):
        if mass[self.cordX, self.cordY] == 0:
            self.health -= 1
        elif mass[self.cordX, self.cordY] == 2: True
