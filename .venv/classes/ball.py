from turtle import Turtle
import random
from utils.constant import LIMIT_TOP, LIMIT_BOTTOM

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.dx = random.choice([-1, 1]) * random.randint(1, 3)
        self.dy = random.choice([-1, 1]) * random.randint(1, 3)
        self.ball_speed = 0.03

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)
        if self.ycor() > LIMIT_TOP or self.ycor() < LIMIT_BOTTOM:
            self.dy *= -1

    def ball_touch_wall(self):
        self.dy *= -1

    def ball_touch_thanh_truot(self):
        self.dx *= -1
        self.ball_speed *= 0.9

    def reset_Ball(self):
        self.goto(0, 0)
        self.dx *= -1
