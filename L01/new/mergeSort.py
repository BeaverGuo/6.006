# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 10:05:01 2016

@author: Administrator
"""
import math
#merge sort
def merge(A,p,q,r):
    #分成2个数组，L=[p,q] n1=q+1-p,R=[q+1,r] n2=r-q
    n1 = q+1-p
    n2 = r-q
    L = [None]*(n1+1)
    R = [None]*(n2+1)
    for i in range(n1):
        L[i] = A[p+i]
    for j in range(n2):
        R[j] = A[q+1+j]
    L[n1] = math.inf#这个用来控制最后一个值，确保全部比较完
    R[n2] = math.inf
    n = r+1-p
    i = 0
    j = 0
    for k in range(p,r+1):
        if L[i] > R[j]:
            A[k] = R[j]
            j += 1
        else:
            A[k] = L[i]
            i += 1
    return True

def mergeSort(A,p,r):
    if p<r:
        q = (p+r)//2
        mergeSort(A,p,q)
        mergeSort(A,q+1,r)
        merge(A,p,q,r)

A=[0,4,5,8,1,2,3]
merge(A,0,3,6)
print(A)
B=[2,3,46,79,8,9,10]
mergeSort(B,0,6)
print(B)

def merge1(a, start1, start2, end):
    index1 = start1
    index2 = start2
    length = end - start1
    aux = [None] * length
    for i in range(length):#遍历将更小的项放入aux
        if ((index1 == start2) or
            ((index2 != end) and (a[index1] > a[index2]))):
            aux[i] = a[index2]#放入更小项
            index2 += 1#继续下一个融合
        else:
            aux[i] = a[index1]
            index1 += 1
    for i in range(start1, end):
        a[i] = aux[i - start1]#minus start1 for extend array a

def merge1Sort(a):
    n = len(a)
    step = 1
    while (step < n):
        for start1 in range(0, n, 2*step):#教如何按指数2来分类分成2组,利用loop,([0],[2]),([1],[3]) 0,2  2*step, start1+step
            start2 = min(start1 + step, n)#start2从start1+step开始，没问题
            end = min(start1 + 2*step, n)#end =start1+2*step,如果就2组，如([0],[2]),([1],[3]),那么结束是2，即是(start1+step+step或者是start2+step),[2]就结束了
            merge(a, start1, start2, end)#start1和start2都是原来数组的序号
        step *= 2























      
    