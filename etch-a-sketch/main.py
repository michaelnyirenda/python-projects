from turtle import Turtle, Screen

raph = Turtle()
screen = Screen()

# moving forward by ten steps
def move_forward():
    raph.forward(10)
    
# moving backward by ten steps  
def move_backward():
    raph.backward(10)
    
# turn left by 5 degrees
def turn_left():
    raph.left(5)
    
# turn right by 5 degrees
def turn_right():
    raph.right(5)
    
# clear the Screen
def clear():
    raph.clear()
    raph.penup()
    raph.home()
    raph.pendown()


screen.listen()
screen.onkeypress(key="w", fun =  move_forward)
screen.onkeypress(key="s", fun =  move_backward)
screen.onkeypress(key="a", fun =  turn_left)
screen.onkeypress(key="d", fun =  turn_right)
screen.onkeypress(key="c", fun =  clear)

screen.exitonclick()