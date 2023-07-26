from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = []
    password_letters = [choice(letters) for char in range(randint(8,10))]
    password_symbols = [choice(symbols) for char in range(randint(2,4))]
    password_numbers = [choice(numbers) for char in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pwd():
    web_name = website_entry.get()
    usr = email_entry.get()
    pwd = password_entry.get()

    if len(web_name) == 0 or len(usr) == 0 or len(pwd) == 0:
        messagebox.showinfo(title="Missing fields! Go back!", message="Please don't leave any fields empty D:")
    else:
        is_ok = messagebox.askokcancel(title=web_name, message=f"These are the details that have been entered: \n Email/Username:{usr} \n Password: {pwd} \n Is it ok to save?")
        
        if is_ok == True:
            with open("saved_passwords.txt", "a") as file:
                file.write(f"{web_name} | {usr} | {pwd} \n")
            
            messagebox.showinfo(title="Password Manager", message="Success! Your password has been saved!")
                
            website_entry.delete(0,END)
            password_entry.delete(0,END)
    

def default_email_button():
    email_entry.insert(0, default_email)        


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=70)
default_email = "alex.jiang903@gmail.com"

canvas = Canvas(width=200, height=200)
canvas.grid(column=1, row=0)
logo = PhotoImage(file="logo.png")

canvas.create_image(100,100, image=logo)

website_label = Label(text="Website:", font=("Arial", 16, "bold"))
website_label.grid(column=0,row=1)

username_label = Label(text="Email/Username:", font=("Arial", 16, "bold"))
username_label.grid(column=0,row=2)

password_label = Label(text="Password:", font=("Arial", 16, "bold"))
password_label.grid(column=0,row=3)

website_entry = Entry(width=38)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=21)
email_entry.grid(column=1,row=2)

email_button = Button(text="Use default email", command=default_email_button)
email_button.grid(column=2, row=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", command=password_generator)
password_button.grid(column=2,row=3)

add_password = Button(text="Add", width=36, command=save_pwd)
add_password.grid(column=1,row=4, columnspan=2)

window.mainloop()