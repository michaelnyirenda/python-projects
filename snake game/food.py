from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("coral")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        x=random.randint(-580, 580)
        y=random.randint(-580, 580)
        self.goto(x, y)
     