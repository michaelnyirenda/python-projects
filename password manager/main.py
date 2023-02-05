from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

photo = PhotoImage(file="logo.png")

canvas = Canvas(width=300, height=200)
canvas.create_image(100, 100, image=photo)
canvas.grid(column = 1, row = 0, columnspan=2, sticky='w')

# labels
website = Label(text="Website:")
website.grid(row=1, column=0)

email_username = Label(text="Email/Username:")
email_username.grid(row=2, column=0)

password = Label(text="Password:")
password.grid(row=3, column=0)

# entries
website_entry = Entry(width = 46,)
website_entry.grid(row=1, column=1,  columnspan=2, sticky='w')

email_username_entry = Entry(width = 46,)
email_username_entry.grid(row=2, column=1,  columnspan=2,sticky='w')

password_entry = Entry( width = 28)
password_entry.grid(row=3, column=1,sticky='w')

# buttons
generate_button = Button(window, text="New Password")
generate_button.grid(row=3, column=2, sticky='w')

add_button = Button(window, text="Add", width=39)
add_button.grid(row=4, column=1, columnspan=2, sticky='w')


window.mainloop()