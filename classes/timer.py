from turtle import Turtle, Screen 

'''Định nghĩa display ở phạm vi toàn cục'''
display = Screen()
class Timer(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.seconds = 59
        self.update_timer()

    def update_timer(self):
        self.clear()
        self.goto(0, 250)
        minutes = self.seconds // 60
        seconds = self.seconds % 60
        self.write(f"{minutes:02d}:{seconds:02d}", align="center", font=("Courier", 30, "normal"))

    def countdown(self):
        if self.seconds > 0:
            self.seconds -= 1
            self.update_timer()
            display.ontimer(self.countdown, 1000)
        else:
            self.time_up()

    def time_up(self):
        self.goto(0, 0)
        self.write("Hết giờ!", align="center", font=("Courier", 40, "bold"))
