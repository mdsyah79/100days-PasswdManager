from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_pic = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_pic)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)

username_label = Label(text="Email/Username :")
username_label.grid(row=2, column=0)

username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2)

passwd_label = Label(text="Password :")
passwd_label.grid(row=3, column=0)

passwd_input = Entry(width=21)
passwd_input.grid(row=3, column=1)

gen_passwd_button = Button(text="Generate Password", width=13, font=("Courier", 9, "normal"), highlightthickness=0)
gen_passwd_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, highlightthickness=0)
add_button.grid(row=4, column=1, columnspan=2)







window.mainloop()