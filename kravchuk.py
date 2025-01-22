import numpy as np
from scipy.optimize import linprog
from math import comb, floor
def kravchuk(k, i, n, q):
    result = 0
    for j in range(k+1):
        result += (((-1)**j)*((q-1)**(k-j))*comb(i, j)*comb(n-i, k-j))
    return result
def mat(n, q):
    return np.array([[kravchuk(k, i, n, q) for i in range(n+1)] for k in range(n+1)])
def vec_struct(n, rat):
    threshold_val = floor((1-rat)*n)
    l = ["a" if x <= threshold_val else 0 for x in range(n+1)]
    l[0] = 1
    return l
def lp(vec, mat):
    c = -1*np.ones(len(vec))
    mat = -1*mat
    b = np.zeros(len(vec))
    bds = [(0, None) if x == "a" else (x, x) for x in vec]
    res = linprog(c, A_ub = mat, b_ub = b, bounds=bds, integrality=-3*c)
    return -1*res.fun
    
