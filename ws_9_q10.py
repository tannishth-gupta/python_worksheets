import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=500, bg="white")
canvas.pack()

x, y, r = 300, 250, 10
robot = canvas.create_oval(x-r, y-r, x+r, y+r, fill="red")

prev_x, prev_y = x, y

def move(dx, dy):
    global prev_x, prev_y
    canvas.move(robot, dx, dy)
    x1, y1, x2, y2 = canvas.coords(robot)
    cx, cy = (x1+x2)/2, (y1+y2)/2
    canvas.create_line(prev_x, prev_y, cx, cy, fill="blue")
    prev_x, prev_y = cx, cy

def up(event): move(0,-5)
def down(event): move(0,5)
def left(event): move(-5,0)
def right(event): move(5,0)

root.bind("<Up>", up)
root.bind("<Down>", down)
root.bind("<Left>", left)
root.bind("<Right>", right)

def reset():
    canvas.delete("all")
    global robot, prev_x, prev_y
    robot = canvas.create_oval(300-r,250-r,300+r,250+r,fill="red")
    prev_x, prev_y = 300,250

tk.Button(root, text="RESET", command=reset).pack()

root.mainloop()
