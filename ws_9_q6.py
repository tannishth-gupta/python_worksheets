import tkinter as tk

root = tk.Tk()
root.geometry("500x450")


canvas = tk.Canvas(root, width=500, height=350, bg="white")
canvas.pack()


x, y = 250, 175  
r = 10

robot = canvas.create_oval(x-r, y-r, x+r, y+r, fill="red")


def move_up():
    canvas.move(robot, 0, -10)

def move_down():
    canvas.move(robot, 0, 10)

def move_left():
    canvas.move(robot, -10, 0)

def move_right():
    canvas.move(robot, 10, 0)


btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Up", width=10, command=move_up).grid(row=0, column=1)
tk.Button(btn_frame, text="Left", width=10, command=move_left).grid(row=1, column=0)
tk.Button(btn_frame, text="Down", width=10, command=move_down).grid(row=1, column=1)
tk.Button(btn_frame, text="Right", width=10, command=move_right).grid(row=1, column=2)

root.mainloop()
