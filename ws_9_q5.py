import tkinter as tk

root = tk.Tk()
root.geometry("500x400")

canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack()

# BODY
canvas.create_rectangle(200, 150, 300, 250, fill="blue")

# RECTANGLE HEAD
canvas.create_rectangle(220, 100, 280, 150, fill="blue")

# LEFT EYE 
canvas.create_oval(235, 115, 245, 125, fill="black")

# RIGHT EYE 
canvas.create_oval(255, 115, 265, 125, fill="black")

# WHEELS
canvas.create_oval(210, 250, 240, 280, fill="black")    # left wheel
canvas.create_oval(260, 250, 290, 280, fill="black")    # right wheel

root.mainloop()
