import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 10, 0, 10])

for i in np.random.random(10)*10:
    y = np.random.random()*10
    plt.scatter(i, y)
    plt.pause(0.05)

plt.show()