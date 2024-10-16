import pygame

class Score:
    def __init__(self, screen_width):
        self.left_score = 0
        self.right_score = 0
        self.font = pygame.font.Font(None, 74)
        self.screen_width = screen_width

    def update(self, screen):
        left_text = self.font.render(str(self.left_score), True, (255, 255, 255))
        right_text = self.font.render(str(self.right_score), True, (255, 255, 255))

        screen.blit(left_text, (self.screen_width // 4, 10))
        screen.blit(right_text, (self.screen_width * 3 // 4, 10))

    def left_point(self):
        self.left_score += 1

    def right_point(self):
        self.right_score += 1
