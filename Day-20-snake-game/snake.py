"""
Snake Module
"""
from turtle import Turtle

MOVE_DISTANCE = 20
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0

class Snake:
    # Create the snake body
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates a new snake object"""
        for pos in START_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, pos):
        """Adds snake segment"""
        segment = Turtle(shape="square")
        segment.color('white')
        segment.penup()
        segment.setposition(pos)
        self.segments.append(segment)

    def extend(self):
        """Extends the snake as soon as it eats some food"""
        self.add_segment(self.segments[-1].position())

    # Move the snake
    def move(self):
        for part_pos in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[part_pos - 1].xcor()
            new_y = self.segments[part_pos - 1].ycor()
            self.segments[part_pos].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        """Moves the snake upward"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Moves the snake downward"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Moves the snake leftwards"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Moves the snake rightward"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
