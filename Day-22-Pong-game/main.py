# Approach
# Create screen
# Create and move paddle
# Create another paddle
# Create the ball and move it
# Detect collision with the wall and bounce
# Detect collision with paddle
# Detect when the paddle misses
# Keep score

# module imports
import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# creating the screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)
screen.listen()

paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.roll_speed)
    screen.update()
    scoreboard.update_score()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    ball.move()
    # Detecting collision and bouncing the ball on the paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    # Detect scoring and centering the ball
    # If right side misses
    if ball.xcor() > 380:
        ball.reset_position()
        ball.bounce_x() # to change the direction of the ball
        # scoreboard.l_score += 1 you should create the l_score private and use a method instead
        scoreboard.l_point()

    # if left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        ball.bounce_x()
        # scoreboard.r_score += 1 you should create the r_score private and use a method instead
        scoreboard.r_point()

    screen.onkey(paddle_right.up, "Up")
    screen.onkey(paddle_left.up, "W")
    screen.onkey(paddle_right.down, "Down")
    screen.onkey(paddle_left.down, "S")


screen.exitonclick()