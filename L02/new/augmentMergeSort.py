# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 20:31:32 2016

@author: Xian Guo
"""
#solution to PS 2-2
#augment mergesort
#A1,A2是已经排序好了的,因为真实的mergeSort是用递归到只有2个元素的时候排的
#[A1,A2]算逆序从A1着手，因为排到后面都是更大的，不是逆序的情况，只有A1中的项大于A2中的项才是逆序
#但下面这个算法augmentMergeSort在A1长度等于A2情况下不可行
'''
def augmentMergeSort(A1,A2):
    retArray=[]
    retParityBit=0
    index_A1=0
    index_A2=0
    l1 = len(A1)
    l2 = len(A2)
    while index_A1 < l1 or index_A2 < l2:
        #append更小的那项
        if A1[index_A1] > A2[index_A2] or index_A1 == l1-1:#判断更大项的长度结束的情况
            retArray.append(A2[index_A2])
            if index_A2 == l2-1:#处理一个数组merge完的情况,并防止数组越界
                for i in A1[index_A1:]:
                    retArray.append(i)
                retParityBit = retParityBit + len(A1[index_A2:])*l2%2
                return (retArray,retParityBit)
            else:
                index_A2 = index_A2 + 1
            #在A1项更大情况下更新奇偶位
            retParityBit = retParityBit + (l1-index_A1)%2
        elif A2[index_A2] > A1[index_A1] or index_A2 == l2-1:
           retArray.append(A1[index_A1])
           if index_A1 == l1-1:
               for i in A2[index_A2:]:
                    retArray.append(i)
               return (retArray,retParityBit) 
           else:
               index_A1 = index_A1 + 1
    return (retArray,retParityBit)

#之后改成下面这个也是错的，数组越界还会发生，当[1],[2]merge时
def augmentMerge(A1,A2):
    retArray=[]
    retParityBit=0
    index_A1=0
    index_A2=0
    l1 = len(A1)
    l2 = len(A2)
    while index_A1 < l1 or index_A2 < l2:
        #append更小的那项
        if(l1<=l2):
            if  index_A1 == l1 or A1[index_A1] >= A2[index_A2] :#判断更大项的长度结束的情况,这里用了short-cut curcuit logic,还得处理相等的情况
                retArray.append(A2[index_A2])
                index_A2 = index_A2 + 1
            #在A1项更大情况下更新奇偶位
                retParityBit = (retParityBit + (l1-index_A1))%2
            elif index_A2 == l2 or A2[index_A2] >= A1[index_A1] :
                retArray.append(A1[index_A1])
                index_A1 = index_A1 + 1
        else:
            if index_A2 == l2 or A2[index_A2] >= A1[index_A1] :
                retArray.append(A1[index_A1])
                index_A1 = index_A1 + 1
            elif index_A1 == l1 or A1[index_A1] >= A2[index_A2] :#判断更大项的长度结束的情况
                retArray.append(A2[index_A2])
                index_A2 = index_A2 + 1
            #在A1项更大情况下更新奇偶位
                retParityBit = (retParityBit + (l1-index_A1))%2
    return (retArray,retParityBit)
'''
#上面的merge用while index_A1 < l1 or index_A2 < l2容易数组越界，改成and
def augmentMerge(A1,A2):
    retArray=[]
    retParityBit=0
    index_A1=0
    index_A2=0
    l1 = len(A1)
    l2 = len(A2)
    while index_A1 < l1 and index_A2 < l2:
        if  A1[index_A1] > A2[index_A2] :
            retArray.append(A2[index_A2])
            index_A2 = index_A2 + 1
            #在A1项更大情况下更新奇偶位
            retParityBit = (retParityBit + (l1-index_A1))%2
        else :
            retArray.append(A1[index_A1])
            index_A1 = index_A1 + 1
    #处理一个数组被merge完的情况
    while index_A1 < l1:
        for i in A1[index_A1:]:
            retArray.append(i)
        index_A1 = l1
        retParityBit = retParityBit + len(A1[index_A2:])*l2%2
    while index_A2 < l2:
        for i in A2[index_A2:]:
            retArray.append(i)
        index_A2 = l2
    return (retArray,retParityBit)

#A1=[1,3]
#A2=[2,4]

#print(augmentMerge(A1,A2))

#真正的mergeSort O(nlogn)
def augmentMergeSort(A):
    Bl=[]
    Br=[]
    bl=0
    br=0
    if len(A)<=1:
        return (A,0)
    mid = len(A)//2
    A_left = A[0:mid]#不包含中间
    A_right = A[mid:len(A)]#包含中间
    (Bl,bl)=augmentMergeSort(A_left)
    (Br,br)=augmentMergeSort(A_right)
    (B,b)=augmentMerge(Bl,Br)
    b=(b+bl+br)%2
    return (B,b)

A=[4,2,6,3,9]
print augmentMergeSort(A)




















           