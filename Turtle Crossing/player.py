from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.set_starting_position()
        self.color("black")
        self.setheading(UP)
        self.shape("turtle")

    def move(self):
        self.setpos(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def is_crossed_finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False

    def set_starting_position(self):
        self.setpos(STARTING_POSITION)
