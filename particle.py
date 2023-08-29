import random
import math
import pygame

class Particle:
    # Load the image once, so it's shared across all particles
    PERSON_IMAGE = pygame.image.load("C:\HMV_Wheel_Bot\pfp\ise.jpeg")
    PERSON_IMAGE = pygame.transform.scale(PERSON_IMAGE, (50, 40))  # Resize image if needed

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.uniform(2, 5)
        self.direction = random.uniform(0, 2 * math.pi)

    def move(self):
        self.x += self.speed * math.cos(self.direction)
        self.y += self.speed * math.sin(self.direction)

    def draw(self, surface):
        surface.blit(self.PERSON_IMAGE, (self.x, self.y))
