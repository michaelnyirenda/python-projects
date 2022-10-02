from turtle import Screen, down
from snake import Snake
import time

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Danger Noodle: The Game")
screen.tracer(0)

snake = Snake()

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

screen.exitonclick()


# s = Shape("compound")
# poly1 = ((0,0),(10,-5),(0,10),(-10,-5))
# s.addcomponent(poly1, "white", "blue")
# # poly2 = ((0,0),(10,-5),(-10,-5))
# # s.addcomponent(poly2, "blue", "red")

# register_shape("snake", s)
# snake =  Turtle(shape = "snake")
# snake.color = "white"
