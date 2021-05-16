from pygame import *


window = display.set_mode((500, 500))
back = (255, 219, 38)
window.fill(back)

font.init()
font = font.SysFont("Impact", 70)
lose = font.render("здох 1", True, (255, 0, 0))
lose2 = font.render("здох 2", True, (255, 0, 0))

speed_x = 3
speed_y = 3

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

game_over = False

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

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(raketka, ball) or sprite.collide_rect(raketka2, ball):
            speed_x *= -1
            speed_y *= -1

        if ball.rect.y > 400 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose, (200, 200))
            game_over = True

        if ball.rect.x > 500:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True

    display.update()
    clock.tick(60)









