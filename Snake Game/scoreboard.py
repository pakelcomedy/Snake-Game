from turtle import Turtle

FONT = ("Courier",14,"normal")

# this is used to define text on the scoreboard
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color ("white")
        self.penup()
        self.goto (0,270)
        self.write (f"Score: {self.score}", align="center",font=FONT)
        self.hideturtle()

# this method increases the score by 1
# it also clears the screen and writes a new score
# it is called when the snake eats a food
    def increase_score(self):        
        self.score+=1
        self.clear()
        self.write (f"Score: {self.score}", align="center",font=FONT)

# this displays GAME OVER on the screen
    def gameover (self):
        self.goto (0,0)
        self.write (f"GAME OVER", align="center",font=FONT)