# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 15:51:05 2017

@author: Xian Guo
"""

import cProfile
import math

from collections import namedtuple

#hash function
#division method
def hashtest(b, mod):
    for i in range(2*mod):
        print(" %d * %d (mod %d) = %d" % (b, i, mod, (b*i) % mod))


def hashtest_multiplication(A, m):
    for k in range(2 * m):
        fraction = (k * A) % 1.0 
        res = math.floor(m * fraction)
        print("floor(%d * (%d * %f mod 1)) = %d" % \
              (m, k, A, res))

def test_dict(base):
    d = {}
    for i in range(1000000):
        d[base*i] = True
    print(len(d))
    


class LLNode(object):
    def __init__(self, key, value, next_node):
        self.key, self.value, self.next_node = \
                key, value, next_node
            
class LinkedList(object):
    def __init__(self):
        """Key-value storage over Linked List
        
        unique values per key"""
        self.root = None
        
    def find(self, key):
        """Returns node given key"""
        # find a node with a given key,
        # by following links: O(n)
        node = self.root
        while node is not None:
            if node.key == key:
                return node
            node = node.next_node
        
    def __getitem__(self, key):
        """Returns value for a given key"""
        node = self.find(key)
        if node is not None:
            return node.value
        else:
            return None
            
    def __setitem__(self, key, value):
        """Sets key given value"""
        node = self.find(key)
        if node is not None:
            # modify existing node
            node.value = value
        else:
            # append front
            self.root = LLNode(key, value, self.root)
            
            
class HashTable(object):
    def __init__(self, num_slots):
        """Initializes chained hash table with num_slots slots"""
        self.num_slots = num_slots
        self.table = [ LinkedList() for _ in range(self.num_slots)]
        self.golden = (math.sqrt(5) - 1.0) / 2.0
        
    def multiplication_address(self, key):
        """Multiplication adressing described above"""
        # hash(k) maps any Python object that implements it
        # to a 64-bit integer. It is not necessarily in the 
        # range of our hashtable.
        fraction = (hash(key) * self.golden) % 1.0 
        return math.floor(self.num_slots * fraction)
        
    def __getitem__(self, key):
        relevant_list = self.table[self.multiplication_address(key)]
        return relevant_list[key]

    def __setitem__(self, key, value):
        relevant_list = self.table[self.multiplication_address(key)]
        relevant_list[key] = value