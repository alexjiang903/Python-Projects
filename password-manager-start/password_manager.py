from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

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

    new_data = {
        web_name : {
            "Username":usr,
            "Password": pwd, 
        }
    }

    if len(web_name) == 0 or len(usr) == 0 or len(pwd) == 0:
        messagebox.showinfo(title="Missing fields! Go back!", message="Please don't leave any fields empty D:")
    else:
        try:
            with open("data.json", "r") as file:
                # Read data
                data = json.load(file)
                
                # Updating old data with new data
                data.update(new_data)
        
        except FileNotFoundError:    
            with open("data.json", "a") as file:
                json.dump(new_data, file, indent = 4)
                
                
        else:
            with open("data.json", "w") as file:    
                #Saving new data
                json.dump(data, file, indent=4)

        finally:    
            website_entry.delete(0,END)
            email_entry.delete(0,END)
            password_entry.delete(0,END)
            messagebox.showinfo(title="Password Manager", message="Success! Your password has been saved!")


def find_password():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            web_name = data[website_entry.get()]
            found_username = web_name["Username"]
            found_password = web_name["Password"]
            messagebox.showinfo(title=website_entry.get(), message=f"Username: {found_username} \n Password: {found_password}")

    except FileNotFoundError:
        messagebox.showinfo(title="Error!", message="No Data File Found! Please try again.")

    except KeyError:
        messagebox.showinfo(title="Error!", message="No website found! Please try again.")
        

def default_email_button():
    email_entry.insert(0, default_email)        


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=70)
default_email = "alex.jiang903@gmail.com"

canvas = Canvas(width=200, height=200)
canvas.grid(column=1, row=0)
logo = PhotoImage(file="password-manager-start/logo.png")

canvas.create_image(100,100, image=logo)

website_label = Label(text="Website:", font=("Arial", 16, "bold"))
website_label.grid(column=0,row=1)

username_label = Label(text="Email/Username:", font=("Arial", 16, "bold"))
username_label.grid(column=0,row=2)

password_label = Label(text="Password:", font=("Arial", 16, "bold"))
password_label.grid(column=0,row=3)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=21)
email_entry.grid(column=1,row=2)

email_button = Button(text="Use default email", command=default_email_button)
email_button.grid(column=2, row=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", command=password_generator, width=13)
password_button.grid(column=2,row=3)

add_password = Button(text="Add", width=36, command=save_pwd)
add_password.grid(column=1,row=4, columnspan=2)

search_button = Button(text="Password search", command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()