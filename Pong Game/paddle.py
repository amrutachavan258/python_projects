
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

        # Set paddle starting position
        self.goto(position)

        # Movement flags
        self.moving_up = False
        self.moving_down = False

    def go_up(self):
        # Start moving upward
        self.moving_up = True

    def go_down(self):
        # Start moving downward
        self.moving_down = True

    def stop_up(self):
        # Stop moving upward
        self.moving_up = False

    def stop_down(self):
        # Stop moving downward
        self.moving_down = False

    def move(self):

        # Move upward while key is pressed
        if self.moving_up and self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + 10)

        # Move downward while key is pressed
        if self.moving_down and self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 10)