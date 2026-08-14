from turtle import Turtle
import random

class Food(Turtle): #inherits the properties of Turtle

    def __init__(self):
        super().__init__()
        self.shape("circle") # shapes the food that is dot in the game
        self.penup() #avoid drawing the line
        self.shapesize(stretch_wid=0.5,stretch_len=0.5) #it sets the size of the Dot
        self.color("red")
        self.speed("fastest")
        self.refresh()

# to generate the new dot that is food at random position
    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)