import tkinter as tk

# Initializing my silly stuff that doesn't need silly operations done to add
window = tk.Tk()
window.title("Calculator")

# initializing operations!
buttons=[]
button_row_0 = tk.Frame()
button_row_1 = tk.Frame(width=100, height=10)
button_row_2 = tk.Frame(width=100, height=10)
button_row_3 = tk.Frame(width=100, height=10)
button_row_4 = tk.Frame(width=100, height=10)
row = [button_row_1, button_row_2, button_row_3, button_row_4]
symbolic_operations = ["+", "-", "/", "*", "="]
# UNFUCK THIS
def val(x):
    storage(x)

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def div(x, y):
    return x / y

def mult(x, y):
    return x * y

hold=[1]
digit_held=0
def storage(a):
    global digit_held
    if (hold[digit_held] is int):
        hold[digit_held]=hold[digit_held]*10
        hold[digit_held]=hold[digit_held]+a
        print(hold[digit_held])
    else:
        hold.append(a)
        print(hold[digit_held])
        digit_held=digit_held+1
    
    
def enter():
    hold[0](hold[1],hold[2])

operations = [add, sub, div, mult, enter]

def add_buttons(j):
    for i in range (10):
        if (i==0):
            j=3
        btn = tk.Button(
            text=i,
            # unfuck
            command=val(i),
            master=row[j],
            )
        btn.pack(side=tk.LEFT)
        if ((i)%3==0):
            j=j+1
        if (i==0):
            j=0
        btn.pack(side=tk.LEFT)

    for i in range (4):
        btn = tk.Button(
            text=symbolic_operations[i],
            command=storage(operations[i]),
            master=row[i],
        )
        btn.pack(side=tk.LEFT)
        if (i==3):
            btn = tk.Button(
            text=symbolic_operations[i+1],
            command=operations[i+1],
            master=row[i],
            )
            btn.pack(side=tk.LEFT)

def pack_buttons():
    button_row_4.pack(side=tk.BOTTOM)
    button_row_3.pack(side=tk.BOTTOM)
    button_row_2.pack(side=tk.BOTTOM)
    button_row_1.pack(side=tk.BOTTOM)

def display(value):
    show=tk.frame(
        text=value
    )
    show.Pack(side=tk.TOP)



add_buttons(0)
pack_buttons()

window.mainloop()
