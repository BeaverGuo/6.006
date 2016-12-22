# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 21:55:55 2016
Matrix element search
NEW PSET SOLUTIONS PROBLEM 1-2 B 2
@author: Administrator
"""
import random
#some helper method
#generate a random matrix   current not used 
def randomProblem(rows = 10, columns = 10, max = 1000):
    """
    Generate a random matrix, with the specified number of rows and
    columns.  Each number is distributed uniformly at random between
    zero and the specified maximum.
    """
    result = []

    for i in range(rows):
        resultRow = []

        for j in range(columns):
            resultRow.append(random.randint(0, max))

        result.append(resultRow)

    return result

#print(randomProblem())
#divide matrix A into 4 submatries   this is right after test! but not used!
def getSubMatrix(A,mid):
    left=[]
    right=[]
    downLeft=[]
    downRight=[]
   
    alen = len(A)
    for i in range(mid):
        lRow=[] #row should be clear after every iteration of i
        for j in range(mid):
            lRow.append(A[i][j])
        left.append(lRow)
    for k in range(mid,alen):
        dlRow=[]
        for l in range(mid):
            dlRow.append(A[k][l])
        downLeft.append(dlRow)
    for m in range(mid):
        rRow=[]
        for n in range(mid,alen):
            rRow.append(A[m][n])
        right.append(rRow)
    for o in range(mid,alen):
        drRow=[]
        for q in range(mid,alen):
            drRow.append(A[o][q])
        downRight.append(drRow)
    
    return (left,right,downLeft,downRight)
            
#how to get the index of the matrix?
def findInMatrix(A,startRow,startCol,matrixSize,num):#submatrix is defined by startRow startCol and matrixSize in A
        n = matrixSize
        (row,col) = (startRow,startCol)
        if n == 1:#handle base
            if num == A[row][col]:
                return (row,col,num)
            else:
                return (None,None,None)
        else:
            mid = n//2
            lnum = None
            rnum = None
            dlnum = None
            drnum = None
            lrow = None
            lcol = None
            rrow = None
            rcol = None
            dlrow = None
            drrow = None
            drrow = None
            drcol = None
            #(matrixLeft,matrixRight,matrixDL,matrixDR) = getSubMatrix(A,mid)
            if A[startRow+mid-1][startCol+mid-1] > num:
                (lrow,lcol,lnum) = findInMatrix(A,startRow,startCol,mid,num)
                (rrow,rcol,rnum) = findInMatrix(A,startRow,startCol+mid,mid,num)
                (dlrow,dlcol,dlnum) = findInMatrix(A,startRow+mid,startCol,mid,num)
            elif A[startRow+mid-1][startCol+mid-1] == num:#get the rightdown value of the sub matrix
                return (startRow+mid-1,startCol+mid-1,num)
            else:
                (drrow,drcol,drnum) = findInMatrix(A,startRow+mid,startCol+mid,mid,num)
                (rrow,rcol,rnum) = findInMatrix(A,startRow,startCol+mid,mid,num)
                (dlrow,dlcol,dlnum) = findInMatrix(A,startRow+mid,startCol,mid,num)
                
            if lnum != None:
                return (lrow,lcol,lnum)
            if rnum != None:
                return (rrow,rcol,rnum)
            if dlnum != None:
                return (dlrow,dlcol,dlnum)
            if drnum != None:
                return (drrow,drcol,drnum)
            else:
                return(None,None,None)

A = [[1,4,7,9],
     [2,4,8,10],
     [6,8,8,11],
     [12,13,14,15]
    ]

#print(getSubMatrix(A,2))
#print(len(A))
print(findInMatrix(A,0,0,4,13))            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    