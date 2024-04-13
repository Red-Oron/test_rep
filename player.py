import pygame


class player:

    def __init__(self):

        self.health = 6

        self.cordX = 0
        self.cordY = 2

        self.hight = 9
        self.width = 16

        self.movingX = 0
        self.movingY = 2

        self.finish = False

        self.sizeX = 765
        self.sizeY = 1035

        self.player_image = pygame.image.load('image')
    def death(self):
        if self.health == 0:
            return True
        else:
            return False

    def move(self, event,mass):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.movingX += 1
            elif event.key == pygame.K_LEFT:
                self.movingX -= 1
            elif event.key == pygame.K_UP:
                self.movingY += 1
            elif event.key == pygame.K_DOWN:
                self.movingY -= 1
            self.location(mass)

    def location(self, screen, mass):
        if self.movingX<=self.width and self.movingX>=0 and self.movingY<=self.hight and self.movingY>=0:
            if mass[self.cordX, self.cordY] == 0:
                self.health -= 1
                self.movingX = self.cordX
                self.movingY = self.cordY
            else:
                self.cordX = self.movingX
                self.cordY = self.movingY
                if mass[self.cordX, self.cordY] == 2: self.Finish = True
        screen.blit(self.player_image, self.player_image.get_rect(bottomright=(self.sizeX, self.sizeY)))


