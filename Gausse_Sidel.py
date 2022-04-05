from math import *
import numpy as np
import matplotlib as plt
from scipy import stats
from numpy.linalg import inv
from numpy.linalg import pinv
from numpy.linalg import norm


def GS(A, b, X0, eps, iterMax):
    M = np.tril(A)
    N = M - A
    Bgs = np.dot(inv(M), N)
    Cgs = np.dot(inv(M), b)
    X1 = np.dot(Bgs, X0) + Cgs
    K = 1
    while norm(X1 - X0) > eps * norm(X1) and K < iterMax:
        X0 = X1
        X1 = np.dot(Bgs, X0) + Cgs
        K += 1
    return X1, K


A = [[64, 24, 1, 8, 15], [23, 50, 7, 14, 16], [4, 6, 58, 20, 22], [10, 12, 19, 66, 3], [11, 18, 25, 2, 54]]
b = [[219], [359], [444], [319], [309]]
X0 = [[0], [1], [1], [1], [2]]
eps = 10 ** (-6)
iterMax = 100

[X, K] = GS(A, b, X0, eps, iterMax)
print('solution = ', X)
print('nbr iter = ', K)
