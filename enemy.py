import pygame
import random
from main import screen

# инициализация pygame
pygame.init()

# установка размеров окна
win = screen

class Object(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('objects/mosquito.png'), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1600)
        self.rect.y = 900
        self.vel = random.randint(1, 3)

    def update(self):
        self.rect.y -= self.vel

# создание группы спрайтов
all_objects = pygame.sprite.Group()

# основной игровой цикл
run = True
clock = pygame.time.Clock()
while run:
    clock.tick(120)

    # проверка на закрытие окна
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # создание нового объекта и добавление его в группу
    if random.randint(1, 100) == 1:
        new_object = Object()
        all_objects.add(new_object)

    # обновление и отрисовка спрайтов
    all_objects.update()

    win.fill((0, 0, 0))
    all_objects.draw(win)
    pygame.display.update()