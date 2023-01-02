from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = site_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) ==0:
        messagebox.showinfo(title="Oops", message = "Please make sure you haven't left any empty fields.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Adding updated data
                 json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(new_data, data_file, indent=4)

        finally:
                site_entry.delete(0, END)
                pass_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def find_password():
    website = site_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPasssword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No detail for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
key_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=key_img)
canvas.grid(row=0, column=1)

#Labels:
site_label = Label(text="Website:")
site_label.grid(column=0, row=2)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=3)
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=4)

#Entries:
site_entry = Entry(width=21)
site_entry.grid(column=1, row=2)
site_entry.focus()
email_entry = Entry(width=36)
email_entry.grid(column=1, row=3, columnspan=2)
email_entry.insert(0, "dothuytrang2312@gmail.com")
pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=4)

#Buttons:
pass_generate = Button(text="Generate Password", highlightthickness=0, command=generate_password)
pass_generate.grid(column=2, row=4)

search_button = Button(text="Search", width=15, highlightthickness=0, command=find_password)
search_button.grid(column=2, row=2)

add_button = Button(text="Add", width=36, highlightthickness=0, command=save)
add_button.grid(column=1, row=5, columnspan=2)

window.mainloop()