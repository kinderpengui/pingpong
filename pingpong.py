import pygame


window = pygame.display.set_mode((500, 500))
back = (255, 219, 38)
window.fill(back)

clock = pygame.time.Clock()
finish = False
game = True
while game:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            game = False
    """if finish != True:"""
    pygame.display.update()
    clock.tick(60)









