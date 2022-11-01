# the screen that the pong game will happen in
from paddle import Paddle
from ball import Ball
from turtle import *
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

score = Scoreboard()

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()

# key press handling
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    # detect collisions with walls and bounces
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # detect collisions with paddle
    # if ball.distance(left_paddle) < 10 or ball.distance(right_paddle) < 50:
    #     ball.bounce_x()
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    
    if ball.xcor() > 380:
        ball.reset_position()
        # add point to scoreboard
        score.l_point()
        
        
    if ball.xcor() < -380:
        ball.reset_position()
        # add point to scoreboard
        score.r_point()
    
   
    



























screen.exitonclick()