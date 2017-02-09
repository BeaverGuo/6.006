#open addressing

#input keys
TABLE_LENGTH = 11
input_keys = [10,22,31,4,15,28,17,88,59]
T = [None] * TABLE_LENGTH
T1 = [None] * TABLE_LENGTH
T2 = [None] * TABLE_LENGTH
C1 = 1
C2 = 3
#hash insert function

#@param T: hash table
#@param k: inser key
#@param idx: 0 for linear probing, 1 for quadratic probing
def hash_insert(T,k,idx):
    i = 0
    m = len(T)
    while i<=m:
        if idx == 0:
            j = linear_prob_helper(k,i,m)
        if idx == 1:
            j = quadratic_prob_helper(k,i,m)
        if idx == 2:
            j = double_hashing_prob_helper(k,i,m)
        if T[j] == None:
            T[j] = k
            return j
        else:
            i += 1
#hash search function
#why stop when encountering None?
def hash_search(T,k):
    i = 0
    j = 0
    m = len(T)
    while i<=m or T[j] == None:
        j = linear_prob_helper(k,i,m)
        if T[j] == k:
            return j
        i += 1
    return None

#linear probe h(k,i) helper function
def h_k_dot(k,i):
    return k

def linear_prob_helper(k,i,m):
    return (h_k_dot(k,i) + i)%m
#quadratic probing
def quadratic_prob_helper(k,i,m):
    return (h_k_dot(k,i) + C1*i + C2*i*i)%m
#double hashing probing
def h1_k(k):
    return k
def h2_k(k):
    m = len(T2)
    return 1 + (k % (m-1))
def double_hashing_prob_helper(k,i,m):
    return (h1_k(k) + i*h2_k(k))%m
def get_result(T,idx):
    for ele in input_keys:
        hash_insert(T,ele,idx)
    return T
    
print("Linear probe result: ", get_result(T,0))
print("Quadratic probe result: ", get_result(T1,1))
print("Doublehashing probe result: ", get_result(T2,2))



