from turtle import Turtle, Screen
from draw_handler import DrawHandler


drawing = DrawHandler()
screen = Screen()
screen.colormode(255)

# drawing.draw_rectangle(100, 100)
# drawing.draw_dashed_line(10, 5)
# drawing.draw_even_sided_shapes(100, 10)
# drawing.draw_random_walk(250, 25)
drawing.draw_spirograph(100, 5)

screen.exitonclick()
