from turtle import Turtle
STARTING_POSITIONS= [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20 # Distance the snake moves in every step of the game.
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake: # This class contains everything related to the snake.

    def __init__(self):# Constructor method, It runs automatically when we create, snake = Snake()
        self.segments = []         # Empty list to store all the snake body segments.
        self.create_snake()        # Call create_snake() to create the initial snake.
        self.head = self.segments[0]        # The first segment is the HEAD of the snake.

    def create_snake(self): # create snake
        for position in STARTING_POSITIONS:  # loop to create a snake
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()  # Prevent the turtle from drawing a line while moving.
        new_segment.goto(position)  # Move the segment to its starting position.
        self.segments.append(new_segment)  # Add this segment to the snake's segments list.

    def extend(self):
        # add a new segment
        self.add_segment(self.segments[-1].position())

    def move(self): # to move the snake
        # to move snake forward the below for loop is used
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # Get the X position of the segment in front.
            new_y = self.segments[seg_num - 1].ycor() # Get the Y position of the segment in front.
            self.segments[seg_num].goto(new_x, new_y)# Move the current segment to the position
                                                     # of the segment in front of it.

        self.head.forward(MOVE_DISTANCE)  # Finally move the head forward.


#change the head direction
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)