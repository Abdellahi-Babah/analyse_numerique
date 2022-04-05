import numpy as np
from copy import deepcopy

def luDecomposition(A):
    [m, n] = np.shape(A)
    cont = 0
    for j in range(n - 1):
        for i in range(j + 1, n):
            cont += 1
            A[i][j] = A[i][j]/A[j][j]
            for k in range(j + 1, n):
                A[i][k] = A[i][k] - A[i][j]*A[j][k]
                cont += 2
    U = np.triu(A)
    L = np.identity(n) + np.tril(A, -1)
    return [L, U, cont]

def LU_possible(A):
    if A.shape[0] != A.shape[1]:
        return False

    n = A.shape[0]
    M = A
    for i in range(-1, 0, -1):
        if M.det() == 0:
            return False
        M = M.minorMatrix(i, i)
    return True


A = [[1, 1+5*(10**(-16)), 3], [2, 2, 20], [3, 6, 4]]
[L, U, comp] = luDecomposition(A)
print('L=', L)
print('U=', U)
B = A-np.dot(L, U)
print('A-LU = ', B)

