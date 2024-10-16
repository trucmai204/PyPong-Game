import pygame
from classes.paddle import Paddle
from classes.ball import Ball
from classes.score import Score
from classes.timer import Timer

class Game:
    def __init__(self):
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
        self.score = Score(self.screen_width)
        self.timer = Timer(self.screen_width, self.screen_height)

        self.game_over = False  # Biến theo dõi trạng thái trò chơi

    def start(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if not self.game_over:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                    self.paddle_left.move_up()
                if keys[pygame.K_s]:
                    self.paddle_left.move_down()
                if keys[pygame.K_UP]:
                    self.paddle_right.move_up()
                if keys[pygame.K_DOWN]:
                    self.paddle_right.move_down()

                self.paddle_left.keep_within_bounds(self.screen_height)
                self.paddle_right.keep_within_bounds(self.screen_height)

                self.ball.move()
                self.ball.bounce(self.screen_height)

                # Kiểm tra va chạm với paddle
                if self.ball.x - self.ball.radius < self.paddle_left.x + self.paddle_left.width and \
                   self.paddle_left.y < self.ball.y < self.paddle_left.y + self.paddle_left.height:
                    self.ball.dx *= -1

                if self.ball.x + self.ball.radius > self.paddle_right.x and \
                   self.paddle_right.y < self.ball.y < self.paddle_right.y + self.paddle_right.height:
                    self.ball.dx *= -1

                # Kiểm tra nếu bóng vượt qua màn hình
                if self.ball.x - self.ball.radius < 0:
                    self.ball.reset(self.screen_width, self.screen_height)
                    self.score.right_point()

                if self.ball.x + self.ball.radius > self.screen_width:
                    self.ball.reset(self.screen_width, self.screen_height)
                    self.score.left_point()

                # Cập nhật màn hình
                self.screen.fill((255, 192, 203))
                self.paddle_left.draw(self.screen)
                self.paddle_right.draw(self.screen)
                self.ball.draw(self.screen)
                self.score.update(self.screen)
                self.timer.update(self.screen)

                # Kiểm tra nếu hết thời gian
                if self.timer.time_left <= 0:
                    self.game_over = True  # Đánh dấu trò chơi kết thúc

            else:
                self.show_game_over()  # Hiển thị thông báo "Hết giờ!"

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def show_game_over(self):
        # Vẽ thông báo "Hết giờ!" khi trò chơi kết thúc
        self.screen.fill((255, 192, 203))  # Đổ màu nền
        self.timer.draw_game_over(self.screen)  # Vẽ thông báo
        pygame.display.flip()  # Cập nhật màn hình

# Khởi tạo và bắt đầu trò chơi
if __name__ == "__main__":
    game = Game()
    game.start()
