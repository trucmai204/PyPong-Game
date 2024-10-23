from turtle import Turtle

start_pos = 0
class Snake:
    def __init__(self,no_of_segments):
        self.start_pos = 0
        self.segments = []
        self.no_of_segments = no_of_segments
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for _ in range(self.no_of_segments):
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.goto(self.start_pos,0)
            self.segments.append(new_segment)
            self.start_pos-=20

    def reset_game(self):
        for segs in self.segments:
            segs.goto(1000,1000)
        self.segments.clear()
        self.start_pos=0
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        """Moves the snake forward"""
        for j in range(len(self.segments) - 1, 0, -1):
            x = self.segments[j - 1].xcor()
            y = self.segments[j - 1].ycor()
            self.segments[j].goto(x, y)
        self.head.fd(20)

    def add_segments(self):
        """Increase the length of snake on colliding with food"""
        new_segment = Turtle(shape="square")
        new_segment.penup()
        x = self.segments[-1].xcor()
        y = self.segments[-1].ycor()
        new_segment.goto(x,y)
        self.segments.append(new_segment)

    def move_right(self):
        """Moves the snake to right"""
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move_up(self):
        """Moves snake to up"""
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        """Moves snake to down"""
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_left(self):
        """Moves snake to left"""
        if self.head.heading() != 0:
            self.head.setheading(180)