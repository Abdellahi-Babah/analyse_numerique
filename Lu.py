import pprint
import scipy
import numpy as np
import scipy.linalg

A = np.array([[1, 1+5*(10**(-16)), 3], [2, 2, 20], [3, 6, 4]])
P, L, U = scipy.linalg.lu(A)

print("A:")
pprint.pprint(A)

print('P:')
pprint.pprint(P)

print("L:")
pprint.pprint(L)

print("U:")
pprint.pprint(U)
