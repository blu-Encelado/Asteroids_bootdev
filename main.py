import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import *

#pygame.init()
#screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT / 2

def game_loop(screen, clock, player, updatable, drawable, asteroids, shots):

    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        for obj in asteroids:
            if obj.collision(player):
                print("GameOver")
                return
            for shot in shots:
                if shot.collision(obj):
                    obj.split()
                    shot.kill()

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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers =(updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x, y)
    asteroid_field = AsteroidField()
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    game_loop(screen, clock, player, updatable, drawable, asteroids, shots)


if __name__ == "__main__":
    main()
