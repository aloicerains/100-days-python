from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = 'left'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(-100, 270)
        self.level = 0

    def writer(self):
        """Writes level"""
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def increase(self):
        """Increases the level"""
        self.clear()
        self.level += 1

    def game_over(self):
        self.goto(-100, 0)
        self.write('GAME OVER!', align=ALIGN, font=FONT)