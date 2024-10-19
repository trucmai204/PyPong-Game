from turtle import Turtle
from utils.constant import LIMIT_TOP, LIMIT_BOTTOM

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor() < LIMIT_TOP:
            y = self.ycor() + 20
            self.goto(self.xcor(), y)

    def go_down(self):
        if self.ycor() > LIMIT_BOTTOM:
            y = self.ycor() - 20
            self.goto(self.xcor(), y)
