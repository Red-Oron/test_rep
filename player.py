import pygame
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.health, self.X, self.Y, self.movingX, self.movingY = 6, 0, 4, 0, 4
        self.hight, self.width, self.cell_size = 9, 16, 100
        self.player_image = pygame.transform.scale(pygame.image.load('data\\Image\\player_image\\player2.png'), (100, 135))
        self.rect = self.player_image.get_rect(center=(self.cell_size * self.X + 50, self.cell_size * self.Y))

    def update(self, mass):
        from functions import get_json
        sound = get_json(['sound'])
        if self.hight > self.movingY >= 0 <= self.movingX < self.width and mass[self.movingY][self.movingX] != 0:
            if sound:
                if mass[self.movingY][self.movingX] == 1:
                    pygame.mixer.music.load('data\\music\\jump.mp3')
                else:
                    pygame.mixer.music.load('data\\music\\ground.mp3')
                pygame.mixer.music.play()
            self.X = self.movingX
            self.Y = self.movingY
        else:
            if self.hight > self.movingY >= 0 <= self.movingX < self.width and mass[self.movingY][self.movingX] == 0:
                self.X, self.Y = 0, 4
                self.health -= 1
                if sound:
                    pygame.mixer.music.load('data\\music\\water1.mp3')
                    pygame.mixer.music.play()
                self.movingX, self.movingY = 0, 4

    def draw(self, surface):
        self.rect = self.player_image.get_rect(center=(self.cell_size * self.X + 50, self.cell_size * self.Y))
        surface.blit(self.player_image, self.rect)


def game(screen, clock):
    from functions import Board, draw_health, quit_any, draw_background, FPS, get_json, update_json, draw_score, mosquitoes_music
    from menu import win_menu, defeat_menu
    from enemy import Enemy
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    score, current_size, sound = get_json(['score', 'size', 'sound'])
    move, sound_mosquitoes = True, True
    surface = pygame.Surface(current_size)
    board = Board()
    player = Player()
    mosquitoes = pygame.sprite.Group()
    while True:
        if sound:
            if sound_mosquitoes and len(mosquitoes) > 0:
                mosquitoes_music(True)
                sound_mosquitoes = False
            elif not sound_mosquitoes and len(mosquitoes) == 0:
                mosquitoes_music(False)
                sound_mosquitoes = True
        # cursor_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_any()
            elif event.type == pygame.VIDEORESIZE:
                current_size = event.size
            elif event.type == pygame.USEREVENT:
                mosquitoes.add(Enemy(randint(300, 1300), randint(5, 10)))
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_w, pygame.K_DOWN, pygame.K_s, pygame.K_UP, pygame.K_d, pygame.K_RIGHT,
                                 pygame.K_a, pygame.K_LEFT] and move:
                    move = False
                    if event.key in [pygame.K_s, pygame.K_DOWN]:
                        player.movingY = player.Y + 1
                    elif event.key in [pygame.K_w, pygame.K_UP]:
                        player.movingY = player.Y - 1
                    elif event.key in [pygame.K_d, pygame.K_RIGHT]:
                        player.movingX = player.X + 1
                    elif event.key in [pygame.K_a, pygame.K_LEFT]:
                        player.movingX = player.X - 1
        if not move:
            move = True
            player.update(board.board)
        mosquitoes.update()
        if pygame.sprite.spritecollide(player, mosquitoes, True):
            player.health -= 1
            player.X, player.Y = 0, 4
            player.movingX, player.movingY = 0, 4
        if player.health == 0:
            mosquitoes_music(False)
            if sound:
                pygame.mixer.music.load('data\\music\\die.mp3')
                pygame.mixer.music.play()
            return defeat_menu
        if board.board[player.Y][player.X] == 2:
            mosquitoes_music(False)
            update_json({'score': get_json(['score']) + 1})
            sound = get_json(['sound'])
            if sound:
                pygame.mixer.music.load('data\\music\\win_sound.mp3')
                pygame.mixer.music.play()
            return win_menu
        draw_background(surface, 'data\\Image\\backgrounds\\river.jpg')
        board.draw(surface)
        player.draw(surface)
        mosquitoes.draw(surface)
        draw_health(surface, player.health)
        draw_score(surface, score)
        scaled_surface = pygame.transform.scale(surface, current_size)
        screen.blit(scaled_surface, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)
