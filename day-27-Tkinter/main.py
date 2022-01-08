import tkinter

# creating a tkinter widget
window = tkinter.Tk()

# set title of window
window.title("First Python GUI Program")

# set minimum size of window
window.minsize(width=500, height=300)

# create a label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))

# place label component onto center of program
# packer is a geometry management mechanism
my_label.pack()

# create an input field
my_entry = tkinter.Entry(width=10)
my_entry.pack()

def button_clicked():
    my_label["text"] = my_entry.get()
    # above is the same as my_label.config(text=...)

# create a button and pack it
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()


# window will loop
window.mainloop()
