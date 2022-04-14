from turtle import Turtle
FONT = ('Courier', 58, 'normal')
ALIGNMENT = "center"


class PongScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.write_score()

    def increment_score_left(self):
        self.right_score += 1
        self.write_score()

    def increment_score_right(self):
        self.left_score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-100, 220)
        self.write(f"{self.left_score}", False, align=ALIGNMENT, font=FONT)
        self.goto(100, 220)
        self.write(f"{self.right_score}", False, align=ALIGNMENT, font=FONT)
