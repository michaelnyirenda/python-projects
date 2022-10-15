from turtle import Screen, down
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Danger Noodle: The Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

# screen listening for key presses
screen.listen()

# key press handling
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_running = True
while game_running:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # detect collisions with food 
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        score.update_score()

screen.exitonclick()


