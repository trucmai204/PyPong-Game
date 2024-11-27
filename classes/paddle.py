import pygame

class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 100
        self.color = (255, 255, 255)
        self.speed = 5

    def move_up(self, boost=False):
        self.y -= self.speed * (2 if boost else 1)

    def move_down(self, boost=False):
        self.y += self.speed * (2 if boost else 1)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def keep_within_bounds(self, screen_height):
        if self.y < 0:
            self.y = 0
        if self.y + self.height > screen_height:
            self.y = screen_height - self.height

    def ai_move(self, ball_x, ball_y, ball_dx):
        # Dự đoán vị trí của bóng dựa trên hướng và tốc độ
        if ball_dx > 0:  # Bóng đang di chuyển về phía paddle AI
            future_y = ball_y + (ball_dx / abs(ball_dx)) * (self.x - ball_x)
            if future_y > self.y + self.height // 2:
                self.y += self.speed
            elif future_y < self.y + self.height // 2:
                self.y -= self.speed