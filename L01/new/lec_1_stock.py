# Code for stock problem (L01, 6.006 MIT EECS)

"""
You are given an array A[0..n-1] of stock prices for
n consecutive days, and want to pick two days i0 and j0,
with 0 <= i0 <= j0 < n such if you buy a share of stock on day
i0 and sell it on day j0 you have maximum gain.  That is,
you want to maximize  A[j0] - A[i0].

The routines 'naive', 'dc', and 'lin' implement a naive
algorithm, a divide-and-conquer algorithm, and a linear-time
algorithm. 

These routines only return the maximum gain possible; they
don't return the days i0 and j0 that achieve this gain.

Exercise: modify these routines to output i0 and j0 as well.

"""

import random
import time

def make_prices(n, seed):
    """ Return array of n random prices, based on seed. """
    random.seed(seed)              # set random # generator seed
    return [ random.random() for _ in range(n) ]# _ is used as a variable that not to be used

def naive(A):
    """ return best gain on A, using naive method 
        running time, due to doubly-nest loop, is Theta(n^2)
    """
    n = len(A)
    ans = 0
    for i0 in range(n):
        for j0 in range(i0,n):
            ans = max(ans, A[j0]-A[i0])
            if ans == A[j0]-A[i0]:
                indexBuy = i0
                indexSell = j0
            else:
                indexBuy = indexBuy
                indexSell = indexSell
    return (ans,indexBuy,indexSell)

def dc(A, lo, hi):
    """ return best gain on A[lo:hi], using divide & conquer 
        running time is solution to T(n) = 2*T(n/2) + Theta(n) = Theta(n log n)
    """
    n = hi-lo
    # base case
    if n == 1:
        return 0#base条件in this case if our array is of size 1, then the maximum profit we can make is 0
    # divide and conquer
    # divide into lo:mid and mid:hi
    mid = (lo+hi)//2            
    # recurse on left half
    gain_low = dc(A, lo, mid)
    # recurse on right half
    gain_high = dc(A, mid, hi)
    # figure out best gain for buying in left half, selling in right half.cross mid情况
    buy_price = min([ A[i] for i in range(lo, mid) ])
    sell_price = max([ A[i] for i in range(mid, hi)])
    gain_cross = sell_price - buy_price
    # optimum is max of three cases just solved
    return max(gain_low, gain_high, gain_cross)

def lin(A):
    """ return best gain, computed by simple linear-time alg 
        running time is Theta(n)
        计算k之前的最小值buy minimum存入数组PMins再计算k点的值与最小值相减，遍历k找出sell maximum
    """
    n = len(A)
    # precompute all prefix minimas
    # PMin[i] is the minimum in the length i+1 prefix of A
    PMins = [0] * n
    PMins[0] = A[0]
    for i in range(1, n):
        PMins[i] = min(A[i], PMins[i-1])#reuse computation
    # max_gain will equal the optimum gain max_{i} max_{j>=i} A[j]-A[i]
    max_gain = 0
    for j in range(1, n):
        max_gain = max(max_gain, A[j]-PMins[j])#保持顺序sell after buy
    return max_gain

#another lin
def lin1(A):
    """ return best gain, computed by linear-time alg 
        running time is Theta(n)
    """
    n = len(A)
    # B[k] = min{ A[i0]: i0 <= k }   for k = 0, 1, ..., n-1
    #      = price to buy at if you have to buy no later than k (and sell no earlier than k)
    B = [A[0]] * n
    for k in range(1, n):
        B[k] = min(B[k-1],A[k]) #reuse computation
    # S[k] = max{ A[j0]: j0 >= k }   for k = 0, 1, ..., n-1
    #      = price to sell at if you have to sell no earlier than k (but bought no later than k)
    S = [A[n-1]] * n
    for k in range(n-2, -1, -1):
        S[k] = max(S[k+1], A[k])#save the reverse direction max value - normal direction min value then iterate
    # G[k] = S[k] - B[k] for k = 0, 1, ..., n-1
    #      = best gain from buying no later than k, then selling no earlier than k
    G = [ S[k]-B[k] for k in range(n) ]
    # opt = max { G[k]: 0 <= k < n }
    #     = best possible gain for given input A
    opt = max(G)
    return opt

def test():

    n = 10000            # may want to use pypy for larger value of n
    print("n = ", n)
    A = make_prices(n, 1)
    i0=None
    j0=None

    t0 = time.time()
    (gain_naive,i0,j0) = naive(A)
    t1 = time.time()
    gain_dc = dc(A,0,n)
    t2 = time.time()
    gain_lin = lin(A)
    t3 = time.time()

    print ("naive: ", gain_naive, "time: ", t1-t0, " seconds.")
    print ("dc:    ", gain_dc,    "time: ", t2-t1, " seconds.")
    print ("lin:   ", gain_lin,   "time: ", t3-t2, " seconds.")
    print ("i0:",i0,"j0:",j0)

test()

""" Typical output:
    n =  10000
    naive:  0.999714239084 time:  8.96542191505  seconds.
    dc:     0.999714239084 time:  0.0268700122833  seconds.
    lin:    0.999714239084 time:  0.00327301025391  seconds.
"""

