from turtle import Turtle, Screen

tim = Turtle()

tim.shape("classic")
tim.color("black")


screen = Screen()
screen.colormode(255)

# Drawn a Square

# for _ in range(4):
#     tim.right(90)
#     tim.forward(100)


# Drawn a Dashed Line

# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# Drawn different Shapes

# colors = ["misty rose", "medium violet red", "spring green", "pale violet red",
#           "light sky blue", "orange", "firebrick", "dark cyan"]
#
# for i in range(3, 11):
#     angle = 360 / i
#     tim.color(colors[i - 3])
#     for j in range(i):
#         tim.forward(100)
#         tim.right(angle)


# Drawn Random Walk

# import random
#
#
# def random_color() -> tuple:
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#
#     return r, g, b
#
#
# colors = ["misty rose", "medium violet red", "spring green", "pale violet red",
#           "light sky blue", "orange", "firebrick", "dark cyan"]
#
# directions = [0, 90, 180, 270]
#
# tim.speed("fast")
# tim.pensize(15)
#
# for _ in range(1000):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


# Drawn Spirograph

import random


def random_color() -> tuple:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


tim.speed("fastest")

for i in range(int(360 / 5)):
    tim.color(random_color())
    tim.circle(100)
    tim.right(5)


screen.exitonclick()
