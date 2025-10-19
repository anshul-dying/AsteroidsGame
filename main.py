import pygame
from player import Player
from constants import *
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

import sys

def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # --- Create groups ---
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assign groups to Player class (so new Players auto-add)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (updatable, shots, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit(1)

            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill() 
                    # asteroid.kill()

        screen.fill((0,0,0))
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        
        time_passed = clock.tick(60)
        dt = time_passed/1000.0

        print(f"DT: {dt}   passed: {time_passed}")
    # print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen width: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
