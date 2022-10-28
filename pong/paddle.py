# # a paddle will move up and down until it reaches the top or bottom of the screen 
# from turtle import *
# x = 350
# y = 0
# class Paddle:
#     def __init__(self):
        
#         paddle = Turtle(shape = "square")
#         paddle.speed(0)
#         paddle.penup()
#         paddle.color("white")
#         paddle.shapesize(stretch_wid=5, stretch_len=1)
#         paddle.setposition(x, y)
        
#     def up():
#         #change the ycor by 20 pixels
#         new_y = paddle.sety(y + 20)
#         paddle.goto(x, new_y)
        
#     def down(paddle):
#         #move paddle by 20 pixels down
#         new_y = paddle.sety(y - 20)
#         paddle.goto(x, new_y)