from turtle import Turtle
FONT = ('Courier', 14, 'normal')
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_highscore()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write_score()

    def get_high_score(self):
        with open("data.txt") as file:
            data = file.read()
            if len(data) > 0:
                return int(data)
            else:
                return 0

    def set_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def increment_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_highscore()
        self.score = 0
        self.write_score()
