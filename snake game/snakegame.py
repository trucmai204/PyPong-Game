# #
# breaking down of problem
# 1. snake body
# 2. food location
# 3. increase size when food is eaten
# 4. check if snake is out of range or does it bite itself
# #
from operator import truediv
from turtle import Screen
import  time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

sleep_time = 0.17

screen = Screen()
screen.setup(width=800,height=600)
screen.tracer(0)
screen.bgcolor("SeaGreen1")
screen.title("Snake Game")
screen.listen()


snake = Snake(3)
food = Food()
scoreboard = ScoreBoard()


screen.onkey(key="Right",fun=snake.move_right)
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)
screen.onkey(key="Left", fun=snake.move_left)

game_over = False
while not game_over:    #run while game is not over
    screen.update()
    time.sleep(sleep_time)
    snake.move()
    scoreboard.update_direction(snake.head.pos())

    #Detecting collision
    if snake.head.distance(food.food) <15:
        '''checks the distance of snake from food'''
        snake.add_segments()
        food.set_position()
        scoreboard.increment_score()

    #Detect collision with wall
    if abs(snake.head.xcor()) >= screen.window_width() / 2 or abs(snake.head.ycor()) >= screen.window_height() / 2:
        game_over = True
        scoreboard.update_score()
        scoreboard.game_over()
        snake.reset_game()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_over=True
            scoreboard.update_score()
            scoreboard.game_over()
            snake.reset_game()

screen.exitonclick()