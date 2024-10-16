import turtle
from turtle import Turtle

class ScoreBoard:
    def __init__(self):
        with open("score.txt") as file:
            self.highscore = int(file.read())
        self.score = 0
        self.scoreboard = Turtle()
        self.direction = Turtle()
        self.scoreboard.penup()
        self.direction.penup()
        self.scoreboard.ht()
        self.direction.ht()
        self.scoreboard.goto(x=0,y=turtle.window_height()/2-25)
        self.direction.goto(x=-(turtle.window_width()/2-25),y=turtle.window_height()/2-25)
        self.scoreboard.write(f"Score: {self.score} High Score: {self.highscore}", align="center",font=("Lexend",15,"normal"))

    def increment_score(self):
        """Increment score once snake collide with food"""
        self.score+=1
        self.scoreboard.clear()
        self.scoreboard.write(f"Score: {self.score} High Score: {self.highscore}", align="center",font=("Lexend",15,"normal"))

    def update_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("score.txt","w") as file:
                file.write(f"{self.highscore}")

    def game_over(self):
        self.scoreboard.goto(0,0)
        self.scoreboard.write(f"Game Over", align="center", font=("Lexend", 25, "normal"))

    def update_direction(self,direction):
        self.direction.clear()
        self.direction.write(f"Direction: {direction} ",font=("Lexend",15,"normal"))