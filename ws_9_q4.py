import tkinter as tk
root=tk.Tk()
root.geometry('500x400')
canvas=tk.Canvas(root,width=500,height=400)
canvas.pack()
x,y=20,200
r=5
dot=canvas.create_oval(x-r,y-r,x+5,y+5,fill="red")
dx=3 
dy=0
def animate():
    canvas.move(dot,dx,dy)
    root.after(20,animate)

animate()
root.mainloop()