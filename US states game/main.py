import turtle
import pandas as pd

data = pd.read_csv('50_states.csv')

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)

# this turtle will draw the map
turtle.shape(image)

# this turtle will write the correct guesses on the map
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.speed('fastest')

# use loop to allow user to keep guessing
game_on = True
correct_guesses = []
score = 0
while game_on:
    answer_state = screen.textinput(title = f"{score}/50", prompt="What's another state's name?")
    # covert to title case
    answer_state = answer_state.title()

    # check if guess is among 50 states
    if answer_state in data['state'].values:
        # write  correct guess on the map
        pen.setpos(int(data[data['state'] == answer_state]['x']), int(data[data['state'] == answer_state]['y']))
        pen.write(answer_state, align = 'center')
        # record the correct guesses in a list
        correct_guesses.append(answer_state)
        # keep track of the number of correct guesses
        score += 1
        # update score in the title (0/50)
        

    




