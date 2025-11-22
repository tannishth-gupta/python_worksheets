import tkinter as tk

root = tk.Tk()
root.geometry("500x400")

canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack()


r = 15                      
x, y = 200, 150              


ball = canvas.create_oval(x-r, y-r, x+r, y+r, fill="red")


dx = 3     # horizontal velocity
dy = 2     # vertical velocity


def animate():
    global dx, dy   # allow modification of dx, dy

    
    canvas.move(ball, dx, dy)

    
    x1, y1, x2, y2 = canvas.coords(ball)

    
    if x1 <= 0 or x2 >= 500:
        dx = -dx   # reverse X direction

    
    if y1 <= 0 or y2 >= 400:
        dy = -dy   # reverse Y direction

    
    root.after(20, animate)

animate()  
root.mainloop()
