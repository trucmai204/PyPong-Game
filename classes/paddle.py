import pygame

class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 100
        self.color = (255, 255, 255)
        self.speed = 5
    def move_up(self):
        self.y -= self.speed
    def move_down(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def keep_within_bounds(self, screen_height):
        if self.y < 0:
            self.y = 0
        if self.y + self.height > screen_height:
            self.y = screen_height - self.height

    def ai_move(self, ball_y):
        if ball_y > self.y + self.height // 2:
            self.y += self.speed + 1  # Tăng tốc
        elif ball_y < self.y + self.height // 2:
            self.y -= self.speed + 1