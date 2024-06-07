import tkinter as tk

# Initializing my silly stuff that doesn't need silly operations done to add
window = tk.Tk()
buttons=[]
button_row_1 = tk.Frame(width=100, height=10)
button_row_3 = tk.Frame(width=100, height=20)
button_row_2 = tk.Frame(width=100, height=100)

def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def div(x, y):
    return x / y
def mult(x, y):
    return x * y

def button_press(button):
    return(button.int())

window.mainloop()
# TO DO:
# basic python learning
# Make buttons again
# execute button_press on tk.Button() click or smth 
# Make working top display
# Convert top display to roman numerals
# figure out what the fuck im doing