import pygame
import random

class Ball:
    def __init__(self, screen_width, screen_height):
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.radius = 10
        self.dx = random.choice([-1, 1]) * random.randint(3, 6)
        self.dy = random.choice([-1, 1]) * random.randint(3, 6)
        self.color = (255, 0, 0)
        self.speed = 0.03

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def bounce(self, screen_height):
        if self.y - self.radius < 0 or self.y + self.radius > screen_height:
            self.dy *= -1

    def reset(self, screen_width, screen_height):
        self.x = screen_width // 2
        self.y = screen_height // 2
        self.dx *= -1
        self.dy = random.choice([-1, 1]) * random.randint(3, 6)
