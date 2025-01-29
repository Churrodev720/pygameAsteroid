import pygame
import constants
import player
import asteroid
import asteroidfield


def main():
    pygame.init()
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
    
    
    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    player.Player.containers = (updatable, )
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable,)
    
    my_player = player.Player(x, y)
    asteroid_field = asteroidfield.AsteroidField()
    # Game loop setup
    clock = pygame.time.Clock()
    dt = 0
    
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       
        for asteroi in asteroids:  #checks collision
            if my_player.collision(asteroi):  
                print("Game over!")
                return
        
        updatable.update(dt)
        
        screen.fill((0, 0, 0))
        
        my_player.draw(screen)
       
        drawable.draw(screen)
        
        pygame.display.flip()
        
        delta_ms = clock.tick(60)
        dt = delta_ms / 1000

if __name__ == "__main__":
    main()