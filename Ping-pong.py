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

    def move(self):

        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 750:
            self.rect.y += self.speed

window = display.set_mode((1000, 800))
display.set_caption("Шутер")
background = transform.scale(image.load("image/galaxy.jpg"), (1000, 800))

#текст 
font.init()
Text = font.Font(None, 35)


#Музыка-фон 

mixer.init()
#mixer.music.load("space.ogg")
# mixer.music.play() # отключил 

#Игровые эффекты 

kick = mixer.Sound("Music/kick.ogg")

#Спрайты 

Player_game_1 = Player("image/racket.png", 15, 75, 15, 5, 15)

finish = True
clock = time.Clock()
FPS = 60 
run = True
while run: 

    for e in event.get():
        if e.type == QUIT:
            run = False

   
    window.blit(background,(0, 0))
    Player_game_1.blid()
    Player_game_1.move()
    
    display.update()
    
    clock.tick(FPS)