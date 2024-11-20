import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Thiết lập màn hình
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong Game with Timer")

# Màu sắc
WHITE = (255, 255, 255)

# Khởi tạo bộ đếm thời gian
timer = Timer(screen_width, screen_height)

# Vòng lặp chính của trò chơi
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Xóa màn hình với màu trắng
    screen.fill(WHITE)

    if not game_over:
        # Cập nhật và hiển thị bộ đếm thời gian
        timer.update(screen)
        if timer.time_left == 0:
            game_over = True
    else:
        # Hiển thị thông báo "Hết giờ!" khi thời gian kết thúc
        timer.draw_game_over(screen)

    # Cập nhật màn hình
    pygame.display.flip()
    pygame.time.delay(50)  # Để giảm tốc độ vòng lặp trò chơi một chút

# Thoát trò chơi
pygame.quit()
sys.exit()
