import tkinter as tk
from tkinter import ttk

window = tk.Tk() 
window.title ( "Calculator" ) 

button_row_0 = ttk.Frame ( width=100, height=10 ) 
button_row_1 = ttk.Frame ( width=100, height=10 ) 
button_row_2 = ttk.Frame ( width=100, height=10 ) 
button_row_3 = ttk.Frame ( width=100, height=10 ) 
button_row_4 = ttk.Frame ( width=100, height=10 ) 

row = [button_row_1, button_row_2, button_row_3, button_row_4]
symbolic_operations = ["+", "-", "/", "*", "="]
previous_number_held = tk.StringVar(window, "0") 
number_held = tk.StringVar(window, "0") 
answer= tk.StringVar(window, "")
operation_held = [False]
answer_display = ttk.Label ( window, textvariable=answer ) 

# methods for the buttons 

def add () :
    
    answer.set(int(previous_number_held.get()) + int(number_held.get())) 

def sub () :
    
    answer.set(int(previous_number_held.get()) - int(number_held.get()))

def div () :
    global answer
    if  ( number_held.get() == "0" ) :
        answer="nah, i'd error"
    
    answer.set( int(previous_number_held.get()) / int(number_held.get()))

def mult ( previous_number_held, number_held ) :
    
    answer.set( int(previous_number_held.get()) * int(number_held.get()))

operations = [add, mult, div, sub]

def storage ( a ) :
    global previous_number_held
    global number_held
    global operation_held
    
    if  ( isinstance ( a, int )  ) :
        if number_held.get()!='':
            number_held.set((int(number_held.get())*10)+a)
        else:
            number_held.set(a)
        answer.set(number_held.get())
    
    else:
        previous_number_held.set(number_held.get())
        operation_held[0]=a
        number_held.set("")

    
def enter () :
    global previous_number_held
    if (number_held.get()!="" and previous_number_held.get()!=""):
        result = operation_held [0] ( previous_number_held, number_held )
        previous_number_held.set ( result ) 

def add_buttons ( ) :
    j=0
    for k in range  ( 10 ) :
        
        if  ( k == 0 ) :
            j = 3

        btn = ttk.Button ( 
            
            text = k,
            command = storage ( k ) ,
            master = row[j],
             ) 
        
        btn.pack ( side=tk.LEFT ) 
        
        if  (  ( k ) % 3 ==0 ) :
            j = j + 1
        
        if  ( k == 0 ) :
            j = 0
        
        btn.pack ( side=tk.LEFT ) 
add_buttons ( )
for h in range  ( 4 ) :
        
    btn = ttk.Button ( 
            
        text=symbolic_operations[h],
        command=storage ( operations[h] ) ,
        master=row[h],
        ) 
        
    btn.pack ( side=tk.LEFT ) 
        
    if  ( h == 3 ) :
            
        btn = ttk.Button ( 
        text=symbolic_operations[4],
        command=enter(),
        master=row[h],
        ) 
            
        btn.pack ( side=tk.LEFT ) 

def pack_buttons (  ) :
    
    button_row_4.pack ( side = tk.BOTTOM ) 
    
    button_row_3.pack ( side = tk.BOTTOM ) 
    
    button_row_2.pack ( side = tk.BOTTOM ) 
    
    button_row_1.pack ( side = tk.BOTTOM ) 
    
    button_row_0.pack ( side = tk.BOTTOM )

 

pack_buttons (  ) 
answer_display.pack()
window.mainloop (  ) 
