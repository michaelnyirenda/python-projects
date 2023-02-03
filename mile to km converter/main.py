from tkinter import *


def button_clicked():
    result.config(text=round(int(input.get())*1.609344)) # get() is used to get the text from the entry

# Window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=10, pady=10) # padding
 
# Label
miles = Label(text="Miles", font=("Arial"))
miles.grid(column= 2, row = 0) # pack() is used to show the label on the screen

equal = Label(text="is equal to", font=("Arial"))
equal.grid(column= 0, row = 1) # pack() is used to show the label on the screen

km = Label(text="Km", font=("Arial"))
km.grid(column= 2, row = 1) # pack() is used to show the label on the screen

result = Label(text="0", font=("Arial"))
result.grid(column= 1, row = 1) # pack() is used to show the label on the screen

# Button
button = Button(text="Calculate", command = button_clicked) # button is an object
button.grid(column = 1,  row = 2) # pack() is used to show the button on the screen

# Entry
input = Entry(width=10)
input.grid(column = 1,  row = 0) # pack() is used to show the entry on the screen

window.mainloop()
