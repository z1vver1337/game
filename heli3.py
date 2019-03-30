import pygame
import os
import random
def game():
    pygame.init()
    size = 1920, 1080
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    screen.fill((0, 0, 0))
    fps = 60
    v = 300
    n = 0
    w = 100
    delta_y = 250
    top = size[1] - delta_y
    bricks_number = size[0] // w + 2
    clock = pygame.time.Clock()
    dy = 70
    orange = (255, 127, 80)
    bricks_top = [400]
    bricks_bot = [680]
    y = 0
    helic_x = 100
    helic_y = 540
    running = True
    frames = 0
    x_left = 0
    score = 0
    pause = False
    image = pygame.image.load(os.path.join(os.getcwd(), 'heli.png'))
    image2 = pygame.image.load(os.path.join(os.getcwd(), 'heli2.png'))
    image3 = pygame.image.load(os.path.join(os.getcwd(), 'heli3.png'))
    myfont = pygame.font.SysFont('arial', 20)
    scorefont = pygame.font.SysFont('arial', 40)
    startfont = pygame.font.SysFont('arial', 70)
    overfont = pygame.font.SysFont('arial', 120)
    for i in range(1, bricks_number):
        while True:
            r = random.randrange(-dy, dy)
            y = bricks_top[i-1] + r
            if y > 0 and y <= top:
                break
        bricks_top.append(y)
        bricks_bot.append(y + delta_y + random.randrange(0, 200))
    for i in range(bricks_number):
        pygame.draw.rect(screen, orange, (w * i, 0, w, bricks_top[i]))
        pygame.draw.rect(screen, orange, (w * i, bricks_bot[i], w, size[1] - bricks_bot[i]))
    one = True
    while one:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                one = False
        screen.fill((0, 0, 0))
        for i in range(20):
            color = random.randrange(0, 255)
            pygame.draw.circle(screen, (color, color, color), (random.randrange(0, 1920), random.randrange(0, 1080)), 5)
            for i in range(200000):
                pass
        textsurface = startfont.render('НАЖМИТЕ ЛЮБУЮ КЛАВИШУ ДЛЯ НАЧАЛА ИГРЫ', False, (255, 255, 255))
        screen.blit(textsurface, (300, 540))
        pygame.display.flip()
        screen.blit(image, (helic_x, helic_y))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[273]:
                    helic_y -= 25 
                if pygame.key.get_pressed()[32]:
                    pause = not pause
                if pygame.key.get_pressed()[13]:
                    return False
        if pause:
            continue
        helic_y += 2
        screen.fill((0, 0, 0))
        for i in range(bricks_number):
            pygame.draw.rect(screen, orange, (w * i - x_left, 0, w, bricks_top[i]))
            pygame.draw.rect(screen, orange, (w * i - x_left, bricks_bot[i], w, size[1] - bricks_bot[i]))
        x_left += v / fps
        k = x_left / w
        k = int(k)
        if k >= 1:
            x_left = x_left % 20
            for i in range(bricks_number - k):
                bricks_top[i] = bricks_top[i + k]
                bricks_bot[i] = bricks_bot[i + k]
            for i in range(bricks_number - k, bricks_number):
                while True:
                    r = random.randrange(-dy, dy)
                    y = bricks_top[i - 1] + r
                    if y > 0 and y <= top:
                        break
                bricks_top[i] = y
                bricks_bot[i] = y + delta_y + random.randrange(0, 200)
        frames += 1
        score += v // 100 
        if frames == 300:
            frames = 0
            v += 50
        if (frames // 5) % 2 == 0:
            screen.blit(image, (helic_x, helic_y))
        else:
            screen.blit(image2, (helic_x, helic_y))
        textsurface = scorefont.render('ВАШ СЧЁТ:' + str(score), False, (255, 255, 255))
        screen.blit(textsurface, (1400, 1000))
        textsurface = myfont.render('НАЖМИТЕ ENTER ДЛЯ НОВОЙ ИГРЫ', False, (255, 255, 255))
        screen.blit(textsurface, (50, 50))
        textsurface = myfont.render('НАЖМИТЕ ПРОБЕЛ ДЛЯ ПАУЗЫ', False, (255, 255, 255))
        screen.blit(textsurface, (50, 80))
        clock.tick(fps)
        pygame.display.flip()
        nc = (helic_x + 120) // w + 1
        for i in range(nc):
            if helic_x <= w * i - x_left <= helic_x + 120:
                if bricks_top[i] >= helic_y or bricks_bot[i] <= helic_y + 80:
                    over = overfont.render('GAME OVER', False, (255, 255, 255))
                    screen.blit(over, (600, 480))
                    screen.blit(image3, (helic_x, helic_y))
                    pygame.display.flip()
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                exit()
                            if event.type == pygame.KEYDOWN:
                                 if pygame.key.get_pressed()[13]:
                                     return False
while True:
    if game() == False:
        game()

