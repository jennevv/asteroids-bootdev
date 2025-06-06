import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            center=self.position,
            radius=self.radius,
            width=2,
            color="white",
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def reverse(self, dt):
        self.velocity *= -1
        self.position += self.velocity * 2 * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(20, 50)
            vel1 = self.velocity.rotate(+rand_angle)
            vel2 = self.velocity.rotate(-rand_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid1 = Asteroid(*self.position, new_radius)
            asteroid2 = Asteroid(*self.position, new_radius)

            asteroid1.velocity = 1.2 * vel1
            asteroid2.velocity = 1.2 * vel2




