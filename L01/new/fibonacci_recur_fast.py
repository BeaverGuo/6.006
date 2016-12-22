# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 10:31:20 2016

@author: Xian Guo
"""
import numpy as np
import cProfile
from operator import mul

#fast fibonacci memorized recursion
cache={}
def fibonacci_recur_fast(n,m):
    if not (n,m) in cache:
        assert n>=0
        if n==0:
            result=0
        elif n==1:
            result=1
        else:
            result=(fibonacci_recur_fast(n-1,m)+fibonacci_recur_fast(n-2,m))
        cache[(n,m)]=result#cache the result from (1,m) (0,m) (2,m) ... for look up
    return cache[(n,m)]

print(fibonacci_recur_fast(6,1000))


def fibonacci_iter(n,m):
    assert n>=0
    if n==0:
        return 0
    f_cur,f_pre = 1,0
    for _ in range(n-1):
        f_cur,f_pre = f_cur+f_pre,f_cur
    return f_cur

print(fibonacci_iter(6,1000))

F = np.array([[1, 1],
              [1, 0]])

def fibonnaci_matrix(n, m):
    Fn = fexp_recursive(F, n, m, mul_op=np.dot)
    return Fn[0][1]