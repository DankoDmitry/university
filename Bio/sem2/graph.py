import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, 0.1)
first = x**2
second = x**3

#plt.plot(x, first)
#plt.plot(x, second, color='red', linestyle='dotted')

#plt.show()


figure, axis = plt.subplots(2)

axis[0].plot(x, first)

axis[1].plot(x, second, color='red', linestyle='dotted')

plt.show()

