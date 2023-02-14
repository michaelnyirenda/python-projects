from tkinter import *
import pandas as pd
from random import *

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- WORDS ------------------------------- #
data = pd.read_csv("data/french_words.csv")
words = data.to_dict(orient="records")

# ---------------------------- FLASH CARDS ------------------------------- #
def press():
    word = choice(words)
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(card_word, text=word["French"])
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

# card front
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word=canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# # card back 
# card_back = PhotoImage(file="images/card_back.png")
# canvas.create_image(400, 263, image=card_back)
# canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
# word_back = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
# canvas.grid(column=0, row=0, columnspan=2)


# Buttons
correct = PhotoImage(file="images/right.png",)
correct_button = Button(image=correct, highlightthickness=0, command = press)
correct_button.grid(column=1, row=1)

wrong = PhotoImage(file="images/wrong.png",)
wrong_button = Button(image=wrong, highlightthickness=0, command = press)
wrong_button.grid(column=0, row=1)

press()

window.mainloop()