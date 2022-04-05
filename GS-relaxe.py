from numpy.linalg import norm
from math import *
import numpy as np
import matplotlib as plt
from scipy import stats
from numpy.linalg import inv
from numpy.linalg import pinv


def GS_relaxe(A, b, X0, eps, iterMax, omega):
    M = np.tril(A)
    N = M - A
    Bgs = np.dot(inv(M), N)
    Cgs = np.dot(inv(M), b)
    X1 = np.dot(Bgs, X0) + Cgs
    X1 = omega*X1+(1-omega)*X0
    K = 1
    while norm(X1 - X0) > eps * norm(X1) and K < iterMax:
        X0 = X1
        X1 = np.dot(Bgs, X0) + Cgs
        X1 = omega * X1 + (1 - omega) * X0
        K += 1
    return X1, K

A = [[64, 24, 1, 8, 15], [23, 50, 7, 14, 16], [4, 6, 58, 20, 22], [10, 12, 19, 66, 3], [11, 18, 25, 2, 54]]
b = [[219], [359], [444], [319], [309]]
X0 = [[0], [1], [1], [1], [2]]
eps = 10 ** (-6)
iterMax = 100
omega = 0.1
Xr, Kr = GS_relaxe(A, b, X0, eps, iterMax, omega)
print('Xr :', Xr)
print('Kr :', Kr)

##tab = np.zeros(0,20)
##for i in range(20):
##    tab[0][i] = 0.1*(i+1)
##    omega = 0.1*(i+1)
##    Xr, Kr = GS_relaxe(A, b, X0, eps, iterMax, omega)
##    plt.plot(Kr, iterMax)