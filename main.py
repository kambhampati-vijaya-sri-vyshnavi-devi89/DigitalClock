from tkinter import *
from time import strftime

# Create UI window
root = Tk()
root.title("Digital Clock")

# Function to update time
def clock():
    tick = strftime("%H:%M:%S %p")
    label.config(text=tick)
    label.after(1000, clock)

# Clock label styling
label = Label(root, font=("segoe", 60), fg="yellow", bg="black")
label.pack(anchor="center")

# Start clock
clock()
mainloop()
