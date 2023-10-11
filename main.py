from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=70, pady=50)

# Label 1

miles = Label(text="Miles")
miles.grid(column=2, row=0)

# Label 2

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

# Label 3

km = Label(text="Km")
km.grid(column=2, row=1)

# Label 4

dynamic_label = Label(text="0")
dynamic_label.grid(column=1, row=1)

# Entry

number_of_miles = Entry(width=10)
number_of_miles.insert(END, string="0")
number_of_miles.grid(column=1, row=0)


def button_clicked():
    miles_entry = number_of_miles.get()
    total = int(miles_entry) * 1.6
    dynamic_label.config(text=total)


# Button function that changes the dynamic label to represent the solution of the conversion must go after entry and before button

button_clicked()

calculate_button = Button(text="Calculate", command=button_clicked)
calculate_button.grid(column=1, row=2)


window.mainloop()
