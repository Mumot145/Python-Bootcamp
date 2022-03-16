from turtle import Turtle
from random import Random


class DrawHandler:
    def __init__(self):
        self.random_number = Random()
        self.arrow = Turtle()

    def draw_rectangle(self, x_size=10, y_size=5):
        self.arrow.pensize(8)
        self.arrow.speed(3)
        if x_size == y_size:
            for _ in range(4):
                self.arrow.forward(x_size)
                self.arrow.right(90)
        else:
            for _ in range(2):
                self.arrow.forward(x_size)
                self.arrow.right(90)
                self.arrow.forward(y_size)
                self.arrow.right(90)

    def draw_dashed_line(self, distance, dash_size):
        self.arrow.pensize(8)
        self.arrow.speed(3)
        for _ in range(distance):
            self.arrow.forward(dash_size)
            self.arrow.penup()
            self.arrow.forward(dash_size)
            self.arrow.pendown()

    def draw_even_sided_shapes(self, side_size, max_shapes):
        self.arrow.pensize(8)
        self.arrow.speed(3)
        for sides in range(3, max_shapes):
            tup_color = (self.random_number.randint(0, 255), self.random_number.randint(0, 255),
                         self.random_number.randint(0, 255))
            self.arrow.pencolor(tup_color)
            angle = 360 / sides
            for side in range(sides):
                self.arrow.forward(side_size)
                self.arrow.right(angle)

    def draw_random_walk(self, total_lengths, length_size):
        available_angles = [0, 90, 180, 270]
        self.arrow.pensize(8)
        self.arrow.speed(10)
        for length in range(total_lengths):
            self.arrow.pencolor(self.random_color())
            self.arrow.forward(length_size)
            self.arrow.right(self.random_number.choice(available_angles))

    def draw_spirograph(self, circle_size, circle_frequency):
        self.arrow.pensize(2)
        self.arrow.speed("fastest")
        for i in range(int(360/circle_frequency)):
            self.arrow.pencolor(self.random_color())
            self.arrow.setheading(i * circle_frequency)
            self.arrow.circle(circle_size)

    def random_color(self):
        return (self.random_number.randint(0, 255), self.random_number.randint(0, 255),
                self.random_number.randint(0, 255))
