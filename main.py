import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # password_list = []

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    letter_list = [random.choice(letters) for char in range(nr_letters)]

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)

    symbol_list = [random.choice(symbols) for _ in range(nr_symbols)]

    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    number_list = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = letter_list + symbol_list + number_list

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    password = "".join(password_list)

    # print(f"Your password is: {password}")
    passwd_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_entries():
    url = website_input.get()
    username = username_input.get()
    passwd = passwd_input.get()
    new_data = {
        url: {
            "email": username,
            "password": passwd,
        }
    }

    if len(url) == 0 or len(passwd) == 0:
        messagebox.showerror(title="Empty Inputs", message="Please enter Website and/or Password.")

    else:
        try:
            with open("data.json", "r") as file:
                # Read old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Update old data
            data.update(new_data)

            # Saving updated data
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)

        finally:
            website_input.delete(0, END)
            passwd_input.delete(0, END)

def find_password():
    #get input from user
    url = website_input.get()

    try:
        #load database from json file
        with open("data.json", "r") as data_file:
            database = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title="No Data File Found", message="No Data File Found")

    else:
        #find data from user input in database
        if not url: # Empty strings are false
            messagebox.showerror(title="Empty Inputs", message="Please enter Website.")
        elif url not in database:
            messagebox.showerror(title="No website info found", message="No website info found.")
        else:
            email = database[url]["email"]
            print(email)
            password = database[url]["password"]
            print(password)

            messagebox.showinfo(title=url, message=f"username is : {email} \npassword is : {password} ")







# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_pic = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_pic)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()

search_button = Button(text="Search", width=13, font=("Courier", 9, "normal"), highlightthickness=0, command=find_password)
search_button.grid(row=1, column=2)

username_label = Label(text="Email/Username :")
username_label.grid(row=2, column=0)

username_input = Entry(width=42)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "email@example.com.sg")

passwd_label = Label(text="Password :")
passwd_label.grid(row=3, column=0)

passwd_input = Entry(width=21)
passwd_input.grid(row=3, column=1)

gen_passwd_button = Button(text="Generate Password", font=("Courier", 9, "normal"), highlightthickness=0,
                           command=generate_password)
gen_passwd_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, highlightthickness=0, command=save_entries)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
