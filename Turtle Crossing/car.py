from turtle import Turtle


class Car(Turtle):
    def __init__(self, color, y_cor):
        super().__init__()
        self.penup()
        self.setpos(300, y_cor)
        self.color(color)
        self.shape("square")
        self.shapesize(stretch_len=3, stretch_wid=1)

    def move(self, speed):
        self.setpos(self.xcor() - speed, self.ycor())

    def collision_check(self, player_position):
        if self.position is not None:
            return self.distance(player_position) < 15
        return False
