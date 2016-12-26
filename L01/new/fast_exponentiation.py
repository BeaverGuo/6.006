# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 14:51:33 2016

@author: Xian Guo
"""
import numpy as np
import cProfile
from operator import mul
#这个mul可能效率更高

#Fast Exponentiation
#求a^b mod m,经常用在RSA里面
#自己写的完全利用公式来实现
'''
def fast_exp(a,b,m):
    if b == 1:
        return a
    elif b%2 == 0:
        return fast_exp(a,b/2,m)
    else:
        return a*fast_exp(a,b-1,m)
'''

#参考答案写法，命名用下划线,为什么没处理b=0的情况？这个Mul是乘法吧，自己写的忘记平方相乘了，菜啊!
def fexp_recursive(a, b, m, mul_op=mul):
    # We can easiely handle b = 0, here, but we choose not to
    # this will be helpful later when we deal with matrices...
    assert b >= 1
    if b == 1:
        return a
    elif b % 2 == 0:
        conquered = fexp_recursive(a, b / 2, m, mul_op=mul_op)
        return  mul_op(conquered, conquered) % m
    else:
        b_one_less = fexp_recursive(a, b - 1, m, mul_op=mul_op)        
        return mul_op(a, b_one_less) % m

print fexp_recursive(2, 6, 1000)

#把b转成2进制, 如果i-th bit值为1则乘以a^(2^i)
def fexp_iterative(a, b, m, mul_op=mul):
    assert b >= 1
    result = a
    multiplier = a
    b -= 1
    while b > 0:
        if b % 2 == 1:
            result = mul_op(result, multiplier) % m
        multiplier = mul_op(multiplier, multiplier) % m
        b /= 2
    return result

print fexp_iterative(2, 6, 1000)