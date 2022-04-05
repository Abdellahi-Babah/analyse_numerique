from math import *
import numpy as np
import matplotlib as plt


def triInf(A , b):
    n = len(b)
    x = np.zeros(n)
    x[0] = b[0] / A[0][0]
    for i in range(1, n):
        x[i] = b[i]
        for j in range(i):
            x[i] = x[i] - A[i][j] * x[j]
        x[i] = x[i] / A[i][i]
    return x


def triSup(A, b):
    n = len(b)
    x = np.zeros(n)
    x[n - 1] = b[n - 1] / A[n - 1][n - 1]
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] = x[i] - A[i][j] * x[j]
        x[i] = x[i] / A[i][i]
    return x


A = [[4, 1, 1], [0, 3, 1], [0, 0, 3]]
A = np.asmatrix(A)
b = [1, 5, 6]
P = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]
P = np.asmatrix(P)
temp = np.multiply(P,b)
print(temp)
U = [[4, 1, 1], [0, 3, 1], [0, 0, 3]]
U = np.asmatrix(U)
L = [[1, 0, 0], [0, 1, 0], [0.5, 0.5, 1]]
L = np.asmatrix(L)



x = triInf(A, b)
print(x)
