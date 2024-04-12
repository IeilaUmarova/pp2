import pygame
from pygame.locals import *
import random, time

# инициализация пайгейма
pygame.init()

# создание поля
width = 500
height = 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('RACE GAME')

# цвета
green = (76, 208, 56)
red = (200, 0, 0)
white = (255, 255, 255)
yellow = (255, 232, 0)
gray = (100, 100, 100)

# первоначальнные данные
gameover = False 
speed = 5 
score = 0
coin_score = 0 

# настроика шрифта
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, (0, 0, 0))

# параметры дороги
marker_width = 5
marker_height = 50
road = (20, 0, 360, height)
left_edge_marker = (15, 0, marker_width, height)
right_edge_marker = (380, 0, marker_width, height)

# расположении дорожных линии
left_lane = 85
center_lane = 215
right_lane = 345
lanes = [left_lane, center_lane, right_lane]

# для движения дорожных линии
lane_marker_move = 0

# класс для встречных машин и игрока
class Vehicle(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)

        # подбор размера для изображения для поля
        image_scale = 45 / image.get_rect().width
        new_width = image.get_rect().width * image_scale
        new_height = image.get_rect().height * image_scale
        self.image = pygame.transform.scale(image, (new_width, new_height))

        # позиция машины
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

# класс машины игрока от класса машины
class PlayerVehicle(Vehicle):
    def __init__(self, x, y):
        # Load the player's car image
        image = pygame.image.load('/Users/leila/Desktop/pp2_Leila_Umarova/practice/lab8/image/car3.png')
        super().__init__(image, x, y)

# первоначальная позиция игрока
player_x = 200
player_y = 500

# создание груп для игрока, монет и встречных машин 
player_group = pygame.sprite.Group()
vehicle_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
player = PlayerVehicle(player_x, player_y)
player_group.add(player)

# загрузка изоброжении для монет и встречных машин 
enemy_image = pygame.image.load('/Users/leila/Desktop/pp2_Leila_Umarova/practice/lab8/image/car1.png')
coin_image = pygame.image.load('/Users/leila/Desktop/pp2_Leila_Umarova/practice/lab9/coin.png')
image_scale = 45 / coin_image.get_rect().width
new_width = coin_image.get_rect().width * image_scale
new_height = coin_image.get_rect().height * image_scale
n_coinimage = pygame.transform.scale(coin_image, (new_width, new_height))

# случай при котором скорость будет рости 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# основной игровой цикл
clock = pygame.time.Clock()
fps = 60
running = True
while running:
    clock.tick(fps)

    # обработка событии
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            speed += 0.5 
        if event.type == QUIT:
            running = False

        # движение игрока на право и на лево 
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT] and player.rect.center[0] > 0:
            player.rect.x -= 30
        if pressed_keys[pygame.K_RIGHT] and player.rect.center[0] < 380:
            player.rect.x += 30

    # задний фон
    screen.fill(green)
    pygame.draw.rect(screen, gray, road)
    pygame.draw.rect(screen, yellow, left_edge_marker)
    pygame.draw.rect(screen, yellow, right_edge_marker)

    # движение дорожных линии
    lane_marker_move += speed * 2
    if lane_marker_move >= marker_height * 2:
        lane_marker_move = 0
    for y in range(marker_height * -2, height, marker_height * 2):
        pygame.draw.rect(screen, white, (left_lane + 45, y + lane_marker_move, marker_width, marker_height))
        pygame.draw.rect(screen, white, (center_lane + 45, y + lane_marker_move, marker_width, marker_height))

    # нарисовка игрока
    player_group.draw(screen)

    # добавление машины и монет
    if len(vehicle_group) < 2:
        add_vehicle = True
        for vehicle in vehicle_group:
            if vehicle.rect.top < vehicle.rect.height * 1.5:
                add_vehicle = False
                break
        if add_vehicle:
            coin = Vehicle(n_coinimage, random.randint(left_lane, right_lane), height / -2)
            coin_group.add(coin)
            vehicle = Vehicle(enemy_image, random.randint(left_lane, right_lane), height / -2)
            vehicle_group.add(vehicle)

    # движение машины и монет
    for vehicle in vehicle_group:
        vehicle.rect.y += speed
        if vehicle.rect.top >= height:
            vehicle.kill()
            score += 1
    for coin in coin_group:
        coin.rect.y += speed
        if coin.rect.top >= height:
            coin.kill()    

    # зарисока машины и монет
    vehicle_group.draw(screen)
    coin_group.draw(screen)

    # отоброжение результатов
    text = font_small.render('Score: ' + str(score), True, white)
    text_rect = text.get_rect()
    text_rect.center = (70, 100)
    screen.blit(text, text_rect)

    c_text = font_small.render('Coins: ' + str(coin_score), True, white)
    c_text_rect = c_text.get_rect()
    c_text_rect.center = (330, 100)
    screen.blit(c_text, c_text_rect)

    # проверка крушения машины
    if pygame.sprite.spritecollideany(player, vehicle_group):
        pygame.mixer.Sound("/Users/leila/Desktop/pp2_Leila_Umarova/practice/lab8/songs/crash.wav").play()
        time.sleep(0.5)
        screen.fill(red)
        screen.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in vehicle_group:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
    
    if pygame.sprite.spritecollideany(player, coin_group):
        pygame.mixer.Sound("/Users/leila/Desktop/pp2_Leila_Umarova/practice/lab9/coin.wav").play()
        coin_score += 1
        for coin in coin_group:
            coin.kill()
    
    pygame.display.update()