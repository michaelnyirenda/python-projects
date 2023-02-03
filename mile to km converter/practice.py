from tkinter import *


def button_clicked():
    my_label.config(text=input.get()) # get() is used to get the text from the entry

# Window
window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20) # padding
 
# Label
my_label = Label(text="I am a label", font=("Arial", 24, "italic"))
my_label.grid(column= 0, row = 0) # pack() is used to show the label on the screen

# Button
new_button = Button(text="Click Me") # button is an object
new_button.grid(column = 2,  row = 0) # pack() is used to show the button on the screen

button = Button(text="Click Me", command = button_clicked) # button is an object
button.grid(column = 1,  row = 1) # pack() is used to show the button on the screen


# Entry
input = Entry(width=10)
input.grid(column = 3,  row = 2) # pack() is used to show the entry on the screen
 











window.mainloop()

