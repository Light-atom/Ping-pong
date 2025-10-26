from pygame import * 
from pygame import *
from random import *
import os 
from time import time as timer #импортируем функцию для засекания времени, чтобы интерпретатор не искал эту функцию в pygame модуле time, даём ей другое название сами

class GameSprite(sprite.Sprite):    
    def __init__(self, player_image, Box_x, Box_y, OX, OY, speed = 2 ):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(Box_x, Box_y))
        self.rect = self.image.get_rect()
        self.Box_x = Box_x
        self.Box_y = Box_y
        self.rect.x = OX 
        self.rect.y = OY
        self.speed = speed

    def blid(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):

    def move_up_down(self):

        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 750:
            self.rect.y += self.speed

    def move_W_S(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 750:
            self.rect.y += self.speed

window = display.set_mode((1000, 800))
display.set_caption("Шутер")
background = transform.scale(image.load("image/galaxy.jpg"), (1000, 800))

#текст 
font.init()
font = font.Font(None, 35)


#Музыка-фон 

mixer.init()
#mixer.music.load("space.ogg")
# mixer.music.play() # отключил 

#Игровые эффекты 

kick = mixer.Sound("Music/kick.ogg")

#Спрайты 


Player_game_1 = Player("image/racket.png", 40, 100, 25, 400, 15)
Player_game_2 = Player("image/racket.png", 40, 100, 945, 400, 15)
ball = GameSprite("image/tenis_ball.png", 50 , 50, 500, 400, 10 )

Player1 = font.render('Lose Player - 1',True, (255, 255, 255))
Player2 = font.render('Lose Player - 2',True, (255, 255, 255))
 
if randint(1, 2) == 1:
    speed_x = 3 
else: 
    speed_x = -3

if randint(1, 2) == 1:
    speed_y = 2
else: 
    speed_y = -2


finish = False
clock = time.Clock()
FPS = 60 
run = True
while run: 

    for e in event.get():
        if e.type == QUIT:
            run = False

    
    window.blit(background,(0, 0))

    if finish == False: 

        Player_game_1.blid()
        Player_game_1.move_up_down()
        Player_game_2.blid()
        Player_game_2.move_W_S()
        ball.blid()
        ball.rect.x += speed_x
        ball.rect.y += speed_y


        if sprite.collide_rect(ball, Player_game_1) or sprite.collide_rect(ball, Player_game_2):
            peremennay = randint(1, 3)
            #peremennay_X = randint(randint(-2, -1), randint(1, 5))

            speed_x *= -1


            if peremennay == 1: 
                speed_y *= 1

            elif  peremennay == 2: 
                speed_y *= 1

            else:
                speed_y *= -1

        if ball.rect.y < 0 or ball.rect.y > 750 :
            speed_y *= -1
            
            speed_1_1 = randint(1, 2)
            if speed_1_1 == 1:
                
                speed_x *= 1
            else:
                speed_x *= -1 
        
    
    if ball.rect.x > 950:
            
            window.blit(Player2, (500, 400))
            finish = True

    if ball.rect.x < 0:
            
            window.blit(Player1, (500, 400))
            finish = True

    display.update()
    
    clock.tick(FPS)
