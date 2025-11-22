import tkinter as tk
root=tk.Tk()
canvas=tk.Canvas(root,width=500,height=400)
canvas.pack()

canvas.create_line(50,300,100,250,200,150,300,200,smooth=False,width=3)

root.mainloop()