import pygame, sys

# инициализация пайгейм
pygame.init()

#скорость 
fps = 144
clock = pygame.time.Clock()

# первоначальные данные
width = 1000
height = 1000
ActiveBrush = 0 #
ActiveColor = 'white' #

#создание экрана и заголовка игры 
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('P A I N T')
painting = [] #

# меню цветов и размеров
def DrawMenu(color, size):
    pygame.draw.rect(screen, 'gray', [0, 0, width, 90]) #
    pygame.draw.line(screen, 'black', (0, 90), (width, 90), 2)
    BigBrush = pygame.draw.rect(screen, 'black', [20, 20, 50, 50]) #
    pygame.draw.circle(screen, 'white', (45, 45), 20)
    MediumBrush = pygame.draw.rect(screen, 'black', [80, 20, 50, 50]) #
    pygame.draw.circle(screen, 'white', (105, 45), 15)
    SmallBrush = pygame.draw.rect(screen, 'black', [140, 20, 50, 50]) #
    pygame.draw.circle(screen, 'white', (165, 45), 10)
    RectBrush = pygame.draw.rect(screen, 'black', [200, 20, 50, 50]) #
    pygame.draw.circle(screen, 'white', (210, 30), 30)
    BrushList = [BigBrush, MediumBrush, SmallBrush, RectBrush]

    # показать какая кисть выбрана 
    if size == 20:
        pygame.draw.rect(screen, 'green', [20, 20, 50, 50], 3)
    if size == 15:
        pygame.draw.rect(screen, 'green', [80, 20, 50, 50], 3)
    if size == 10:
        pygame.draw.rect(screen, 'green', [140, 20, 50, 50], 3)
    if size == 5:
        pygame.draw.rect(screen, 'green', [200, 20, 50, 50], 3)
    
    #показать какой цвет выбран 
    pygame.draw.circle(screen, color, (400,45), 30)
    pygame.draw.circle(screen, 'darkgray', (400, 45), 30, 3)

    # цвета
    blue = pygame.draw.rect(screen, (0, 0, 255), [width-45, 20, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [width-45, 45, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [width-70, 20, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [width-70, 45, 25, 25])
    black = pygame.draw.rect(screen, (0, 0, 0), [width-95, 20, 25, 25])
    lightblue = pygame.draw.rect(screen, (0, 255, 255), [width-95, 45, 25, 25])
    eraser = pygame.draw.rect(screen, (255, 255, 255), [width-130, 20, 25, 25])
    ColorRect = [blue, red, green, yellow, black, lightblue, eraser]
    RgbList = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 0, 0),(0, 255, 255), (255, 255, 255)]

    return BrushList, ColorRect, RgbList

# функция для рисования 
def DrawPainting(paints):
    for paint in paints:
        if paint[2] == 5: # 
            pygame.draw.rect(screen, paint[0], (paint[1][0] - paint[2] // 2, paint[1][1] - paint[2] // 2, 35, 35))
        else: #
            pygame.draw.circle(screen, paint[0], paint[1], paint[2])

running = True
while running:
    clock.tick(fps) # fsp
    screen.fill('white')
    mouse = pygame.mouse.get_pos() # позиция мышки 
    click = pygame.mouse.get_pressed()[0] # шелк для рисования 
    
    # добавление новой фигуры 
    if click and mouse[1] > 90:
        painting.append((ActiveColor, mouse, ActiveBrush))
    
    # рисование фигур 
    if mouse[1] > 90:
        if ActiveBrush == 5:
            pygame.draw.rect(screen, ActiveColor, (mouse[0] - ActiveBrush // 2, mouse[1] - ActiveBrush // 2, 35, 35))
        else:
            pygame.draw.circle(screen, ActiveColor, mouse, ActiveBrush)
    
    DrawPainting(painting)

    brushes, colors, rgb = DrawMenu(ActiveColor, ActiveBrush)

    for event in pygame.event.get():

        # для оконц=чания игры
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # для ластика что бы стереть все что нарисовано 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                painting = []

        # поменять фигуру, цвет и размер
        if event.type == pygame.MOUSEBUTTONDOWN:
            for brush in range(len(brushes)):
                if brushes[brush].collidepoint(event.pos):
                    ActiveBrush = 20 - (brush*5)
        
            for color in range(len(colors)):
                if colors[color].collidepoint(event.pos):
                    ActiveColor = rgb[color]

    pygame.display.flip()