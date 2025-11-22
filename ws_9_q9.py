import tkinter as tk
import math

root = tk.Tk()
root.geometry("600x500")

canvas = tk.Canvas(root, width=600, height=500, bg="white")
canvas.pack()

A = (150,300)
D = (400,300)

L2 = 120
L3 = 150
L4 = 130

theta = 0

def update():
    global theta
    canvas.delete("all")

    A_x, A_y = A
    B_x = A_x + L2*math.cos(math.radians(theta))
    B_y = A_y - L2*math.sin(math.radians(theta))

    C1_x = B_x
    C1_y = B_y
    C2_x = D[0]
    C2_y = D[1]

    d = math.hypot(C2_x - C1_x, C2_y - C1_y)
    a = (L3**2 - L4**2 + d**2) / (2*d)
    h = math.sqrt(max(L3**2 - a**2, 0))

    x2 = C1_x + a*(C2_x - C1_x)/d
    y2 = C1_y + a*(C2_y - C1_y)/d

    C_x = x2 + h*(C2_y - C1_y)/d
    C_y = y2 - h*(C2_x - C1_x)/d

    canvas.create_line(A_x, A_y, B_x, B_y, width=4, fill="red")
    canvas.create_line(B_x, B_y, C_x, C_y, width=4, fill="blue")
    canvas.create_line(C_x, C_y, D[0], D[1], width=4, fill="green")
    canvas.create_line(A_x, A_y, D[0], D[1], width=4, fill="black")

    canvas.create_oval(A_x-5, A_y-5, A_x+5, A_y+5, fill="black")
    canvas.create_oval(B_x-5, B_y-5, B_x+5, B_y+5, fill="black")
    canvas.create_oval(C_x-5, C_y-5, C_x+5, C_y+5, fill="black")
    canvas.create_oval(D[0]-5, D[1]-5, D[0]+5, D[1]+5, fill="black")

    theta += 2
    root.after(30, update)

update()
root.mainloop()

