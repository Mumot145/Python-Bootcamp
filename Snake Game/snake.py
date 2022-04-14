from turtle import Turtle
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.snake_head = self.snake_segments[0]

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def add_segment(self, position):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.snake_segments.append(segment)

    def move_forward(self):
        for segment_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment_num - 1].xcor()
            new_y = self.snake_segments[segment_num - 1].ycor()
            self.snake_segments[segment_num].goto(new_x, new_y)
        self.snake_head.forward(20)

    def reset(self):
        for segment in self.snake_segments:
            segment.hideturtle()

        self.snake_segments.clear()
        self.create_snake()
        self.snake_head = self.snake_segments[0]

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
