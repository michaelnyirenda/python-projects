from turtle import Turtle, Screen

screen = Screen()
screen.setup(width = 500, height = 500)

colours = ["red", "purple", "orange", "blue", "green"]
y_pos = [200, 100, 0, -100, -200]

for i in colours:
    turtle =  Turtle(shape = "turtle")
    turtle.color(i)
    turtle.penup()
    turtle.goto(x = -230, y = y_pos[colours.index(i)])
    
    
    

    
# user_bet = screen.textinput(title = "make your bet", prompt = "which turtle will win the race? enter a name: ")

 











screen.exitonclick()