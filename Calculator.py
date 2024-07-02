import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import roman
import customtkinter as ct

''' to do: 
local variable names go a-z
fix the fuckass numbers method, clarity over optimization
clean code
'''

window = ct.CTk() 
window.title ( "Calculator" ) 
window.config (bg="gray10")
answer= tk.StringVar(window, "")
display = ct.CTkLabel ( window, textvariable=answer, text_color="white", bg_color="transparent") 
display.grid(row=0, column=0, columnspan=3)
# Warnings because I am NOT making my own roman numeral program to handle decimals!
warnings=mb.showwarning(title="Warnings", message="Hey! This calculator is... not perfect! You may be better off with something else. There are no decimals and limited range of numbers. Enjoy!")

# Sections of the program
button_column=tk.Label(master=window, bg="gray10")
button_column.grid(row=0, column=3, rowspan=5)

number_box=tk.Label(master=window, bg="gray10")
number_box.grid(row=2, column=0, rowspan=4, columnspan=3)



# Methods to, well, do the 4 basic operations on the numbers selected! Does not support multiple operations at a time.

def add (x, y) :
    x=int(x)
    y=int(y)
    return x + y

def sub (x, y) :
    x=int(x)
    y=int(y)
    return x - y

def div (x, y) :
    x=int(x)
    y=int(y)
    if (y==0):
        y=1
    return x // y

def mult (x, y) :
    x=int(x)
    y=int(y)
    return x * y

# Selects operation and prints the result of that operation. Far from optimized.
def enter (x,y,z):
    global held_num
    global previous_num
    # who up harding they code (FIX THIS!!!!)
    if (z=="+"):
        answer.set(roman.toRoman(add(x, y)))
        held_num=str(roman.fromRoman(answer.get()))
    elif (z=="-"):
        answer.set(roman.toRoman(sub(x, y)))
        held_num=str(roman.fromRoman(answer.get()))
    elif (z=="*"):
        answer.set(roman.toRoman(mult(x, y)))
        held_num=str(roman.fromRoman(answer.get()))
    elif (z=="/"):
        answer.set(roman.toRoman(div(x, y)))
        held_num=str(roman.fromRoman(answer.get()))
    else:
        answer.set(roman.toRoman(0))
    
# sinful little beasts that hold the information.
held_num=0
previous_num=0
operation=""

def storage (a) :
    global held_num
    global operation
    global previous_num
    if not (isinstance(a, int)):
        operation=a
        previous_num=held_num
        held_num=0
        answer.set(a)
    else:
        a=(held_num*10)+a
        held_num=a
        answer.set(roman.toRoman(a))
        print(a)
def clear(_):
    global held_num
    global previous_num
    held_num=previous_num=0
    answer.set(roman.toRoman(0))
def add_buttons():
    # Commenting for ease of seeing which is which
    # 1
    button=ct.CTkButton( master=number_box, text=roman.toRoman(1), command=lambda x=1: storage(x))
    button.grid(row=0, column=0)
    # 2
    button=ct.CTkButton( master=number_box, text=roman.toRoman(2), command=lambda x=2: storage(x))
    button.grid(row=0, column=1)
    # 3
    button=ct.CTkButton( master=number_box, text=roman.toRoman(3), command=lambda x=3: storage(x))
    button.grid(row=0, column=2)
    # 4
    button=ct.CTkButton( master=number_box, text=roman.toRoman(4), command=lambda x=4: storage(x))
    button.grid(row=1, column=0)
    # 5
    button=ct.CTkButton( master=number_box, text=roman.toRoman(5), command=lambda x=5: storage(x))
    button.grid(row=1, column=1)
    # 6
    button=ct.CTkButton( master=number_box, text=roman.toRoman(6), command=lambda x=6: storage(x))
    button.grid(row=1, column=2)
    # 7
    button=ct.CTkButton( master=number_box, text=roman.toRoman(7), command=lambda x=7: storage(x))
    button.grid(row=2, column=0)
    # 8
    button=ct.CTkButton( master=number_box, text=roman.toRoman(8), command=lambda x=8: storage(x))
    button.grid(row=2, column=1)
    # 9
    button=ct.CTkButton( master=number_box, text=roman.toRoman(9), command=lambda x=9: storage(x))
    button.grid(row=2, column=2)
    # 0
    button=ct.CTkButton( master=number_box, text=roman.toRoman(0), command=lambda x=0: storage(x))
    button.grid(row=4, column=0, columnspan=2, sticky="ew")


    button=ct.CTkButton(master=number_box, text="+", command=lambda a="+": storage(a))
    button.grid(row=4, column=2)
    button=ct.CTkButton(master=button_column, text="-", command=lambda a="-": storage(a))
    button.grid(row=1, column=3)    
    button=ct.CTkButton(master=button_column, text="*", command=lambda a="*": storage(a))
    button.grid(row=2, column=3)    
    button=ct.CTkButton(master=button_column, text="/", command=lambda a="/": storage(a))
    button.grid(row=3, column=3, sticky="w")
    button=ct.CTkButton(master=button_column, text="=", command=lambda a="_": enter (previous_num, held_num, operation))
    button.grid(row=4, column=3)
    button=ct.CTkButton(master=button_column, text="c", command=lambda a=0: clear(a))
    button.grid(row=0, column=3) 
    

add_buttons()
window.mainloop (  ) 
