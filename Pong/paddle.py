from turtle import Turtle
DOWN = 270
UP = 90


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.setposition(position)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        #

    def move_up(self):
        # move up
        y_cor = self.ycor() + 20
        self.goto(self.xcor(), y_cor)

    def move_down(self):
        # move up
        y_cor = self.ycor() - 20
        self.goto(self.xcor(), y_cor)
