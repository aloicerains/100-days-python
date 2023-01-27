# The program uses the turtle module to create an etc-a-sketch app
# W - moves forward
# S - moves backwards
# A - moves counterclockwise
# D - moves clockwise
# C - clears the screen

from turtle import Turtle
from turtle import Screen

tim = Turtle()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_clockwise():
    tim.circle(-70, 90)

def move_counter_clockwise():
    tim.circle(70, 90)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def turn_left():
    tim.left(90)


def turn_right():
    tim.right(90)
# create screen
screen = Screen()
screen.listen()
screen.onkey(move_forward, "W")
screen.onkey(move_backward, "S")
screen.onkey(move_clockwise, "D")
screen.onkey(move_counter_clockwise, "A")
screen.onkey(clear_screen, "C")
screen.onkey(turn_right, "R")
screen.onkey(turn_left, "L")

screen.exitonclick()
