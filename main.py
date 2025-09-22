import pygame
from constants import *
from player import *

#pygame.init()
#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

def game_loop(screen, clock, updatable, drawable):

    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        
        screen.fill("black")

        for draw in drawable:
            draw.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(x, y)

    game_loop(screen, clock, updatable, drawable)
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
