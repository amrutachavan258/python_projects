from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0) #controls the animation

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

# Right paddle
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeyrelease(r_paddle.stop_up, "Up")

screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeyrelease(r_paddle.stop_down, "Down")

# Left paddle
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeyrelease(l_paddle.stop_up, "w")

screen.onkeypress(l_paddle.go_down, "s")
screen.onkeyrelease(l_paddle.stop_down, "s")
game_is_on = True
while game_is_on:

    time.sleep(ball.move_speed)

    screen.update()

    r_paddle.move()
    l_paddle.move()

    ball.move()


    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with r_paddle
    if (
            ball.distance(r_paddle) < 50
            and ball.xcor() > 320
    ) or (
            ball.distance(l_paddle) < 50
            and ball.xcor() < -320
    ):
        ball.bounce_x()

    #Detect R paddle missed
    # Right player misses
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    # Left player misses
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()