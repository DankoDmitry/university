import random
import numpy as np


n = int(input('input lenght'))

arr = np.random.randint(0, 100, n)

print (arr)
print (max(arr), min(arr), arr.mean())




