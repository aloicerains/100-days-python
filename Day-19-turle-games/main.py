# Turtle Games Competition Project

"""
Turtle Games
"""

# Import modules
from turtle import Turtle
from turtle import Screen
import random

# turtle colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
random.shuffle(colors)


# create turtles
turtles = []
y = -100
for col in colors:
    name = Turtle(shape="turtle")
    name.color(col)
    turtles.append(name)
    name.penup()
    name.goto(-230, y)
    y += 50

# create screen
screen = Screen()
screen.setup(width=500, height=400)
# screen input prompt
user_input = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Select color: ")

if user_input:
    race_is_on = True
while race_is_on:
    random.shuffle(turtles)
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            break
        turtle.forward(random.randint(0, 10))
if user_input == turtle.pencolor():
    print(f"You won! The winner is {turtle.pencolor()} turtle")
else:
    print(f"You lost! The winner is {turtle.pencolor()} turtle")


# to persist the screen
screen.exitonclick()
