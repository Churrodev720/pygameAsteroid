import circleshape
import constants
import pygame
import shot

class Player(circleshape.CircleShape):
    def __init__(self, x, y, shots_group):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.shots_group = shots_group
        self.timer = 0
        
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)
        
    def rotate(self, dt):
    # Increment or decrement the rotation angle
        self.rotation += constants.PLAYER_TURN_SPEED * dt
        
    def update(self, dt):
        super().update(dt)
        keys = pygame.key.get_pressed()
        self.shots_group.update(dt)
        
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        if keys[pygame.K_a]:
            self.rotate(-dt)  # Rotate left
        if keys[pygame.K_d]:
            self.rotate(dt)   # Rotate right
        if keys[pygame.K_w]:  
            self.move(dt)     #move forward
        if keys[pygame.K_s]:
            self.move(-dt)    #move backwards
            
        self.timer += -dt
            
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt
    
    def shoot(self):
        if self.timer <= 0:
            new_shot = shot.Shot(self.position.x, self.position.y)
            direction = pygame.Vector2(0, 1)
            direction = direction.rotate(self.rotation)
            direction = direction * constants.PLAYER_SHOOT_SPEED
            new_shot.velocity = direction
            self.shots_group.add(new_shot)
            self.timer = constants.PLAYER_SHOOT_COOLDOWN
        
        