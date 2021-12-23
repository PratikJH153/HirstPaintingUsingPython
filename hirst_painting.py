import colorgram
from turtle import Turtle, Screen
import random


# def grab_colors_from_image():
#     rgb = []
#     colors = colorgram.extract("hirst.jpg", 50)
#     for color in colors:
#         r = color.rgb.r
#         g = color.rgb.g
#         b = color.rgb.b
#
#         rgb.append((r, g, b))
#
#     return rgb


colors = [(246, 245, 243), (233, 239, 246), (246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106),
          (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66),
          (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71),
          (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159),
          (175, 200, 188), (34, 151, 210), (65, 66, 56), (106, 140, 124), (153, 202, 227), (48, 69, 71), (131, 128, 121)]

tim = Turtle()
tim.speed("fastest")

x = -200
y = -200

tim.hideturtle()

tim.penup()
tim.setposition(x, y)

screen = Screen()
screen.colormode(255)

for i in range(10):
    for j in range(10):
        tim.dot(20, random.choice(colors))
        tim.forward(50)

    y += 50
    tim.setposition(x, y)


screen.exitonclick()
