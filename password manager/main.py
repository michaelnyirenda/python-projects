from tkinter import *
import csv

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# write to csv file
header = ["website", "email/username", "password"]
with open("data.csv", "w", newline='') as data_file:
    writer = csv.writer(data_file)
    writer.writerow(header)
    
password_data = []

def save():
    # get input from entries and append to data list
    password_data.append(f'{website_entry.get()}')
    password_data.append(f'{email_username_entry.get()}')
    password_data.append(f'{password_entry.get()}')
    
    # clear entries
    website_entry.delete(0, END)
    email_username_entry.delete(0, END)
    password_entry.delete(0, END)
    
    # write to csv file
    with open("data.csv", "a", newline='') as data_file:
        writer = csv.writer(data_file)
        writer.writerow(password_data)
    
    # clear data list
    password_data.clear()


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
website_entry = Entry(window, width = 46,)
website_entry.grid(row=1, column=1,  columnspan=2, sticky='w')
website_entry.focus()

email_username_entry = Entry(window, width = 46,)
email_username_entry.grid(row=2, column=1,  columnspan=2,sticky='w')

password_entry = Entry(window, width = 28)
password_entry.grid(row=3, column=1,sticky='w')

# buttons
generate_button = Button(window, text="New Password")
generate_button.grid(row=3, column=2, sticky='w')

add_button = Button(window, text="Add", width=39, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky='w')


window.mainloop()