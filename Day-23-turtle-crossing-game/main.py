
# and moves the turtle north
# 

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

TIME_DIFF = 600
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
CARS = []


def update_cars():
    """Adds cars to CARS list"""
    car_manager = CarManager()
    CARS.append(car_manager)


scoreboard = Scoreboard()

game_is_on = True
time1 = time.time()
update_cars()
while game_is_on:
    time.sleep(0.1)
    scoreboard.writer()
    screen.update()
    screen.listen()
    screen.onkey(player.move, "Up")
    time_diff = (time.time() - time1) * 1000
    if time_diff >= TIME_DIFF:
        update_cars()
        time1 = time.time()
    for car in CARS:
        # Shorten the list for cars that are past the boundaries
        if car.xcor() > 310:
            CARS.remove(car)
            continue
        if car.distance(player) < 20 or player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
            print(len(CARS))
        car.move()
    if player.finish():
        player.restart()
        scoreboard.increase()
        TIME_DIFF -= 50  # For adjusting the car generation speed
        CarManager.move_faster()

screen.exitonclick()
