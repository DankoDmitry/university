import numpy as np
import pprint

a = np.arange(1,11)

arr = np.array([[i for i in a],
		[i*i for i in a],
		[i**3 for i in a]])
arr = np.transpose(arr)

text = str(arr).replace('[', '')
text = text.replace(']', '')
print ('', text)
