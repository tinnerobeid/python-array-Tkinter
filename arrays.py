from tkinter import *
from tkinter import simpledialog


def create_array():
    try:
        num = int(entry.get())
        my_array = []
        for i in range(num):
            value = simpledialog.askinteger("Input", f"Enter value {i + 1}:")  # opens another window to ask user to
            # enter nums
            my_array.append(value)
        result_label.config(text=f"The created array is: {my_array}")  # shows results
    except ValueError:
        result_label.config(text="Please enter a valid number of values.")


window = Tk()
window.geometry("400x300")
window.title("myArrays")

num_label = Label(window, text="Enter the number of values: ")
num_label.place(x=22, y=50)

entry = Entry(window)
entry.place(x=180, y=50)

create_button = Button(window, text="Create Array", command=create_array)
create_button.place(x=150, y=80)

result_label = Label(window, text="")
result_label.pack()

window.mainloop()
