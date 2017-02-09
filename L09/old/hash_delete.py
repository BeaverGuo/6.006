#hash delete function
def hash_delete(T,k):
    i = 0
    m = len(T)
    while i <= m:
        j = linear_prob_helper(k,i,m)
        if T[j] == k:
            T[j] = 'DELETED'
            return
        elif T[j] == None:
            break;
        else:
            i += 1

