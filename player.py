import pygame


class Player:

    def __init__(self):
        self.score = 0
        self.health = 6
        self.X = 0
        self.Y = 4
        self.hight = 9
        self.width = 16
        self.movingX = 0
        self.movingY = 4
        self.sizeX = 100
        self.sizeY = 200
        self.screen_width = 1600
        self.screen_hight = 900
        self.cell_size = self.screen_width / self.width
        self.player_image = pygame.transform.scale(pygame.image.load('data\\Image\\player_image\\player2.png'), (100, 135))
        self.player_rect = self.player_image.get_rect(center=(self.cell_size * self.X + 50, self.cell_size * self.Y))

    def update(self, mass):
        from functions import get_json
        if 0 <= self.movingX < self.width and 0 <= self.movingY < self.hight and mass[self.movingY][self.movingX] != 0:
            self.X = self.movingX
            self.Y = self.movingY
            if mass[self.Y][self.X] == 1:
                sound = get_json(['sound'])
                if sound:
                    pygame.mixer.music.load('data\\music\\jump.mp3')
                    pygame.mixer.music.play()
            else:
                sound = get_json(['sound'])
                if sound:
                    pygame.mixer.music.load('data\\music\\ground.mp3')
                    pygame.mixer.music.play()
        else:
            if self.hight > self.movingY >= 0 <= self.movingX < self.width and mass[self.movingY][self.movingX] == 0:
                self.health -= 1
                sound = get_json(['sound'])
                if sound:
                    pygame.mixer.music.load('data\\music\\water1.mp3')
                    pygame.mixer.music.play()
            self.movingX = self.X
            self.movingY = self.Y

    def draw(self, surface):
        self.player_rect = self.player_image.get_rect(center=(self.cell_size * self.X + 50, self.cell_size * self.Y))
        surface.blit(self.player_image, self.player_rect)


def game(screen, clock):
    from functions import Board, Health, Score, quit_any, draw_background, FPS, get_json, update_json
    from menu import win_menu, defeat_menu
    total_score, current_size = get_json(['score', 'size'])
    move = True
    surface = pygame.Surface(current_size)
    board = Board()
    player = Player()
    health = Health(player.health)
    score = Score(total_score)
    while True:
        # cursor_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_any()
            elif event.type == pygame.VIDEORESIZE:
                current_size = event.size
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_w, pygame.K_DOWN, pygame.K_s, pygame.K_UP, pygame.K_d, pygame.K_RIGHT,
                                 pygame.K_a, pygame.K_LEFT] and move:
                    move = False
                    if event.key in [pygame.K_w, pygame.K_DOWN]:
                        player.movingY += 1
                    elif event.key in [pygame.K_s, pygame.K_UP]:
                        player.movingY -= 1
                    elif event.key in [pygame.K_d, pygame.K_RIGHT]:
                        player.movingX += 1
                    elif event.key in [pygame.K_a, pygame.K_LEFT]:
                        player.movingX -= 1
        if not move:
            move = True
            player.update(board.board)
            health.change(player.health)
            if player.health == 0:
                sound = get_json(['sound'])
                if sound:
                    pygame.mixer.music.load('data\\music\\die.mp3')
                    pygame.mixer.music.play()
                return defeat_menu
            if board.board[player.Y][player.X] == 2:
                update_json(score=get_json(['score']) + 1)
                sound = get_json(['sound'])
                if sound:
                    pygame.mixer.music.load('data\\music\\win_sound.mp3')
                    pygame.mixer.music.play()
                return win_menu
        draw_background(surface, 'data\\Image\\backgrounds\\river.jpg')
        board.draw(surface)
        player.draw(surface)
        health.draw(surface)
        score.draw(surface)
        scaled_surface = pygame.transform.scale(surface, current_size)
        screen.blit(scaled_surface, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)
