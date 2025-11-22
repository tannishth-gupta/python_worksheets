import tkinter as tk

root = tk.Tk()
root.geometry("500x400")

canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack()


x, y = 50, 200     
target_x = 450
r = 10             
velocity = 3       


robot = canvas.create_oval(x-r, y-r, x+r, y+r, fill="red")


def move_robot():
    global x   

    if x < target_x:
        canvas.move(robot, velocity, 0)   # move horizontally
        x += velocity                     # update internal position
        root.after(20, move_robot)        # schedule next frame

    else:
        print("Robot has reached the target!")


move_robot()

root.mainloop()
