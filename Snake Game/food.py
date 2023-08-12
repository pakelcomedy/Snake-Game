from turtle import Turtle
from random import *

# render the food as a small circle
class Food (Turtle):
    def __init__(self):
        super().__init__()
        self.shape ("circle")
        self.penup()
        self.shapesize (stretch_len=0.5,stretch_wid=0.5)
        self.color ("blue")
        self.speed ("fastest")
        self.refresh()    

# this places the food at a random location
# we call this when the snake touches food
    def refresh (self):
        random_x = randint (-280, 280)
        random_y = randint (-280, 280)
        self.goto(random_x, random_y)
