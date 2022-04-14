from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.display_level()

    def display_level(self):
        self.setpos(-250, 250)
        self.write(f"Level: {self.level}", font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.display_level()

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"GAME OVER", font=FONT, align="center")
