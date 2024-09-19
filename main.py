# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import *

def main():
    pygame.init()
    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2))
    dt = 0

    while True:
        # Will allow user to close the game using the X button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Allow the player to turn left or right. Calling before rendering.
        player.update(dt)

        # Will the screen black
        pygame.Surface.fill(screen, (0, 0, 0))

        # Draw the player on the screen
        player.draw(screen)

        # Refresh the display to show the triangle
        pygame.display.flip()

        # Limit the framerate to 60 FPS    
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()