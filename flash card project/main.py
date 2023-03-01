from tkinter import *
import pandas as pd
from random import *
from os.path import exists

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
words = {}

# ---------------------------- WORDS ------------------------------- #
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    words = original_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")
    
# ---------------------------- FLASH CARDS ------------------------------- #
def next_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = choice(words)
    canvas.itemconfig(title, text="French", fill = "black")
    canvas.itemconfig(card_word, text=current_word["French"], fill = "black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, flip)
    
# ---------------------------- CARD FLIP ------------------------------- #
def flip():
    canvas.itemconfig(title, text="English", fill = "white")
    canvas.itemconfig(card_word, text=current_word["English"], fill = "white")
    canvas.itemconfig(canvas_image, image=card_back)
        
# ---------------------------- REMOVE WORD ------------------------------- #
def remove_word():
    words.remove(current_word)
    next_word()
    updated_data = pd.DataFrame(words)
    updated_data.to_csv("data/words_to_learn.csv", index=False)
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip)
    
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
correct = PhotoImage(file="images/right.png",)
correct_button = Button(image=correct, highlightthickness=0, command = remove_word)
correct_button.grid(column=1, row=1)

wrong = PhotoImage(file="images/wrong.png",)
wrong_button = Button(image=wrong, highlightthickness=0, command = next_word)
wrong_button.grid(column=0, row=1)

next_word()

window.mainloop()

