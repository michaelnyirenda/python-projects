from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width = 500, height = 500)

racing = True

user_bet = screen.textinput(title = "make your bet", prompt = "which turtle will win the race? enter a name: ")

colours = ["red", "purple", "orange", "blue", "green"]
turtles = []
y_pos = [200, 100, 0, -100, -200]

for i in colours:
    turtle =  Turtle(shape = "turtle")
    turtle.color(i)
    turtle.penup()
    turtle.goto(x = -230, y = y_pos[colours.index(i)])
    turtles.append(turtle)

if user_bet:
    racing = True
    
while racing:
    #move the turtle forward with random number between 0 and 10
    for i in turtles:
        if i.xcor() > 230:
            racing = False
            winning_colour = i.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner!")
        rand_distance = randint(0, 10)
        i.forward(rand_distance)



screen.exitonclick()