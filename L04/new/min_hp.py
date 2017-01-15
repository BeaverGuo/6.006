# Min-Heap psedo code
'''
MIN-HEAPIFY(A, i):
    l <- LEFT(i)
    r <- RIGHT(i)
    if l ≤ heap-size[A] and A[l] < A[i]:
        then smallest <- l
        else smallest <- i
    if r ≤ heap-size[A] and A[r] < A[smallest]:
        then smallest <- r
    if smallest != i:
        then swap(A[i], A[smallest])
            MIN-HEAPIFY(A, smallest)
'''