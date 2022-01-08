import tkinter

# creating a tkinter widget
window = tkinter.Tk()

# set title of window
window.title("First Python GUI Program")

# set minimum size of window
window.minsize(width=500, height=300)

# set window padding
window.config(padx=20, pady=20)

# create a label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))

# displays label component onto center of program
# packer is a geometry management mechanism
# my_label.pack()

# place is another manager, sets absolute positions 
# my_label.place(x=0, y=0)

# grid will display component relatively to other grided components
# grid CANNOT be used with place
my_label.grid(column=0, row=0)

# create an input field
my_entry = tkinter.Entry(width=10)
my_entry.grid(column=1, row=1)

# trigger function
def button_clicked():
    my_label["text"] = my_entry.get()
    # above is the same as my_label.config(text=...)

# create a button and pack it
# command attaches a function to button's on click evenet listener
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=1)

# window will loop
window.mainloop()
