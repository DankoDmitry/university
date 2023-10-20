import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-100, 100, 0.1)
first = x**2
second = x**3

plt.plot(x, np.sin(x)/x)
plt.show()

