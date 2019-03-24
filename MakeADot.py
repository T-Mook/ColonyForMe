import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 1, 0, 1])

for v in np.random.random(5):
    for w in np.random.random(5):
        x = 
        plt.scatter(v, w)
        plt.pause(0.01)

plt.show() # 종료 후에도 노출되도록 하기 위함