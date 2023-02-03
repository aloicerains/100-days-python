"""
Ball Module
"""

from turtle import Turtle, Screen
import random


INCREMENT = 5
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.speed('slowest')
        self.penup()
        self.y_incr = INCREMENT
        self.x_incr = INCREMENT
        self.roll_speed = 0.08

    def move(self):
        """Moves the ball"""

        x = self.xcor() + self.x_incr
        y = self.ycor() + self.y_incr
        self.goto(x, y)

    def bounce_y(self):
        """Bounces the ball on the y axis"""
        self.y_incr *= -1

    def bounce_x(self):
        """Bounces back the """
        self.x_incr *= -1
        self.roll_speed *= 0.8

    def reset_position(self):
        self.home()
        self.roll_speed = 0.08

