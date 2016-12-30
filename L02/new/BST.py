 '''Binary Search Trees
 Binary tree: Tree where each node has up to two leaves

  1
 / \
2   3
Binary search tree: Used for searching. A binary tree where the left child contains only nodes with values less than the parent node, and where the right child only contains nodes with values greater than or equal to the parent.

  2
 / \
1   3
'''
#checkBST 1
def inOrder(node,elements=[]):
    if node == null:
        return elements
    inOrder(node.left,elements)#一直递归到最左边leaf再append,左,node,右这样
    elements.append(node.value)
    inOrder(node.right,elements)

def checkBST1(B):
    elements = []
    inOrder(B.root,elements)
    for i in range(len(B)):
        if elements[i-1] >= elements[i]:
            return False
    return True

#checkBST 2
def checkBST2(node, low=float("-inf"), high=float("inf")):
    if node.value < low or node.value > high:
        return False
    elif node.left:
        if not checkBST2(node.left,low,node.value):
            return False
        if not checkBST2(node.right,node.value,high):
            return False
    return True


#create a blanced BST
def createBlancedBSTFromList(eles):
    if not len(eles):
        return None
    #elements = []
    #inOrder(B,elements)
    el_len = len(eles)
    mid = el_len // 2
    r = Node()
    r.value = eles[mid]
    r.left = createBlancedBST(eles[0:mid])
    r.right = createBlancedBST(eles[mid:el_len])
    return r

def createBlancedBST(B):
    elements = []
    inOrder(B,elements)
    return createBlancedBSTFromList(elements)
