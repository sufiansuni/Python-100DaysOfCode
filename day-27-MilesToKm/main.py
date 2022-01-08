import tkinter

# window
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=240, height=90)
window.config(padx=36, pady=16)

# miles_input
miles_input = tkinter.Entry()
miles_input.grid(column=1, row=0)

# miles_label
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

# is_equal_to_label
is_equal_to_label = tkinter.Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

# km_output_label
km_output = 0
km_output_label = tkinter.Label(text=str(km_output))
km_output_label.grid(column=1, row=1)

# km_label
km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

# calculate function
def calculate():
    km_output = int(miles_input.get())
    km_output_label["text"] = str(km_output * 1.609344)

# calculate button
button = tkinter.Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

# program loop
window.mainloop()
