# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 11:44:56 2016

@author: Xian Guo
"""
#maximum stock gain problem:'buy','sell','buy','sell'
#abstract problem to -->
#find max(A[i2]-A[i1])+(A[i4]-A[i3]) where 0<=i1<=i2<=i3<=i4<=n-1
#主要还是要分成2部分 divide and conquer
def max2buysellStockGain(A):
    n = len(A)
    PMin=[None]*n #从0到n-1的某个i的最小值存储下来 这个用于快速计算i处single buy single sell最大利润G[i]
    G = [None]*n #从0到n-1的某个i sell at i single buy single sell最大利润G[i] 
    PBS = [None]*n #i及其之前single buy single sell最大利润
    PMin[0] = A[0]
    G[0] = 0
    PBS[0] = 0
    for i in range(1,n):
        PMin[i] = min(PMin[i-1],A[i])#min A[x] before 把它存下来就不用下次再去计算了
    for i in range(1,n):
        G[i] = max(G[i-1],A[i]-PMin[i])#max profit sell at i 因为存下来了所以不用计算，直接look up
    for i in range(1,n):
        PBS[i] = max(PBS[i-1],G[i])#one buy sell max profit before i
#reverse max
    PMax = [None]*n
    GR = [None]*n
    PBSR = [None]*n
    PMax[n-1] = A[n-1]
    GR[n-1] = 0
    PBSR[n-1] = 0
    
    for j in range(n-2,-1,-1):#n-2 to 0
        PMax[j] = max(PMax[j+1],A[j])
    for j in range(n-2,-1,-1):
        GR[j] = max(GR[j+1],PMax[j]-A[j])
    for j in range(n-2,-1,-1):
        PBSR[j] = max(PBSR[j+1],GR[j])
    
    maxGain = 0
    for i in range(n):
        maxGain = max(PBS[i]+PBSR[i],maxGain)
    
    return maxGain

A = [13,4,5,6,17,8,9,10]
print(max2buysellStockGain(A))

#another solution similar to the algorithm before 简单看成4步操作 4个loop解决了
 def max2buysellStockGain1(A):
     n = len(A)
     PMin=[None]*n
     PBSMax = [None]*n
     PBSBMax = [None]*n
     PMin[0] = A[0]
     PBSMax[0] = 0
     PBSBMax[0] = -A[0]
     maxGain = 0
     for i in range(1,n):
        PMin[i] = min(PMin[i-1],A[i])#min A[x] before i
     for i in range(1,n):
        PBSMax[i] = max(PBSMax[i-1],A[i]-PMin[i])#max profit sell at i
     for i in range(1,n):
        PBSBMax[i] = max(PBSBMax[i-1],PBSBMax[i]-A[i])#one buy sell buy max profit before i
     for i in range(1,n):
         maxGain = max(A[i]+PBSBMax[i],maxGain)
    return maxGain
    