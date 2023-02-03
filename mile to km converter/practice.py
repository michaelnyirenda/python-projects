from tkinter import *

window = Tk()

window.title("My first GUI program")

window.minsize(width=500, height=300)
 
# Label

my_label = Label(text="I am a label", font=("Arial", 24, "italic"))
my_label.pack() # pack() is used to show the label on the screen


# Button

def button_clicked():
    my_label.config(text=input.get()) # get() is used to get the text from the entry

button = Button(text="Click Me", command = button_clicked) # button is an object
button.pack() # pack() is used to show the button on the screen


# Entry

input = Entry(width=10)
input.pack() # pack() is used to show the entry on the screen
 











window.mainloop()

