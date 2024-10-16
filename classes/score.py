import pygame
import os
from collections import defaultdict

class Score:
    def __init__(self, screen_width, mode='single'):
        self.left_score = 0
        self.right_score = 0
        self.font = pygame.font.Font(None, 74)
        self.screen_width = screen_width
        self.high_scores = defaultdict(int)  # Sử dụng defaultdict để quản lý điểm cao
        self.mode = mode
        self.load_high_scores()

    def load_high_scores(self):
        """Tải điểm cao từ tệp nếu tồn tại."""
        if os.path.exists("high_score.txt"):
            try:
                with open("high_score.txt", "r") as file:
                    scores = file.read().strip().split(',')
                    if len(scores) >= 2:
                        self.high_scores['single'] = int(scores[0])
                        self.high_scores['multi'] = int(scores[1])
                    elif len(scores) == 1:
                        self.high_scores['single'] = int(scores[0])
                    else:
                        self.high_scores['single'] = 0
                        self.high_scores['multi'] = 0
            except (ValueError, IOError):
                self.high_scores['single'] = 0
                self.high_scores['multi'] = 0
        else:
            self.high_scores['single'] = 0
            self.high_scores['multi'] = 0

    def save_high_scores(self):
        """Lưu điểm cao vào tệp."""
        try:
            with open("high_score.txt", "w") as file:
                file.write(f"{self.high_scores['single']},{self.high_scores['multi']}")
        except IOError:
            print("Error saving high scores.")

    def update(self, screen):
        """Cập nhật và vẽ điểm số lên màn hình."""
        left_text = self.font.render(str(self.left_score), True, (255, 255, 255))
        right_text = self.font.render(str(self.right_score), True, (255, 255, 255))

        high_score_text = self.font.render(f"High Score: {self.high_scores[self.mode]}", True, (255, 255, 255))

        screen.blit(left_text, (self.screen_width // 4, 10))
        screen.blit(right_text, (self.screen_width * 3 // 4, 10))
        screen.blit(high_score_text, (self.screen_width // 2 - high_score_text.get_width() // 2, 60))

    def left_point(self):
        """Cập nhật điểm cho người chơi bên trái."""
        self.left_score += 1
        self.update_high_score()

    def right_point(self):
        """Cập nhật điểm cho người chơi bên phải."""
        self.right_score += 1
        self.update_high_score()

    def update_high_score(self):
        """Cập nhật và lưu điểm cao."""
        if self.mode == 'single':
            # So sánh cả hai điểm với điểm cao hiện tại
            current_high = self.high_scores['single']
            if self.left_score > current_high:
                self.high_scores['single'] = self.left_score
            elif self.right_score > current_high:
                self.high_scores['single'] = self.right_score
            # Lưu điểm cao nếu có sự thay đổi
            if self.high_scores['single'] > current_high:
                self.save_high_scores()
        else:  # mode == 'multi'
            if self.left_score > self.high_scores['multi']:
                self.high_scores['multi'] = self.left_score
                self.save_high_scores()
            if self.right_score > self.high_scores['multi']:
                self.high_scores['multi'] = self.right_score
                self.save_high_scores()

    def check_winner(self, max_score):
        """Kiểm tra người thắng cuộc."""
        if self.left_score >= max_score:
            return "Left Player Wins!"
        elif self.right_score >= max_score:
            return "Right Player Wins!"
        return None
