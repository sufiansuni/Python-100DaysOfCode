# ---------------------------- DESCRIPTION ------------------------------- #
# Password Manager App
# ------------
# stores login information entered by user
# user is able to access it later on
# user ux: click to copy info to clipboard, easy to paste to website

# ---------------------------- IMPORTS ------------------------------- #
import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0)
logo_img = tkinter.PhotoImage(file="day-29-PasswordManager/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.pack()

window.mainloop()
