
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):  # You could also approach it by avoiding inheritance and creating
    # the turtle instance in CarManager

    move_distance = STARTING_MOVE_DISTANCE

    def __init__(self):
        super().__init__()
        self.create_turtle()

    def create_turtle(self):
        """Generates random turtle"""
        self.color(random.choice(COLORS))
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        x = -280
        y = random.randint(-250, 250)
        self.goto(x, y)

        # self.forward(STARTING_MOVE_DISTANCE)

    def move(self):
        """Moves the turtle forward"""
        self.forward(CarManager.move_distance)

    @classmethod
    def move_faster(cls):
        """Increases the speed of the turtle"""
        cls.move_distance += MOVE_INCREMENT

