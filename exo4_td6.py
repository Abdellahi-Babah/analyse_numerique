from numpy.linalg import norm
from math import *
import numpy as np
from scipy.linalg import lu
from copy import deepcopy
import matplotlib as plt
from scipy import stats
from numpy.linalg import inv
from numpy.linalg import pinv

def val_propres_lu(A, eps, iterMax):
    n = len(A)
    M0 = deepcopy(A)
    [P, L, U]= lu(M0)
    M1 = np.dot(U, L)
    K = 1
    while norm(np.diag(M1)-np.diag(M0))>eps and K < iterMax :
        M0 = M1
        [P, L, U] = lu(M0)
        M1 = np.dot(U, L)
        K += 1
    return M1, K

A = [[2, -1, 0], [-1, 2, -1],[0, -1, 2]]
eps = 10**(-6)
iterMax = 100

M1, K = val_propres_lu(A, eps, iterMax)
print('M1 :', M1) # ça donne une matrice triangulaire sup. les valeurs propres sont donc 3.41, 2 et 0.58
print('K :', K)
B = [[1/sqrt(2), 1/sqrt(2)], [1/sqrt(2), -1/sqrt(2)]]

eps = 10**(-6)
iterMax = 100

M1 = val_propres_lu(B, eps, iterMax)
print('M1 :', M1)
print('K :', K)
