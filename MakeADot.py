from matplotlib import pyplot as plt
import numpy as np
from matplotlib import animation
import random

fig, ax = plt.subplots()

# Part : Set X, Y
x = []
y = []
xpoint = 0
ypoint = 0

# Part : Condition
while (xpoint != 5 or ypoint != 5):
    if (xpoint != 0 and xpoint != 10 and ypoint != 0 and ypoint != 10):
        xpoint = xpoint+(random.randrange(-1, 2))
        ypoint = ypoint+(random.randrange(-1, 2))
        x.append(xpoint)
        y.append(ypoint)
    elif (xpoint == 0 and ypoint == 0):
        xpoint = xpoint+1
        ypoint = ypoint+1
        x.append(xpoint)
        y.append(ypoint)
    elif (xpoint == 10 and ypoint == 10):
        xpoint = xpoint-1
        ypoint = ypoint-1
        x.append(xpoint)
        y.append(ypoint)
    elif xpoint == 0:
        xpoint = xpoint+1
        ypoint = ypoint+(random.randrange(-1, 2))
        x.append(xpoint)
        y.append(ypoint)
    elif ypoint == 0:
        xpoint = xpoint+(random.randrange(-1, 2))
        ypoint = ypoint+1
        x.append(xpoint)
        y.append(ypoint)
    elif xpoint == 10:
        xpoint = xpoint-1
        ypoint = ypoint+(random.randrange(-1, 2))
        x.append(xpoint)
        y.append(ypoint)
    elif ypoint == 10:
        xpoint = xpoint+(random.randrange(-1, 2))
        ypoint = ypoint-1
        x.append(xpoint)
        y.append(ypoint)
    else:
        print("exceptions!")
        print(str(xpoint)+" and "+str(ypoint))

# Part : ax
point, = ax.plot([x[0]], [y[0]], 'ro')
# ax.legend()
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])

def update_point(n, x, y, point):
    point.set_data(np.array([x[n], y[n]]))
    return point

# Operation
ani=animation.FuncAnimation(fig=fig, func=update_point, frames=len(x), fargs=(x, y, point), repeat=False)

print(x)
print(y)
plt.show()
