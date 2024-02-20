import numpy as np
import matplotlib.pyplot as plt

def Messure(A, B):
    N = len(B)
    s = 0
    for i in range(N):
        s = s + (abs( A[i] - B[i]))**2
    return np.sqrt(s)

def X_1(A, b, x, i):
    s = 0
    for p in range(len(b)):
        if p != i: s += A[i, p]*x[p]
    return (b[i] - s)/A[i,i]

def Simp(A, b, E, P):
    if np.linalg.det(A) == 0: return ("error")

    N = len(b)
    X = np.zeros(N)

    k = 0
    while(Messure(X, P) > E):
        Y = np.zeros(N)
        for i in range(N):
            Y[i] = X_1(A, b, X, i)
        X = Y
        k+=1
    return ("simp: ", X, k)    

A = np.zeros((2,2))
while np.linalg.det(A) == 0:
    A = np.random.randint (1, 20, (5, 5))
b = np.random.randint (0, 20, 5)
E = 0.001
P = np.linalg.solve (A, b)
print(A, b, P)

print(Simp(A, b, E, P))