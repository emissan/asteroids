# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # Add group classes to hold and manage multiple objects for easier tracking
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add the different classes to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable)

    # Player and asteroid field created
    player = Player((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()

    while True:
        # Will allow user to close the game using the X button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Allow the player to turn left or right. Calling before rendering.
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print(f"Game over!")
                sys.exit()

        # Will the screen black
        pygame.Surface.fill(screen, (0, 0, 0))

        # Draw the player on the screen
        for obj in drawable:
            obj.draw(screen)

        # Refresh the display to show the triangle
        pygame.display.flip()

        # Limit the framerate to 60 FPS    
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()