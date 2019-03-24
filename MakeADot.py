from matplotlib import pyplot as plt
import numpy as np
from matplotlib import animation

# Example
# fig, ax = plt.subplots()
# xdata, ydata = [], []
# ln, = plt.plot([], [], 'ro')
# 
# def init():
#     ax.set_xlim(0, 2*np.pi)
#     ax.set_ylim(-1, 1)
#     return ln,
# 
# def update(frame):
#     xdata.append(frame)
#     ydata.append(np.sin(frame))
#     ln.set_data(xdata, ydata)
#     return ln,
# 
# ani = animation.FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
#                     init_func=init, blit=True)
# plt.show()

fig, ax = plt.subplots()
x = np.random.random(50)
x = np.cumsum(x, dtype=float)
y = np.random.random(50)
y = np.cumsum(y, dtype=float)

point, = ax.plot([x[0]], [y[0]], 'ro')
ax.legend()
ax.set_xlim([0, 50])
ax.set_ylim([0, 50])

def update_point(n, x, y, point):
    point.set_data(np.array([x[n], y[n]]))
    return point

ani=animation.FuncAnimation(fig, update_point, 99, fargs=(x, y, point))

plt.show()
