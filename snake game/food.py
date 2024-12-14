import random as rd
import turtle as t
class Food:
    def __init__(self):
        self.food = t.Turtle(shape="circle")
        self.food.color("blue")
        self.food.penup()
        self.food.shapesize(stretch_len=0.6,stretch_wid=0.6,outline=1)
        self.set_position()
    def set_position(self):
        x = rd.randint(-int(t.window_width()/2-20),int(t.window_width()/2-20))
        y = rd.randint(-int(t.window_height()/2-20),int(t.window_height()/2-20))
        self.food.goto(x,y)