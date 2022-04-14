# 1) create turtle, move him forward with up key
# 2) create car, move it left at a speed
# 3) spawn cars randomly in defined area starting at right
# 4) detect collision of car with turtle
# 5) detect crossing of finish line
# 6) scoreboard tracking of level, game over

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

car_manager = CarManager(260, -260)
scoreboard = Scoreboard()
player = Player()

screen.onkeypress(player.move, "Up")

game_is_on = True

while game_is_on:
    car_manager.spawn_car()
    car_manager.move_cars()
    for car in car_manager.CARS:
        if car.distance(player.pos()) < 20:
            game_is_on = False
            scoreboard.game_over()
        if car.xcor() < -300:
            car_manager.remove_car(car)

    if player.is_crossed_finish():
        scoreboard.level_up()
        car_manager.level += 1
        player.set_starting_position()

    time.sleep(0.1)
    screen.update()

screen.exitonclick()
