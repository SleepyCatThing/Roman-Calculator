import tkinter as tk

# Initializing my silly stuff that doesn't need silly operations done to add
window = tk.Tk()
buttons=[]
button_row_1 = tk.Frame(width=100, height=10)
button_row_3 = tk.Frame(width=100, height=20)
button_row_2 = tk.Frame(width=100, height=100)

# Big, messy and unoptimal loop to make a 9 button display. Each inner loop adds a row. 
for i in range (9):

    if i in range (3):
        button_adder= tk.Button(
        text=i+1,
        master=button_row_1,
        width=5,
        height=5
        )

    elif i in range (6):
        button_adder= tk.Button(
        text=i+1,
        master=button_row_2,
        width=5,
        height=5
        )

    elif i in range (9):
        button_adder= tk.Button(
        text=i+1,
        master=button_row_3,
        width=5,
        height=5
        )

    buttons.append(button_adder)

for j in range (9):
    buttons[j].pack(side=tk.LEFT)

# this doesn't need a comment but i think itd be funny
button_row_3.pack(side=tk.BOTTOM)
button_row_2.pack(side=tk.BOTTOM)
button_row_1.pack(side=tk.BOTTOM)

window.mainloop()