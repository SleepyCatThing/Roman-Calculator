import tkinter as tk
window = tk.Tk()
buttons=[]
button_row_1 = tk.Frame(width=100, height=10)
button_row_3 = tk.Frame(width=100, height=20)
button_row_2 = tk.Frame(width=100, height=100)


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
    button_packer = buttons[j]
    button_packer.pack(side=tk.LEFT)


button_row_3.pack(side=tk.BOTTOM)
button_row_2.pack(side=tk.BOTTOM)
button_row_1.pack(side=tk.BOTTOM)




window.mainloop()