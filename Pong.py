import pygame
from classes.paddle import Paddle
from classes.ball import Ball
from classes.score import Score


class Menu:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.font = pygame.font.Font(None, 74)
        self.options = ["1 Player", "2 Players"]
        self.selected_option = None

    def draw(self, screen):
        screen.fill((0, 0, 0))  # Màu nền đen
        title = self.font.render("Select Mode", True, (255, 255, 255))
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


def main_menu(screen):
    menu = Menu(screen.get_width(), screen.get_height())
    running = True

    while running:
        screen.fill((0, 0, 0))
        menu.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected = menu.get_selected_option(pygame.mouse.get_pos())
                if selected:
                    if selected == "1 Player":
                        return 1
                    elif selected == "2 Players":
                        return 2

        pygame.display.flip()
        pygame.time.Clock().tick(60)


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

    def start(self):
        running = True
        pause_menu = PauseMenu(self.screen_width, self.screen_height)

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

            # Vẽ trò chơi hoặc menu tạm dừng
            self.screen.fill((255, 192, 203))  # Màu nền trò chơi
            self.paddle_left.draw(self.screen)
            self.paddle_right.draw(self.screen)
            self.ball.draw(self.screen)
            self.score.update(self.screen)

            if self.paused:
                pause_menu.draw(self.screen)  # Vẽ menu tạm dừng

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


# Chạy trò chơi với giao diện chọn chế độ
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    while True:
        # Hiển thị menu để chọn chế độ
        game_mode = main_menu(screen)

        # Chọn chế độ chơi
        if game_mode == 1:
            game = Game(ai_mode=True)
        elif game_mode == 2:
            game = Game(ai_mode=False)

        # Bắt đầu trò chơi và kiểm tra xem có chọn "Exit" không
        result = game.start()
        if result == "exit":
            continue
