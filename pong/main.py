# the screen that the pong game will happen in
# from paddle import Paddle
from turtle import *
X = 350
Y = 0

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

# the paddle that will move up and down
paddle = Turtle(shape = "square")
paddle.speed(0)
paddle.penup()
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.setposition(X, Y)


def up():
    #change the ycor by 20 pixels
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)
   
  
def down():
    #move paddle by 20 pixels down
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)
  
# key press handling
screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")


game_on = True
while game_on:
    screen.update()




























screen.exitonclick()