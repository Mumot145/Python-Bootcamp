# Pong notes
# classes: paddle, ball, scoreboard

# create screen - DONE
# create and move paddle
# create another paddle
# create the ball and make it move
# detect collision with wall and bounce
# detect collision with paddle
# detect when paddle misses
# keep score
import random
from turtle import Screen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import PongScoreBoard

game_is_on = True

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

scoreboard = PongScoreBoard()

max_y = screen.window_height() / 2 - 20
min_y = -(screen.window_height() / 2 - 20)

max_x = screen.window_width() / 2 - 20
min_x = -(screen.window_width() / 2 - 20)

l_paddle = Paddle((-350, 0))
screen.onkeypress(l_paddle.move_up, "Up")
screen.onkeypress(l_paddle.move_down, "Down")

r_paddle = Paddle((350, 0))
screen.onkeypress(r_paddle.move_up, "w")
screen.onkeypress(r_paddle.move_down, "s")

random_direction = [10, 5, -5, -10]
ball = Ball(random.choice(random_direction), random.choice(random_direction))

while game_is_on:
    time.sleep(0.03)
    ball.move()
    if ball.ycor() >= max_y or ball.ycor() <= min_y:
        ball.bounce_y()

    if ball.xcor() >= max_x:
        ball.reset_ball(random.choice(random_direction), random.choice(random_direction))
        scoreboard.increment_score_right()
    elif ball.xcor() <= min_x:
        ball.reset_ball(random.choice(random_direction), random.choice(random_direction))
        scoreboard.increment_score_left()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    screen.update()

screen.exitonclick()
