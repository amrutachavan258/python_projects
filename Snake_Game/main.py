from turtle import Screen
import time
from Food import Food
from score import ScoreBoard
from snake import Snake


screen = Screen() #displays screen
screen.setup(width=600, height=600)
screen.bgcolor("black") #bg of screen
screen.title("My Snake Game") #title of the screen
screen.tracer(0) #for animation delay


snake = Snake() #the object of the snake class from snake.py to display the snake
food = Food()  #the object of the food class from food.py to display the food
scoreboard = ScoreBoard()  #the object of the scoreboard class from score.py to display the score

screen.listen() # Tell the screen to listen for keyboard input
screen.onkey(snake.up, "Up") # When the UP arrow key is pressed, call snake.up()
screen.onkey(snake.down, "Down") # When the DOWN arrow key is pressed, call snake.down()
screen.onkey(snake.left, "Left") # When the LEFT arrow key is pressed, call snake.left()
screen.onkey(snake.right, "Right") # When the RIGHT arrow key is pressed, call snake.right()

starting_position = [(0,0), (20,0), (-20,0), (-40,0)] #position of the squares which create a snake
segments = []
game_is_on = True
while game_is_on:
    screen.update()  # updates the screen
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh() #this is the method created in the food.py to create the new food after the snake touches
        snake.extend()
        scoreboard.increase_score()


    # Detect Collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick() # Keep the game window open until the user clicks on it