import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

game_is_on = True

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

food = Food()
scoreboard = Scoreboard()

new_snake = Snake()
screen.onkey(new_snake.up, "Up")
screen.onkey(new_snake.down, "Down")
screen.onkey(new_snake.left, "Left")
screen.onkey(new_snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    new_snake.move_forward()
    if new_snake.snake_head.distance(food) < 15:
        food.refresh()
        scoreboard.increment_score()
        new_snake.extend()

    if new_snake.snake_head.xcor() > ((screen.window_width())/2) \
            or new_snake.snake_head.xcor() < -(screen.window_width() / 2):
        scoreboard.reset()
        new_snake.reset()
    elif new_snake.snake_head.ycor() > (screen.window_height()/2) \
            or new_snake.snake_head.ycor() < -(screen.window_height() / 2):
        scoreboard.reset()
        new_snake.reset()

    for segment in new_snake.snake_segments[1:]:
        if new_snake.snake_head.distance(segment) < 10:
            scoreboard.reset()
            new_snake.reset()

screen.exitonclick()
