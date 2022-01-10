# ---------------------------- DESCRIPTION ------------------------------- #
# Password Manager App
# --------------------
# stores login information entered by user
# user ux: user can paste a generated password

# ---------------------------- IMPORTS ------------------------------- #
import tkinter
from tkinter.constants import END
from tkinter import messagebox
import random
import pyperclip

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

    entry_3.delete(0, END)
    entry_3.insert(END, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_login():

    # prepare a new login data entry
    new_login = f"{entry_1.get()} | {entry_2.get()} | {entry_3.get()}\n"

    if len(entry_1.get()) == 0 or len(entry_2.get()) == 0 or len(entry_3.get()) == 0:
        messagebox.showinfo(title="Error", message="Fields cannot be blank")
    else:
        # confirmation messagebox
        is_ok = messagebox.askokcancel(title=entry_1.get(), message=f"Details:\n{new_login}\nSave?")
        # write it as a new line in a file, data.txt
        
        if is_ok:
            with open("day-29-PasswordManager/data.txt", "a") as file:
                file.write(new_login)

            # clear the input fields
            entry_1.delete(0, END) 
            # entry_2.delete(0, END)
            entry_3.delete(0, END)

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

# entry_1
entry_1 = tkinter.Entry(width=35)
entry_1.grid(row=1, column=1, columnspan=2, sticky="EW")
entry_1.focus()

# label_2
label_2_text = "Email/Username:"
label_2 = tkinter.Label(text=label_2_text)
label_2.grid(row=2, column=0)

# entry_2
default_email = "sufiansuni@gmail.com"
entry_2 = tkinter.Entry(width=35)
entry_2.grid(row=2, column=1, columnspan=2, sticky="EW")
entry_2.insert(END, default_email)

# label_3
label_3_text = "Password:"
label_3 = tkinter.Label(text=label_3_text)
label_3.grid(row=3, column=0)

# entry_3
entry_3 = tkinter.Entry(width=20)
entry_3.grid(row=3, column=1, sticky="EW")

# generate password button
gen_pass_btn = tkinter.Button(text="Generate Password", command=generate_password)
gen_pass_btn.grid(row=3, column=2, sticky="EW")

# add button
add_pass_btn = tkinter.Button(text="Add", command=save_login, width=36)
add_pass_btn.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
