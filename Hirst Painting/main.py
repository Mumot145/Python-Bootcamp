from turtle import Turtle, Screen
from random import Random
import colorgram

rgb_colors = []

rand = Random()
colors = colorgram.extract('20_001.jpg', 25)

turtle = Turtle()
turtle.pensize(8)
turtle.penup()

screen = Screen()
screen.colormode(255)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),
              (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174),
              (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42),
              (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203)]

start_x = -250
start_y = -250

for column in range(10):
    turtle.setposition(start_x, start_y)
    start_x = -250
    start_y += 50
    for row in range(10):
        color = rand.choice(color_list)
        turtle.pencolor(color)
        turtle.pendown()
        turtle.dot(20)
        print(turtle.position())
        turtle.penup()
        turtle.forward(50)

screen.exitonclick()
