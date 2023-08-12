from turtle import Turtle
# in python, constants are displayed in ALL-CAPS

STARTING = [(0,0),(0,-20),(0,-40)]
MOVE_DISTANCE = 20
UP=90
DOWN=270
RIGHT=0
LEFT=180
    
class Snake:
    def __init__(self):         
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

   # this is used to create the snake
     # we defined a starting position   
    def create_snake(self):
        for position in STARTING:
            self.add_segment(position)            
    
    # this is used to define each of the segments
    def add_segment (self, position):
        new=Turtle(shape="square")
        new.color("white")
        new.penup()
        new.goto (position)
        self.segments.append(new)
    
    # this is used to define the position of new snake segments
    def extend (self):
        self.add_segment(self.segments[-1].position())

    # this is used to gte the snake to move
    def move(self):
        for seg_num in range (len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        
        self.head.forward(MOVE_DISTANCE)  

# these define the direction of the snake
    def up (self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
    def down (self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left (self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right (self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)