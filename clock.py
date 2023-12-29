import tkinter as tk
from time import strftime

def update_clock():
    '''Update the clock label with the current time'''
    current_time = strftime("%H:%M:%S")  # Getting current time
    clock_label.config(text=current_time)  # Updating label text
    clock_label.after(1000, update_clock)  # Scheduling next update after 1 second

app = tk.Tk()
app.title("Python Clock")

clock_label = tk.Label(app, font=("Helvetica", 48))
clock_label.pack()

update_clock()  # Starting the clock update function
app.mainloop()