import circleshape
import constants
import pygame

class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.SHOT_RADIUS)
        
    def update(self, dt):
        self.position += (self.velocity * dt)
        self.rect.center = (self.position.x, self.position.y)