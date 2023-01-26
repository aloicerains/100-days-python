# using the turtle library
import turtle as t
from turtle import Turtle
from turtle import Screen
import random

tim = Turtle()
tim.shape('turtle')
t.colormode(255)
tim.speed('fastest')
# tim.hideturtle()
# # tim.color('brown')

# colors = ['red', 'green', 'orange', 'brown', 'magenta', 'blue', 'black', 'purple']
# Turtle challenge 1 - Drawing a square
# def draw_square():
#     for _ in range(4):
#         tim.forward(100)
#         tim.right(90)

# 2 Drawing a dashed line
# def draw_dashed_line():
#     for _ in range(10):
#         tim.pendown()
#         tim.forward(10)
#         tim.penup()
#         tim.forward(10)

# challenge 3
# Drawing a set of 8 triangles with sides from 3 to 10
# def draw_triangles():
#     sides = [3, 4, 5, 6, 7, 8, 9, 10]
#     for side, col in zip(sides, colors):
#         angle = round(360/side, 2)
#         tim.pencolor(col)
#         for _ in range(side):
#             tim.forward(100)
#             tim.right(angle)

# challenge 4: Random Walk
# The turtle should make a random walk and each walk should have different color

# Creating a random color
# def random_color():
#     # Tuple comprehension will result to a generator
#     return tuple(random.randint(0, 255) for _ in range(3))


# def random_walk():
#     direction = [0, 90, 180, 270]
#     tim.speed(1)
#     for _ in range(100):
#         tim.color(random_color())
#         tim.pensize(3)
#         tim.forward(20)
#         tim.setheading(random.choice(direction))
#
# def draw_spiral(loops):
#     """
#     Draws the spirals of given loops
#     :param loops:
#     :return: None
#     """
#     angle = round(360/loops, 2)
#     for _ in range(loops):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.left(angle)

#random_walk()
# displaying on the screen
# draw_spiral(60)

# Main project


from color_gram_extract import *

colors = rgb_colors[3:]


def get_color():
    """
    Pick a random color from the list
    :return: col(str)
    """
    return random.choice(colors)


# Draw circle


def draw_circle():
    """
    Draws circle of radius 10
    :return:
    """
    tim.color(get_color())
    tim.begin_fill()
    tim.circle(10)
    tim.end_fill()


def shift_to_new_row():
    """
    Makes tim jump to a new row
    :return: None
    """
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.right(180)


tim.penup()
tim.setx(-245)
tim.sety(-215)
for _ in range(10):
    for _ in range(10):
        # tim.pendown() no need for pendown if using dots otherwise handy with draw_circle method
        # draw_circle() you can also use dot instead of the method
        tim.dot(20, get_color())
        tim.penup()
        tim.forward(50)
    shift_to_new_row()


screen = Screen()
screen.exitonclick()
