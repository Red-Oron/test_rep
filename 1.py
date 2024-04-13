if __name__ == '__main__':
    pygame.init()
    size = width, height = 100, 100
    screen = pygame.display.set_mode(size)
while True:
    screen.fill((0,0,0))
    draw(ma,screen)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()