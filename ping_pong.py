from pygame import *
import random

win_height = 700
window = display.set_mode((win_height,500))
display.set_caption('Пинг понг')
#background = transform.scale(image.load('field.png'), (700,500))
color = (252, 186, 3)
window.fill(color)

clock = time.Clock()
FPS = 60


lost = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_1(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.x < 650:
            self.rect.y += self.speed
    def update_2(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.x < 650:
            self.rect.y += self.speed


racket_1 = Player('racket.png', 50,200, 10, 50,80)
racket_2 = Player('racket.png', 600,200, 10, 50,80)

speed_x = 3
speed_y = 3

ball = GameSprite('ball.png', 100,200, 10, 70,50)

font.init()
font1 = font.SysFont('Arial', 35)

win1 = font1.render('победа 1ого', 1, (255,255,255))
win2 = font1.render('победа 2ого', 1, (255,255,255))

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        #window.draw()
        window.fill(color)
        racket_1.reset()
        racket_1.update_1()
        racket_2.reset()        
        racket_2.update_2()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(racket_1, ball) or sprite.collide_rect(racket_2, ball):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(win2, (200,200))
        if ball.rect.x > win_height:
            window.blit(win1, (200,200))


    #window.blit(background, (0,0))
    
    display.update()
    clock.tick(FPS)



'''class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = random.randint(65,635)
            lost = lost + 1'''
#mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.play()