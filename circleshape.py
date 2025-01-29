import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        
        # Create a square surface big enough for the circle
        size = radius * 2  # diameter
        self.image = pygame.Surface((size, size))
        # Make the background transparent
        self.image.set_colorkey((0, 0, 0))
        # Draw the circle on the surface
        pygame.draw.circle(self.image, (255, 255, 255), (radius, radius), radius)
        # Create the rect for positioning
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        self.rect.center = self.position
        self.rect.center = (self.position.x, self.position.y)
        
    def collision(self, other):
        distance = pygame.math.Vector2.distance_to(self.position, other.position) 
        return distance <= (self.radius + other.radius)