from turtle import Turtle


class Pen(Turtle):
    def __init__(self, coord, state):
        super().__init__()
        self.color('red')
        self.hideturtle()
        self.penup()
        self.goto(coord)
        self.write(arg=state, align='left', font=('Arial', 8, 'normal'))
