# Creating a turtle that starts at the bottom of the screen and listen for "Up keystrokes"
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('red')
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        """Moves the turtle forward"""
        self.forward(MOVE_DISTANCE)

    def restart(self):
        self.goto(STARTING_POSITION)

    def finish(self):
        """Detect if player has reached finish line"""
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False
