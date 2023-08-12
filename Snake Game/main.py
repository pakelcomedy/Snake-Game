from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#define our screen
screen=Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

# create objects from the Snake, Food and Scoreboard classes
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# define the control keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# create a while loop to keeping running
game_on = True
while game_on: 
    # the screen updates, the time delays, and the snake moves continuously
    screen.update()
    time.sleep(0.1)
    snake.move()

# what happens when the snake comes in contact with food
        # the food goes to a different location
        # the snake increases in length
        # the scoreboard increases in score
    if snake.head.distance (food)<15:        
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

# what happens when the snake hits the edges of the screen
    # the loop ends
    # the game is over
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_on=False
        scoreboard.gameover()

# what happens when the snake comes in contact with its body
    # the loop ends
    # the game is over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on=False
            scoreboard.gameover()

screen.mainloop()