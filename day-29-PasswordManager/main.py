# ---------------------------- DESCRIPTION ------------------------------- #
# Password Manager App
# --------------------
# stores login information entered by user
# user ux: user can paste a generated password

# ---------------------------- IMPORTS ------------------------------- #
import tkinter
from tkinter.constants import END, N
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]

    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)

    password_entry.delete(0, END)
    password_entry.insert(END, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_login():
    # prepare new data as json
    new_data ={
        website_entry.get() : {
            "email": email_entry.get(),
            "password": password_entry.get()
        }
    }

    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Error", message="Fields cannot be blank")
    else:
        try:
            with open("day-29-PasswordManager/data.json", "r") as data_file:
                # read file /load json
                data = json.load(data_file)

        except FileNotFoundError:
            # create file if not found 
            with open("day-29-PasswordManager/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # update old data
            data.update(new_data)
            # open in write mode and update 
            with open("day-29-PasswordManager/data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            # clear the input fields
            website_entry.delete(0, END) 
            # email_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def search_login():
    website = website_entry.get()
    # read data file
    try:
        with open("day-29-PasswordManager/data.json", "r") as data_file:
            # read file /load json
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Data file not found", message="data.json not found")
    else:
        try:
            login_data = data[website]
        except KeyError:
            messagebox.showinfo(title="No login data", message="No login data for entered website")
        else:
            try:
                email = login_data["email"]
                password = login_data["password"]
            except KeyError:
                messagebox.showinfo(title="Missing fields", message="Login data is missing either email/username or password fields")
            else:
                messagebox.showinfo(title=f"Login Data for {website}", message=f"Email: {email}\nPassword: {password}")
                pyperclip.copy(password)

# ---------------------------- UI SETUP ------------------------------- #
# Window
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Logo (Canvas)
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
logo_img = tkinter.PhotoImage(file="day-29-PasswordManager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# label_1
label_1_text = "Website:"
label_1 = tkinter.Label(text=label_1_text)
label_1.grid(row=1, column=0)

# website_entry
website_entry = tkinter.Entry(width=35)
website_entry.grid(row=1, column=1, sticky="EW")
website_entry.focus()

# search button
add_pass_btn = tkinter.Button(text="Search", command=search_login)
add_pass_btn.grid(row=1, column=2, sticky="EW")

# label_2
label_2_text = "Email/Username:"
label_2 = tkinter.Label(text=label_2_text)
label_2.grid(row=2, column=0)

# email_entry
default_email = "sufiansuni@gmail.com"
email_entry = tkinter.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(END, default_email)

# label_3
label_3_text = "Password:"
label_3 = tkinter.Label(text=label_3_text)
label_3.grid(row=3, column=0)

# password_entry
password_entry = tkinter.Entry(width=20)
password_entry.grid(row=3, column=1, sticky="EW")

# generate password button
gen_pass_btn = tkinter.Button(text="Generate Password", command=generate_password)
gen_pass_btn.grid(row=3, column=2, sticky="EW")

# add button
add_pass_btn = tkinter.Button(text="Add", command=save_login, width=36)
add_pass_btn.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
