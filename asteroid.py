import circleshape
import constants
import pygame
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

        
 
    def update(self, dt):
        self.position += (self.velocity * dt)
        self.rect.center = (self.position.x, self.position.y)
        
    def split(self):
        self.kill()  # Remove the current asteroid from the game

        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return

        # Generate velocities for the new asteroids
        ran_angle = random.uniform(20, 50)
        velocity_1 = self.velocity.rotate(ran_angle) * 1.2
        velocity_2 = self.velocity.rotate(-ran_angle) * 1.2

        # Compute the radius of the new asteroids
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        # Create new asteroids (no need to pass group)
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = velocity_1

        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2.velocity = velocity_2
            