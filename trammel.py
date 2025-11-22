
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation



a=30
b=15
s = -a*b / (a + b)
frames=400
theta=np.linspace(0,2*np.pi,frames)

x_slider=a*np.cos(theta)
y_slider=b*np.sin(theta)

x_tracer=a*np.cos(theta) + s*np.cos(theta)
y_tracer=b*np.sin(theta) + s*np.sin(theta)

fig , ax = plt.subplots(figsize=(7,7))
ax.set_aspect('equal','box')
ax.set_xlim(-a+0.5,a+0.5)
ax.set_ylim(-b+0.5,b+0.5)
ax.set_xlabel("X-axis (slider path)")
ax.set_ylabel("Y-axis (slider path)")
ax.set_title("Elliptical Trammel (2D Animation)") 

ax.axhline(0,color='gray',linestyle='--',linewidth=1)
ax.axvline(0,color='gray',linestyle='--',linewidth=1)

rod_line,= ax.plot([],[],'k-',linewidth=2)
slider_x,=ax.plot([],[],'s',color='blue',markersize='8')
slider_y, = ax.plot([], [], 's', color='red', markersize=8)
tracer, = ax.plot([], [], 'o', color='green', markersize=8)
path, = ax.plot([], [], color='green', alpha=0.6)

def start_frame():
    rod_line.set_data([],[])
    slider_x.set_data([], [])
    slider_y.set_data([], [])
    tracer.set_data([], [])
    path.set_data([], [])
    return rod_line, slider_x, slider_y, tracer, path

def update(i):
    x_s=x_slider[i]
    y_s = y_slider[i]
    x_t = x_tracer[i]
    y_t = y_tracer[i]

    rod_line.set_data([x_s,0],[0,y_s])
    slider_x.set_data([x_s], [0])
    slider_y.set_data([0], [y_s])
    tracer.set_data([x_t], [y_t])
    path.set_data(x_tracer[:i+1], y_tracer[:i+1])

    return rod_line, slider_x, slider_y, tracer, path

ani=animation.FuncAnimation(fig,update,frames=frames,init_func=start_frame,blit=True,interval=25)

plt.show()
