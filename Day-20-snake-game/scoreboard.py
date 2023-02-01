"""
Scoreboard Module
"""
from turtle import Turtle

ALIGNMENT = "left"
FONT = ('Courier', 12, 'bold')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.goto(0, 280)
        self.score = 0

    def update_score(self):
        self.clear()
        self.score += 1

    def write_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
