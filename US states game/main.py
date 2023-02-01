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


# record the correct guesses in a list
correct_guesses = []

 # use loop to allow user to keep guessing
while len(correct_guesses) < 50:
    # update score in the title (0/50)  
    answer_state = screen.textinput(title = f"{len(correct_guesses)}/50", prompt="What's another state's name?")
    # covert to title case
    answer_state = answer_state.title()
    
    if answer_state == 'Exit':
        # create a new data frame with the states that were not guessed 
        states_left_over = [state for state in data.state.values if state not in correct_guesses]

        # create a new csv file with the states that were not guessed
        df = pd.DataFrame(states_left_over)
        df.to_csv('states_to_learn.csv')
        break

    # check if guess is among 50 states
    if answer_state in data.state.values:
        # write  correct guess on the map
        pen.setpos(int(data[data.state == answer_state]['x']), int(data[data.state== answer_state]['y']))
        pen.write(answer_state, align = 'center')
        # keep track of the number of correct guesses
        correct_guesses.append(answer_state)
        
        

        

    




