import pygame
from classes.paddle import Paddle
from classes.ball import Ball
from classes.score import Score


class Menu:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font_title = pygame.font.SysFont("Times New Roman", 100)
        self.font_option = pygame.font.SysFont("Times New Roman", 43)
        self.options = ["1 Player", "2 Players", "Hướng dẫn"]
        self.selected_option = None

    def draw(self, screen):
        screen.fill((176, 176, 178))
        shadow = self.font_title.render("Select Mode", True, (50, 50, 50))
        screen.blit(shadow, (self.screen_width // 2 - shadow.get_width() // 2 + 5, 85))
        title = self.font_title.render("Select Mode", True, (173, 216, 240))  # Màu xanh dương nhạt
        screen.blit(title, (self.screen_width // 2 - title.get_width() // 2, 80))

        # Vẽ các nút với màu xanh dương
        for index, option in enumerate(self.options):
            button_rect = pygame.Rect(self.screen_width // 2 - 100, 250 + index * 100, 200, 60)
            color = (0, 128, 255) if option != self.selected_option else (0, 102, 204)
            pygame.draw.rect(screen, color, button_rect, border_radius=10)
            pygame.draw.rect(screen, (255, 255, 255), button_rect, 3, border_radius=10)

            text = self.font_option.render(option, True, (255, 255, 255))
            screen.blit(text, (button_rect.centerx - text.get_width() // 2, button_rect.centery - text.get_height() // 2))

    def get_selected_option(self, mouse_pos):
        for index, option in enumerate(self.options):
            button_rect = pygame.Rect(self.screen_width // 2 - 100, 250 + index * 100, 200, 60)
            if button_rect.collidepoint(mouse_pos):
                self.selected_option = option
                return option
        self.selected_option = None
        return None


def display_instructions(screen):
    font = pygame.font.Font("Arimo-Italic-VariableFont_wght.ttf", 25)
    instructions_text = [
        "1. Điều khiển thanh chắn (Paddle) để đánh bóng qua lại.",
        "2. Người chơi 1 sử dụng phím W (lên) và S (xuống).",
        "3. Người chơi 2 sử dụng phím mũi tên lên và xuống.",
        "4. Mục tiêu là ngăn bóng không rơi ra ngoài phía sân của bạn.",
        "5. Trò chơi kết thúc khi một bên đạt điểm tối đa.",
        "6. Nhấn phím ESC để tạm dừng hoặc thoát trò chơi."
    ]

    screen.fill((255, 255, 255))  # Màu nền trắng
    title = font.render("Hướng dẫn chơi", True, (0, 0, 0))
    screen.blit(title, (screen.get_width() // 2 - title.get_width() // 2, 50))

    for i, line in enumerate(instructions_text):
        text = font.render(line, True, (0, 0, 0))
        screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2, 150 + i * 50))

    pygame.display.flip()

    # Đợi người dùng bấm chuột để quay lại menu
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False

def main_menu(screen):
    menu = Menu(*screen.get_size())
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill((0, 0, 0))  # Màu nền menu
        menu.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                selected = menu.get_selected_option(pygame.mouse.get_pos())
                if selected:
                    if selected == "1 Player":
                        return 1
                    elif selected == "2 Players":
                        return 2
                    elif selected == "Hướng dẫn":
                        display_instructions(screen)
                        break  # Quay lại menu sau khi xem hướng dẫn

        pygame.display.flip()
        clock.tick(60)


class PauseMenu:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = pygame.font.Font(None, 74)
        self.options = ["Continue", "Exit"]
        self.selected_option = None

    def draw(self, screen):
        overlay = pygame.Surface((self.screen_width, self.screen_height))
        overlay.set_alpha(128)  # Độ trong suốt (128/255 là khoảng 50%)
        overlay.fill((0, 0, 0))  # Đổ màu đen
        screen.blit(overlay, (0, 0))

        title = self.font.render("Paused", True, (255, 255, 255))
        screen.blit(title, (self.screen_width // 2 - title.get_width() // 2, 100))

        for index, option in enumerate(self.options):
            text = self.font.render(option, True, (255, 255, 255))
            screen.blit(text, (self.screen_width // 2 - text.get_width() // 2, 250 + index * 100))

    def get_selected_option(self, mouse_pos):
        for index, option in enumerate(self.options):
            text_rect = pygame.Rect(self.screen_width // 2 - 100, 250 + index * 100, 200, 80)
            if text_rect.collidepoint(mouse_pos):
                self.selected_option = option
                return option
        return None


class Game:
    def __init__(self, ai_mode=False):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Pong")
        self.clock = pygame.time.Clock()

        # Tạo paddles, bóng và điểm số
        self.paddle_left = Paddle(50, self.screen_height // 2 - 50)
        self.paddle_right = Paddle(self.screen_width - 60, self.screen_height // 2 - 50)
        self.ball = Ball(self.screen_width, self.screen_height)
        self.ai_mode = ai_mode
        self.score = Score(self.screen_width, mode='single' if ai_mode else 'multi')
        self.paused = False  # Thêm biến paused để thêm trạng thái tạm dừng
        self.countdown = 60
        self.high_scores = 0  # Điểm cao nhất
        self.font = pygame.font.Font(None, 50)  # Font để hiển thị thời gian và điểm
        self.game_over_displayed = False  # Thêm biến để kiểm tra xem đã hiển thị game over chưa

    def start(self):
        running = True
        pause_menu = PauseMenu(self.screen_width, self.screen_height)
        start_ticks = pygame.time.get_ticks()  # Lấy thời điểm bắt đầu trò chơi
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.paused = not self.paused  # Bật/tắt chế độ tạm dừng

                # Xử lý sự kiện khi đang tạm dừng
                if self.paused and event.type == pygame.MOUSEBUTTONDOWN:
                    selected = pause_menu.get_selected_option(pygame.mouse.get_pos())
                    if selected == "Continue":
                        self.paused = False  # Tiếp tục trò chơi
                    elif selected == "Exit":
                        return "exit"  # Trả về "exit" khi người chơi chọn thoát

            # Xử lý logic trò chơi nếu không bị tạm dừng
            if not self.paused:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                    self.paddle_left.move_up()
                if keys[pygame.K_s]:
                    self.paddle_left.move_down()

                if self.ai_mode:
                    self.ai_move()
                else:
                    if keys[pygame.K_UP]:
                        self.paddle_right.move_up()
                    if keys[pygame.K_DOWN]:
                        self.paddle_right.move_down()

                self.paddle_left.keep_within_bounds(self.screen_height)
                self.paddle_right.keep_within_bounds(self.screen_height)
                self.ball.move()
                self.ball.bounce(self.screen_height)

                # Kiểm tra va chạm với paddle trước khi kiểm tra ra ngoài màn hình
                # Kiểm tra va chạm với paddle trái
                if self.ball.x - self.ball.radius < self.paddle_left.x + self.paddle_left.width and \
                        self.paddle_left.y < self.ball.y < self.paddle_left.y + self.paddle_left.height:
                    self.ball.x = self.paddle_left.x + self.paddle_left.width + self.ball.radius  # Đặt lại vị trí bóng
                    self.ball.dx *= -1  # Đảo hướng bóng

                # Kiểm tra va chạm với paddle phải
                if self.ball.x + self.ball.radius > self.paddle_right.x and \
                        self.paddle_right.y < self.ball.y < self.paddle_right.y + self.paddle_right.height:
                    self.ball.x = self.paddle_right.x - self.ball.radius  # Đặt lại vị trí bóng
                    self.ball.dx *= -1  # Đảo hướng bóng

                # Kiểm tra nếu bóng đã ra khỏi giới hạn màn hình và ghi điểm
                if self.ball.x - self.ball.radius < 0:  # Bóng ra ngoài bên trái
                    self.ball.reset(self.screen_width, self.screen_height)
                    self.score.right_point()  # Ghi điểm cho AI
                elif self.ball.x + self.ball.radius > self.screen_width:  # Bóng ra ngoài bên phải
                    self.ball.reset(self.screen_width, self.screen_height)
                    self.score.left_point()  # Ghi điểm cho người chơi

            # Cập nhật thời gian và kiểm tra hết giờ
            if not self.paused:
                seconds = (pygame.time.get_ticks() - start_ticks) / 1000
                self.countdown = max(0, 60 - int(seconds))

                if self.countdown <= 0 and not self.game_over_displayed:
                    self.high_scores = max(self.high_scores, self.score.load_high_scores() or 0)
                    self.game_over()
                    return
            if self.countdown <= 0 and not self.game_over_displayed:
                self.high_scores = max(self.high_scores, self.score.load_high_scores())
                self.display_winner()
                return
            # Vẽ trò chơi hoặc menu tạm dừng
            self.screen.fill((255, 192, 203))  # Màu nền trò chơi
            self.paddle_left.draw(self.screen)
            self.paddle_right.draw(self.screen)
            self.ball.draw(self.screen)
            self.score.update(self.screen)

            time_text = self.font.render(f"Time: {self.countdown}", True, (255, 255, 255))
            self.screen.blit(time_text, (10, 10))  # Vẽ ở góc trên bên trái

            if self.paused:
                pause_menu.draw(self.screen)  # Vẽ menu tạm dừng

            if self.game_over_displayed:
                running = False  # Thoát vòng lặp trò chơi

            pygame.display.flip()
            self.clock.tick(60)

    def ai_move(self):
        # Kiểm tra xem bóng có gần paddle phải hay không
        if self.ball.x > self.screen_width // 2:  # Chỉ di chuyển nếu bóng ở nửa màn hình bên phải
            # Dự đoán vị trí bóng sẽ đến
            future_y = self.ball.y + (self.ball.dy / abs(self.ball.dx)) * (self.paddle_right.x - self.ball.x)
            # Nếu vị trí dự đoán lớn hơn paddle, di chuyển xuống
            if future_y > self.paddle_right.y + self.paddle_right.height // 2:
                self.paddle_right.move_down()
            # Nếu vị trí dự đoán nhỏ hơn paddle, di chuyển lên
            elif future_y < self.paddle_right.y + self.paddle_right.height // 2:
                self.paddle_right.move_up()

    def display_winner(self):
        winner = "Player 1 Wins!" if self.score.left_score > self.score.right_score else "Player 2 Wins!"
        font = pygame.font.Font(None, 74)
        text = font.render(winner, True, (255, 255, 255))
        self.screen.blit(text, (
            self.screen_width // 2 - text.get_width() // 2,
            self.screen_height // 2 - text.get_height() // 2
        ))
        pygame.display.flip()
        pygame.time.wait(3000)

    def game_over(self):
        self.screen.fill((0, 0, 0))  # Màu nền đen
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, (255, 0, 0))  # Màu chữ đỏ
        self.screen.blit(text, (
            self.screen_width // 2 - text.get_width() // 2,
            self.screen_height // 2 - text.get_height() // 2
        ))
        pygame.display.flip()
        pygame.time.wait(3000)  # Chờ 3 giây

        # Quay lại menu chính
        self.game_over_displayed = True
        main_menu(self.screen)  # Gọi lại menu chính


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    while True:
        # Hiển thị menu để chọn chế độ
        game_mode = main_menu(screen)

        # Chọn chế độ chơi
        if game_mode == 1:
            game = Game(ai_mode=True)
            result = game.start()
            if result == "exit":
                pygame.quit()
                exit()
        elif game_mode == 2:
            game = Game(ai_mode=False)
            result = game.start()
            if result == "exit":
                pygame.quit()
                exit()
