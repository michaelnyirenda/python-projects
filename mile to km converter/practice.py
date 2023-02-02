import tkinter

window = tkinter.Tk()

window.title("My first GUI program")

window.minsize(width=500, height=300)
 
# Label

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "italic"))
my_label.pack(expand = True) # pack() is used to show the label on the screen




















window.mainloop()

