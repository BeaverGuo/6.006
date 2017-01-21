#Max heap

class MaxHeap(object):
    def __init__(self, max_size=128):
        self.storage = [None for _ in range(max_size)] # heap array
        self.heap_size = 0 # init heap size

    # display whole max-heap by iterate each tree level 
    def display(self, width=80):
        next_element = 0
        for i in range(0,1000):
            level_elts = 2**i # i level , total elements 2**i
            elts = self.storage[next_element:min(next_element + level_elts,self.heap_size)] #level i elements
            next_element = min(next_element + level_elts, self.heap_size)
            if len(elts) == 0:
                break
            # gap is width, if use i in for loop, two i conflict
            positions = [ (k+1) * width / (level_elts + 1) for k in range(level_elts)] 
            output = " "
            for j, (elt,pos) in enumerate(zip(elts,positions)):
                idx = 2**i + j - 1
                while len(output) <= pos:
                    output += " "
                output += "%d[@%d]" % (elt,idx)
            print output

    def fix_down(self, index): # max-heapify
        while index < self.heap_size:
            # pick maximum child
            max_child_idx = None
            # find max of left child and right child 
            if 2*index + 1 < self.heap_size:
                max_child_idx = 2*index + 1

            if 2*index + 2 < self.heap_size and \
                    self.storage[2*index + 2] > self.storage[2*index + 1]:
                max_child_idx = 2 * index + 2

            # check RI of max-heap
            if max_child_idx is None or \
                    self.storage[index] > self.storage[max_child_idx]:
                break

            # if violate exchange and recurse
            self.storage[index], self.storage[max_child_idx] = self.storage[max_child_idx], self.storage[index]
            index = max_child_idx

    def fix_up(self, index): # heapify go up
        assert index < self.heap_size
        while index > 0:
            parent_idx = (index - 1) // 2
            if self.storage[index] >= self.storage[parent_idx]:
                self.storage[index], self.storage[parent_idx] = self.storage[parent_idx], self.storage[index]
                index = parent_idx
            else:
                break

    def insert(self,element):
        self.heap_size += 1
        new_index = self.heap_size - 1
        self.storage[new_index] = element
        self.fix_up(new_index)

    def extract_max(self):
        self.storage[0], self.storage[self.heap_size - 1] = self.storage[self.heap_size -1], self.storage[0]
        self.heap_size -= 1
        self.fix_down(0)
        return self.storage[self.heap_size]

    def heapify(self):
        for i in range(self.heap_size - 1, -1, -1):
            self.fix_down(i)

    @staticmethod
    def wrap_list(lst):
        h = MaxHeap(0)
        h.storage = lst
        h.heap_size = len(lst)
        return h


example = [3,4,5,8,6,1,10,9,5]
h = MaxHeap.wrap_list(example)
h.display()


def heap_sort(array):
    as_heap = MaxHeap.wrap_list(array)
    as_heap.heapify()
    while as_heap.heap_size > 0:
        as_heap.extract_max()
