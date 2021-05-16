from pygame import *


window = display.set_mode((500, 500))
back = (255, 219, 38)
window.fill(back)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.width = width
        self.height = height
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 80:
            self.rect.y += self.speed

raketka = Player("raketka.png", 10, 400, 4.5, 90, 90)
raketka2 = Player("raketka.png", 390, 400, 4.5, 90, 90)
ball = GameSprite("pong.png", 220, 250, 2, 30, 30)

clock = time.Clock()
finish = False
game = True
while game:
    for events in event.get():
        if events.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        raketka.reset()
        raketka2.reset()
        raketka.update()
        raketka2.update2()
        ball.reset()
    display.update()
    clock.tick(60)









