import pygame
import constants
import player

def main():
    print("Starting asteroids!")

    # Initialize screen WIDTH and HEIGHT
    SCREEN_WIDTH, SCREEN_HEIGHT = constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Create screen object
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Initialize the display
    print(screen)
    
    # Create the player at the center of the screen
    x = constants.SCREEN_WIDTH / 2
    y = constants.SCREEN_HEIGHT / 2
    my_player = player.Player(x, y)
    
    
    # Game loop setup
    clock = pygame.time.Clock()
    dt = 0
    
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       
        my_player.update(dt)
        
        screen.fill((0, 0, 0))
       
        my_player.draw(screen)
        
        pygame.display.flip()
        
        delta_ms = clock.tick(60)
        dt = delta_ms / 1000

if __name__ == "__main__":
    main()