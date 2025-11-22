import tkinter as tk
root=tk.Tk()
canvas=tk.Canvas(root,width=500,height=400)
canvas.pack()

canvas.create_rectangle(100,100,200,200,fill="black")

root.mainloop()