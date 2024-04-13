import pygame


class Player:

    def __init__(self):
        self.score = 0

        self.health = 6

        self.cordX = 0
        self.cordY = 4

        self.hight = 9
        self.width = 16

        self.movingX = 0
        self.movingY = 4

        self.finish = False

        self.sizeX = 100
        self.sizeY = 200

        self.screen_width = 1600
        self.screen_hight = 900

        self.cell_size = self.screen_width / self.width
        self.realcordX = 100 * self.cordX + 50
        self.realcordY = 100 * self.cordY

        # self.player_image = pygame.image.load('player_image/playe2r.png')
        self.player_image = pygame.transform.scale(pygame.image.load('player_image/playe2r.png'), (100, 135))
        self.player_rect = self.player_image.get_rect(center=(self.realcordX, self.realcordY))

        self.jump_sound1 = 'music/jamp.mp3'
        self.water1 = 'music/water1.mp3'
        self.bg_music = 'music/bgmusic.mp3'
        self.ground = 'music/ground.mp3'
        self.win_sound = 'music/win_sound.mp3'
        self.die = 'music/die.mp3'

    def death(self):
        if self.health == 0:
            pygame.mixer.music.load(self.die)
            pygame.mixer.music.play()
            return True
        else:
            return False

    def move(self, event, mass):
        if event.type == pygame.KEYDOWN:
            pygame.mixer.music.load(self.water1)
            if event.key == pygame.K_d:
                self.movingX += 1
                self.location(mass)
            elif event.key == pygame.K_a:
                self.movingX -= 1
                self.location(mass)
            elif event.key == pygame.K_w:
                self.movingY -= 1
                self.location(mass)
            elif event.key == pygame.K_s:
                self.movingY += 1
                self.location(mass)
            elif event.key == pygame.K_RIGHT:
                self.movingX += 1
                self.location(mass)
            elif event.key == pygame.K_LEFT:
                self.movingX -= 1
                self.location(mass)
            elif event.key == pygame.K_UP:
                self.movingY -= 1
                self.location(mass)
            elif event.key == pygame.K_DOWN:
                self.movingY += 1
                self.location(mass)



    def location(self, mass):

        if 0 <= self.movingX < self.width and 0 <= self.movingY < self.hight:
            if mass[self.movingY][self.movingX] == 0:
                pygame.mixer.music.load(self.water1)
                pygame.mixer.music.play()
                self.health -= 1
                self.movingX = self.cordX
                self.movingY = self.cordY
            else:
                if mass[self.movingY][self.movingX] == 1:
                    pygame.mixer.music.load(self.jump_sound1)
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load(self.ground)
                    pygame.mixer.music.play()
                self.cordX = self.movingX
                self.cordY = self.movingY
                if mass[self.cordY][self.cordX] == 2:
                    pygame.mixer.music.load(self.win_sound)
                    pygame.mixer.music.play()
                    self.Finish = True
        else:
            self.movingX = self.cordX
            self.movingY = self.cordY
    def draw(self, screen):
        self.realcordX = 100 * self.cordX + 50
        self.realcordY = 100 * self.cordY
        self.player_rect = self.player_image.get_rect(center=(self.realcordX, self.realcordY))
        screen.blit(self.player_image, self.player_rect)

