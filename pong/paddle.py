# a paddle will move up and down until it reaches the top or bottom of the screen 
from turtle import *
class Paddle(Turtle):
    def __init__(self, x, y):
        super(Paddle, self).__init__()
        # the paddle that will move up and down
        self.shape("square")
        self.speed(0)
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(x, y)


    def up(self):
        #change the ycor by 20 pixels
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    
    def down(self):
        #move paddle by 20 pixels down
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
  