from math import *
###Exo1###
###Q2###
def g1(x):
    return sqrt(2*x + 3)

def g2(x):
    return 3/(x-2)

def g3(x):
    return (x**2-3)/2

def PointFix(f,x0,eps,N):
    n=0
    while n<N:
        x = f(x0)
        if x-x0 <= eps:
            return x
        n += 1
        x0 = x

def f(x):
    return x**2-2*x-3

U1 = PointFix(g1,4,0.0001,100)
U2 = PointFix(g2,4,0.0001,100)
#U3 = PointFix(g3,4,0.0001,100)
print("U1 = "+str(U1))
print("U2 = "+str(U2) )
#print(U3)


