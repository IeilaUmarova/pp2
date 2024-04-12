import pygame 
from random import randrange 

#рабочее окно
RES = 800
SIZE = 50

#начальное положение змейки и яблоко
x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
dirs = {'W': True, 'S': True, 'A': True, 'D': True}
length = 1 #длина змейки
snake = [(x, y)]
dx, dy = 0, 0 #направление движения 
fps = 5 #скорость змейки
score = 0

pygame.init()
sc = pygame.display.set_mode([RES, RES]) #создали рабочее окно
clock = pygame.time.Clock() #для регулировки скорости змейки
font_score = pygame.font.SysFont('Arial', 25, bold = True) #размер и шрифт для набронных очков
font_end = pygame.font.SysFont('Arial', 30, bold = True) #так же для конечной надписи

while True:
    sc.fill(pygame.Color('black'))
    #нарисуем змейку
    [(pygame.draw.rect(sc, pygame.Color('blue'), (i, j, SIZE-2, SIZE-2))) for i, j in snake]
    #нарисуем яблоко
    pygame.draw.rect(sc, pygame.Color('pink'), (*apple, SIZE, SIZE))
    #размещение надписи
    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('white'))
    sc.blit(render_score, (5, 5))

    #движение змейки
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]

    #поедание яблоко
    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        fps += 1
        score += 1

    #случай проигрыша
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('white'))
            sc.blit(render_end, (RES // 2 - 200, RES // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    pygame.display.flip() #обновляем поверхность
    clock.tick(fps) #задержка для fps

    #зкрытие приложения 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #управление
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}