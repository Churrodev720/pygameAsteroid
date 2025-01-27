import circleshape
import constants
import pygame

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
 
    def update(self, dt):
        self.position += (self.velocity * dt)
        self.rect.center = (self.position.x, self.position.y)