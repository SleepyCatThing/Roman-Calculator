import tkinter as tk
from tkinter import ttk
import roman

window = tk.Tk() 
window.title ( "Calculator" ) 
operation=""
answer= tk.StringVar(window, "")
answer_display = ttk.Label ( window, textvariable=answer ) 

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
    z=int(z)
    # who up harding they code
    if (z==0):
        answer.set(roman.toRoman(add(x, y)))
        held_num=str(roman.fromRoman(answer.get()))
    elif (z==1):
        answer.set(roman.toRoman(sub(x, y)))
        held_num=str(roman.fromRoman(answer.get()))
    elif (z==2):
        answer.set(roman.toRoman(mult(x, y)))
        held_num=str(roman.fromRoman(answer.get()))
    elif (z==3):
        answer.set(roman.toRoman(div(x, y)))
        held_num=str(roman.fromRoman(answer.get()))
    else:
        answer.set(roman.toRoman(0))
    
# sinful little beasts that hold the information. 
held_num=0
previous_num=0
op=""
operations=[add, sub, mult, div, enter]
symbolic_operations=["+", "-", "*", "/", "="]

def storage (a) :
    global held_num
    global op
    global previous_num
    if not (isinstance(a, int)):
        g=int(a)
        op=g
        previous_num=held_num
        held_num=0
        f=symbolic_operations[int(a)]
        answer.set(f)
    else:
        a+=1
        a=(held_num*10)+a
        held_num=a
        answer.set(roman.toRoman(a))
        print(a)
def clear(a):
    global held_num
    global previous_num
    held_num=a
    held_num=0
    previous_num=0
    answer.set(roman.toRoman(0))

# This is where the magic happens! A wacky little display button :3

display=ttk.Label(window, textvariable=answer)    
display.grid(row=0, column=0, columnspan=4)
    
def add_buttons ( ) :
    val=0
    for i in range(3):
        for j in range(3):
            button=tk.Button(
            text=roman.toRoman(val+1),    
            command=lambda i=val:storage(i),   
            )
            button.grid(row=i+1,column=j)
            
            val += 1
    button=tk.Button(
        text=roman.toRoman(0),
        command=lambda a=0: storage(a)
    )
    button.grid(row=4, column=0)
    button=tk.Button(
    text="+",
    command=lambda a="0": storage(a)
    )
    button.grid(row=4, column=2)
    button=tk.Button(
    text="-",
    command=lambda a="1": storage(a)
    )
    button.grid(row=1, column=3)    
    button=tk.Button(
    text="*",
    command=lambda a="2": storage(a)
    )
    button.grid(row=2, column=3)    
    button=tk.Button(
    text="/",
    command=lambda a="3": storage(a)
    )
    button.grid(row=3, column=3, sticky="w")
    button=tk.Button(
    text="=",
    command=lambda a="4": enter (previous_num, held_num, op)
    )
    button.grid(row=4, column=3)
    button=tk.Button(
        text="c",
        command=lambda a=0: clear(a)
    )
    button.grid(row=0, column=3) 
    button=tk.Button(
    text=".",
    command=lambda a="4": enter (previous_num, held_num, op)
    )
    button.grid(row=4, column=1)  
    




add_buttons()
window.mainloop (  ) 
