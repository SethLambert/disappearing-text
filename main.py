import datetime as dt
import time
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("800x1000")
root.title("Disappearing Ink")

timer = 0

def save():
   text_file = open("work.txt", "w")
   text_file.write(entry.get(1.0, 'end'))
   text_file.close()
   
def clear_box():
    entry.delete(1.0, "end")

def reset_timer():
    global timer
    timer = 0

#header
header = tk.Label(root, text = "Disappearing Ink", font=('calibre', 36, 'bold'))


#text entry
var = tk.StringVar()
entry = tk.Text(root, font=('calibre', 12, 'normal'))
directions = tk.Label(root, text = f'Text will dissapear in {10 - timer} seconds.', font=('calibre', 12, 'normal'))
save_button = tk.Button(root, text ="Save", command = save)

#grid
header.grid(row=0,column=0, columnspan = 2, padx=10,pady=10)
entry.grid(row=1, column=0, padx=10,pady=10, columnspan = 2)
directions.grid(row=2, column=0, padx=10,pady=10)
save_button.grid(row=2, column=1, padx=10,pady=10)

run_game = True
counter = 0
characters = 0
while run_game:
    root.update()
    #check for writing progress:
    new_characters = len(entry.get(1.0, 'end-1c'))
    if new_characters > characters:
        reset_timer()
        characters = new_characters
        
    time.sleep(.01)
    counter += 1
    if counter % 100 == 0:
        if timer == 10:
            clear_box()
            reset_timer()
        else:
            timer += 1
    directions.config(text=f'Text will dissapear in {10 - timer} seconds.')


root.mainloop()