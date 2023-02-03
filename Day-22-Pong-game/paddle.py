"""
Paddle module
"""
from turtle import Turtle, Screen
class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape('square')
        self.color('white')
        # self.setheading(to_angle=90)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=pos[0], y=pos[1])
        self.screen = Screen()
        self.screen.update()
    def up(self):
        """Moves the paddle upwards"""
        # self.forward(20)
        x = self.xcor()
        y = self.ycor() + 20
        self.goto(x, y)
        # self.screen.update()

    def down(self):
        """Moves the paddle downward"""
        x = self.xcor()
        y = self.ycor() - 20
        self.goto(x, y)
        # self.backward(20)
        # self.screen.update()
