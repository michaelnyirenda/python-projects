from turtle import Turtle

SEGMENT_POS = [(0,0), (-20, 0), (-40, 0)] # list of segment positions
MOVE_DISTANCE = 20 # distance to move each segment

class Snake:
    def __init__(self):
        self.segments =[]
        self.create_snake()
        
    def create_snake(self):
        """Create the snake"""
        for i in SEGMENT_POS:
            segment = Turtle(shape = "square")
            segment.penup()
            segment.color("white")
            segment.setpos(i)
            self.segments.append(segment)
    
    def move(self):
        """move the each segment to the position of the segment in front of it"""
        for i in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[i-1].xcor() # the x coordinate of the segment in front of it
            new_y = self.segments[i-1].ycor() # the y coordinate of the segment in front of it
            self.segments[i].goto(new_x, new_y)
        
        self.segments[0].forward(MOVE_DISTANCE)