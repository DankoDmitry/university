import numpy as np


W=6
arr = [10,50,1,4,0.36,0.84,1]

def A(w, arr):
    Z_1 = np.sqrt((arr[0]*w)**2 + arr[1]**2)
    Z_2 = np.sqrt((arr[2]*w)**2 + arr[3]**2)
    Z_3 = np.sqrt((-arr[4] * w**2 + arr[6])**2 + (arr[5] * w)**2)

    return round (Z_1/(Z_2*Z_3), 3)

def Fi(w, arr):
    arctg_1 = np.arctan(arr[0]*w/arr[1])
    arctg_2 = np.arctan(arr[2]*w/arr[3])
    arctg_3 = np.arctan(arr[5]*w/(-arr[4]*w**2+arr[6]))

    return round (arctg_1 - arctg_2 - arctg_3, 3)

def Answer(w, arr):
    P=0.5*A(0.5, arr)

    return (f"y = {P}*sin({w}t - {Fi(0.5, arr)})")

print()
print(f"A({W}) = {A(0.5, arr)}")
print(f"fi({W}) = {Fi(0.5, arr)}")
print(Answer(0.5, arr))
print()