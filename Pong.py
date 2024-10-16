import pygame
from classes.paddle import Paddle
from classes.ball import Ball
from classes.score import Score_Of_Player
from utils.key_handler import key_down, key_up, keys_pressed
from classes.timer import Timer 
import time

# Thiết lập màn hình
display = Screen()
display.setup(width=800, height=600)
display.bgcolor("pink")
display.title("Pong")
display.tracer(0)

# Khởi tạo các đối tượng
paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()
score = Score_Of_Player()
timer = Timer()
'''Bắt đầu đếm ngược'''
timer.countdown()

# Lắng nghe sự kiện bàn phím
display.listen()
display.onkeypress(lambda: key_down("Up"), "Up")
display.onkeyrelease(lambda: key_up("Up"), "Up")
display.onkeypress(lambda: key_down("Down"), "Down")
display.onkeyrelease(lambda: key_up("Down"), "Down")
display.onkeypress(lambda: key_down("w"), "w")
display.onkeyrelease(lambda: key_up("w"), "w")
display.onkeypress(lambda: key_down("s"), "s")
display.onkeyrelease(lambda: key_up("s"), "s")


# Bắt đầu trò chơi
start_game = True
while start_game:
    time.sleep(ball.ball_speed)
    if timer.seconds == 0:
        start_game = False 

    # Kiểm tra trạng thái các phím và di chuyển thanh trượt
    if keys_pressed["Up"]:
        paddle_right.go_up()
    if keys_pressed["Down"]:
        paddle_right.go_down()
    if keys_pressed["w"]:
        paddle_left.go_up()
    if keys_pressed["s"]:
        paddle_left.go_down()

    display.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ball_touch_wall()

    # Kiểm tra va chạm với thanh trượt phải
    if ball.xcor() > 340 and ball.distance(paddle_right) < 50:
        ball.ball_touch_thanh_truot()

    # Kiểm tra va chạm với thanh trượt trái
    if ball.xcor() < -340 and ball.distance(paddle_left) < 50:
        ball.ball_touch_thanh_truot()

    # Kiểm tra nếu bóng vượt qua thanh trượt phải
    if ball.xcor() > 380:
        ball.reset_Ball()
        score.left_score()

    # Kiểm tra nếu bóng vượt qua thanh trượt trái
    if ball.xcor() < -380:
        ball.reset_Ball()
        score.right_score()

display.exitonclick()
