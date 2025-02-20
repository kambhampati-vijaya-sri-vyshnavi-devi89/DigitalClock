

# Digital Clock using Tkinter  

## Description  
This project is a **simple digital clock** built using Python's **Tkinter** GUI library. It displays the **current time** in an easy-to-read format and updates every second.  

## Features  
✅ Real-time **digital clock**  
✅ Uses **Tkinter** for GUI  
✅ Updates automatically every second  

## Installation  
Ensure you have Python installed. Tkinter comes pre-installed with Python, but if needed, install it using:  
```sh
pip install tk
```

## Usage  

### 1. **Run the Script**  
Save the following code as `digital_clock.py` and execute it:  
```python
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
```

### 2. **Run the Script**  
```sh
python digital_clock.py
```
The **clock** will appear and update in real-time!  

## Notes  
- The **`strftime("%H:%M:%S %p")`** function formats time as `HH:MM:SS AM/PM`.  
- The **`label.after(1000, clock)`** ensures the clock updates every second.  
- The UI can be customized by modifying font, color, and alignment.  

