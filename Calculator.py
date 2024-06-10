import tkinter as tk

# Initializing my silly stuff that doesn't need silly operations done to add
window = tk.Tk()
window.title("WAWAO")

# initializing operations!
buttons=[]
button_row_0 = tk.Frame()
button_row_1 = tk.Frame(width=100, height=10)
button_row_2 = tk.Frame(width=100, height=10)
button_row_3 = tk.Frame(width=100, height=10)
button_row_4 = tk.Frame(width=100, height=10)
row = [button_row_1, button_row_2, button_row_3, button_row_4]
# UNFUCK THIS
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def div(x, y):
    return x / y
def mult(x, y):
    return x * y
def enter(num1, num2, operation):
    num3=operation(num1, num2)
    print(num3)
symbolic_operations = ["+","-","/","*","="]
operations = [add, sub, div, mult, enter]

# creating display for clear and math display

# creating display for numbers
j=0
for i in range (9):
    if i == 3:
        j=j+1
    if i == 6:
        j=j+1
    btn = tk.Button(
            text=i+1,
            command=i+1,
            master=row[j],
        )
    btn.pack(side=tk.LEFT)
    # UNFUCK THIS
    # UNFUCK THIS
    # UNFUCK THIS
btn = tk.Button(
            text=0,
            command=0,
            master=row[3],
        )
btn.pack(side=tk.LEFT)
# creating display for symbols
for i in range (4):
    btn = tk.Button(
        text=symbolic_operations[i],
        command=operations[i],
        master=row[i],
    )
    btn.pack(side=tk.LEFT)
    # UNFUCK THIS
    # UNFUCK THIS
    # UNFUCK THIS
btn = tk.Button(
text=symbolic_operations[4],
command=operations[4],
master=row[3],
)
btn.pack(side=tk.LEFT)
button_row_4.pack(side=tk.BOTTOM)
button_row_3.pack(side=tk.BOTTOM)
button_row_2.pack(side=tk.BOTTOM)
button_row_1.pack(side=tk.BOTTOM)



window.mainloop()
# TO DO:
# basic python learning
# Make buttons again
# execute button_press on tk.Button() click or smth 
# Make working top display
# Convert top display to roman numerals
# figure out what the fuck im doing