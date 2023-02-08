from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []
    
    # add letters, symbols and numbers to the list
    password_list += [choice(letters) for x in range(randint(8, 12))]
    password_list += [choice(symbols) for x in range(randint(2, 4))]
    password_list += [choice(numbers) for x in range(randint(2, 4))]

    #shuffle only works on a list so that's why we have the list password plus
    shuffle(password_list)

    #add the characters of the list to the string
    password = "".join(password_list)
        
    password_entry.insert(0, password)
    pyperclip.copy(password)
    password_list.clear()
    
# ---------------------------- SEARCH ------------------------------- #
def search():
    website = website_entry.get().capitalize()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # get input from entries and append to data list
    website = website_entry.get().capitalize()
    email_username = email_username_entry.get()
    password = password_entry.get()
    
    new_data = {
       website: {
              "email": email_username,
              "password": password,
           }
       }
    
    if len(password) == 0 or len(website) == 0 or len(email_username) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        # check if file exists
        try:
            with open("data.json", "r") as data_file: # open in read mode
                data = json.load(data_file) # read data from file   
                
        # if file doesn't exist, create it        
        except FileNotFoundError:        
            with open("data.json", "w") as data_file: # open in write mode
                json.dump(new_data, data_file, indent=4) # write data to file
                
        # if file exists, update it
        else:
            data.update(new_data) # update data with new data
            with open("data.json", "w") as data_file: # open in write mode
                json.dump(data, data_file, indent=4) # write data to file
    
        finally:
            # clear entries
            website_entry.delete(0, END)
            email_username_entry.delete(0, END)
            password_entry.delete(0, END)

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
website_entry = Entry(window, width = 29)
website_entry.grid(row=1, column=1,  columnspan=2, sticky='w')
website_entry.focus()

email_username_entry = Entry(window, width = 46,)
email_username_entry.grid(row=2, column=1,  columnspan=2,sticky='w')

password_entry = Entry(window, width = 29)
password_entry.grid(row=3, column=1,sticky='w')

# buttons
generate_button = Button(window, text="New Password", width=11, command=generate_password)
generate_button.grid(row=3, column=2, sticky='w')

add_button = Button(window, text="Add", width=39, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky='w')

search_button = Button(window, text="Search", width=11, command=search)
search_button.grid(row=1, column=2, sticky='w')

window.mainloop()