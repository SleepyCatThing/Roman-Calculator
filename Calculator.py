import tkinter as tk
window = tk.Tk()
buttons=[]
frame_1 = tk.Frame(width=100, height=10)
frame_3 = tk.Frame(width=100, height=20)
frame_2 = tk.Frame(width=100, height=100)
for btn in range (9):
    if btn in range (3):
        btnx= tk.Button(
        text=btn+1,
        master=frame_1,
        width=5,
        height=5
        )
    elif btn in range (6):
        btnx= tk.Button(
        text=btn+1,
        master=frame_2,
        width=5,
        height=5
        )
    elif btn in range (9):
        btnx= tk.Button(
        text=btn+1,
        master=frame_3,
        width=5,
        height=5
        )
    buttons.append(btnx)
for btns in range (9):
    burger = buttons[btns]
    burger.pack(side=tk.LEFT)


frame_3.pack(side=tk.BOTTOM)
frame_2.pack(side=tk.BOTTOM)
frame_1.pack(side=tk.BOTTOM)




window.mainloop()