from math import *

import a as a
from scipy import stats
import matplotlib as plt
import numpy as np


def luDecomposition(A):
    [n, n] = np.shape(A)
    comp = 0
    for j in range(n - 1):
        for i in range(j + 1, n):
            comp += 1
            A[i][j] = A[i][j] / A[j][j]
            for k in range(j + 1, n):
                A[i][k] = A[i][k] - A[i][j] * A[j][k]
                comp += 2
    U = np.triu(A)
    L = np.identity(n) + np.tril(A, -1)
    return [L, U, comp]


def vander(n):
    A = np.zeros(n)
    for i in range(n):
        for j in range(n):
            A[i][j] = (i + j) ^ j
    return A


C = np.zeros((2, 6))
for k in range(1, 7):
    C[0, k] = np.log(10 * k)
    A = vander(k)
    [L, U, comp] = luDecomposition(A)
    C[1, k] = log(comp)

[a, b, r, p, std, err] = stats.linregress(tab[0,:], tab[1,:])


A = np.array([[-4, -1, -2],
              [-4, 12, 3],
              [-4, -2, 18]])
[L, U] = luDecomposition(A)
print('L=', L)
print('U=', U)
