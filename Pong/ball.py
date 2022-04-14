from turtle import Turtle


class Ball(Turtle):
    def __init__(self, x_move, y_move):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.width = 20
        self.color("white")
        self.setposition(0, 0)
        self.x_move = x_move
        self.y_move = y_move

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        print(self.x_move)
        print(self.y_move)
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_ball(self, x_move, y_move):
        self.setposition(0, 0)
        self.x_move = x_move
        self.y_move = y_move
