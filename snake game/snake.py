from turtle import Turtle

SEGMENT_POS = [(0,0), (-20, 0), (-40, 0)] # list of segment positions
MOVE_DISTANCE = 20 # distance to move each segment
DIRECTIONS = [0, 90, 180, 270] # Right, Up, Left, Down
class Snake:
    def __init__(self):
        self.segments =[]
        self.create_snake()
        
    def create_snake(self):
        """Create the snake"""
        for i in SEGMENT_POS:
            self.add_segment(i)
            
    def add_segment(self, i):
        segment = Turtle(shape = "square")
        segment.penup()
        segment.color("white")
        segment.setpos(i)
        self.segments.append(segment)
    
    def extend(self):
        #add a new segment to snake
        self.add_segment(self.segments[-1].position())
    
    def move(self):
        """move the each segment to the position of the segment in front of it"""
        for i in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[i-1].xcor() # the x coordinate of the segment in front of it
            new_y = self.segments[i-1].ycor() # the y coordinate of the segment in front of it
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
        
    def up(self):
        if self.segments[0].heading() != DIRECTIONS[3]: # if not heading down
            self.segments[0].setheading(DIRECTIONS[1]) # then head up
    
    def down(self):
        if self.segments[0].heading() != DIRECTIONS[1]: # if not heading up
            self.segments[0].setheading(DIRECTIONS[3]) # then head down
        
    def left(self):
        if self.segments[0].heading() != DIRECTIONS[0]: # if not heading right
            self.segments[0].setheading(DIRECTIONS[2]) # then head left
        
    def right(self):
        if self.segments[0].heading() != DIRECTIONS[2]: # if not heading left
            self.segments[0].setheading(DIRECTIONS[0]) # then head right
        