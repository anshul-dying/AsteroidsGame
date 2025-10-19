from circleshape import CircleShape
from constants import *
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        # Immediately remove the current asteroid.
        self.kill()

        # If the asteroid is already the smallest size, just return.
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Generate a random split angle between 20 and 50 degrees.
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors by rotating the current velocity.
        new_velocity_1 = self.velocity.rotate(random_angle) * 1.2
        new_velocity_2 = self.velocity.rotate(-random_angle) * 1.2

        # Calculate the new radius for the smaller asteroids.
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new Asteroid objects at the current position with the new radius and velocities.
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity_1

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_velocity_2
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def draw(self, screen):
        pygame.draw.circle(screen, "grey", (int(self.position.x), int(self.position.y)), int(self.radius), 2)