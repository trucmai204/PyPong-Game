import pygame

class Timer:
    def __init__(self, screen_width, screen_height):
        self.time_left = 59  # Đếm ngược từ 59 giây
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.last_update = pygame.time.get_ticks()  # Đánh dấu thời gian cập nhật cuối cùng

    def update(self, screen):
        current_time = pygame.time.get_ticks()  # Lấy thời gian hiện tại
        if current_time - self.last_update >= 1000:  # Cập nhật mỗi giây
            self.time_left -= 1
            self.last_update = current_time

        # Nếu thời gian hết
        if self.time_left < 0:
            self.time_left = 0

        # Hiển thị thời gian lên màn hình
        font = pygame.font.Font(None, 74)
        timer_text = f"00:{self.time_left:02d}"  # Định dạng hiển thị như 00:59
        text_surface = font.render(timer_text, True, (0, 0, 0))
        screen.blit(text_surface, (self.screen_width // 2 - 50, 10))  # Vị trí giữa màn hình, phía trên

    def draw_game_over(self, screen):
        font = pygame.font.Font(None, 74)  # Font chữ cho thông báo
        game_over_text = font.render("Hết giờ!", True, (0, 0, 0))  # Màu chữ đỏ
        text_rect = game_over_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2))  # Vị trí giữa màn hình
        screen.blit(game_over_text, text_rect)  # Vẽ thông báo lên màn hình
