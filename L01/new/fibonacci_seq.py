# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 15:18:22 2016

@author: Xian Guo
"""
#Fibonacci sequence 0,1,1,2,3...
#自己写的完全按照定义 O(2^n) pool :(
def fib_naive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_naive(n-1) + fib_naive(n-2)

#answer  %m是什么鬼?
def fibonacci_recursive_slow(n, m):
    assert n >= 0 #习惯写断言
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibonacci_recursive_slow(n - 1, m) + fibonacci_recursive_slow(n - 2, m)) % m

#因为递归子问题之间有重叠，可以用存储的方法来避免重复计算
cache = {}
def fibonacci_recursive_fast(n, m):
    if not (n,m) in cache:
        assert n >= 0
        if n == 0:
            result = 0
        elif n == 1:
            result = 1
        else:
            result = (fibonacci_recursive_fast(n - 1, m) + fibonacci_recursive_fast(n - 2, m)) % m
        cache[(n,m)] = result
    return cache[(n,m)]

#由于stack limit原因,把递归转成迭代版本

def fibonacci_iterative(n,m):
    assert n > 0
    if n == 0:
        return 0
    f_current, f_previous = 1, 0
    for _ in range(n-1):
        f_current, f_previous = f_current + f_previous % m, f_current
    return f_current
