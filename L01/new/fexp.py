# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 23:46:51 2016

@author: Administrator
"""
#fast exponentiation
#calculate a^b mod m
import numpy as np
import cProfile
from operator import mul

def fexp_recursive(a,b,m,mul_op=mul):
    assert b >= 1
    if b == 1:
        return a
    elif b % 2 == 0:
        conquered = fexp_recursive(a,b/2,m,mul_op=mul_op)
        return mul_op(conquered,conquered)%m
    else:
        b_one_less = fexp_recursive(a,b-1,m,mul_op=mul_op)
        return mul_op(a,b_one_less)%m

print(fexp_recursive(2, 6, 1000))

def fexp_iterative(a,b,m,mul_op=null):
    assert b>=1
    result=a
    multiplier=a
    b-=1
    while b>0:
        if b%2==1:
            result=mul_op(result,multiplier)
        multiplier=mul_op(multiplier,multiplier)
        b/=2
    return result
    
    
#fibonacci slow also definition
def fibonacci_recursive_slow(n, m):
    assert n >= 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci_recursive_slow(n - 1, m) + fibonacci_recursive_slow(n - 2, m)) % m     
    
    
    
    
    
    
    
    