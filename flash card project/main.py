from tkinter import *
import pandas as pd
from random import *

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- WORDS ------------------------------- #
df = pd.read_csv("data/french_words.csv")
words = df.to_dict(orient="records")


# ---------------------------- FLASH CARDS ------------------------------- #

def press():
    word = choice(words)
    canvas.itemconfig(word_back, text=word["French"])


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

canvas.create_image(400, 263, image=card_front)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
word_front = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

canvas.create_image(400, 263, image=card_back)
canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word_back = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# Buttons
right = PhotoImage(file="images/right.png",)
right_button = Button(image=right, highlightthickness=0, command = press)
right_button.grid(column=1, row=1)

wrong = PhotoImage(file="images/wrong.png",)
wrong_button = Button(image=wrong, highlightthickness=0, command = press)
wrong_button.grid(column=0, row=1)

window.mainloop()