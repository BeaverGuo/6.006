# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 15:13:25 2016
Maximum sum subsequence problem
divide and conquer
@author: Administrator
"""
import random
import time
import math

def make_prices(n,seed):
    random.seed(seed)
    return [random.random() for _ in range(n)]


def maxSubSum(A,lo,hi):
#safety check

    if lo == None:
        lo=0
    if hi == None:
        hi = len(A)
    if A == None:
        return
    
    n = hi - lo
    
    if n == 1:
        return (lo,hi,A[lo])#handle base condition when the array size is 1
    else:
        mid = (lo + hi) //2
        (left_lo,left_hi,left_sum) = maxSubSum(A,lo,mid)#left recursive call
        (right_lo,right_hi,right_sum) = maxSubSum(A,mid,hi)#right recursive call
        (cross_lo,cross_hi,cross_sum) = findCrossMax(A,lo,mid,hi)#cross mid
        submax = max(left_sum,right_sum,cross_sum)
        if submax == left_sum:
            leftIndex = left_lo
            rightIndex = left_hi
        elif submax == right_sum:
            leftIndex = right_lo
            rightIndex = right_hi
        else:
            leftIndex = cross_lo
            rightIndex = cross_hi
            
        return (leftIndex,rightIndex,submax)
    

def findCrossMax(A,lo,mid,hi):
    left_sum = -math.inf
    sum = 0
    lIndex = 0#在if里面要定义否则会报错
    rIndex = 0
    for i in range(mid,lo-1,-1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            lIndex = i
    right_sum = -math.inf
    sum = 0
    for j in range(mid+1,hi):
        sum += A[j]
        if sum > right_sum:        
            right_sum = sum
            rIndex = j
    
    return (lIndex,rIndex,left_sum + right_sum)

testB = [10, -2, 10, 5, -4, 14]

print maxSubSum(testB,0,6)













           