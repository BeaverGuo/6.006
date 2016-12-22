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
def inOrder(node,elements=[]):
    if node == null:
        return elements
    inOrder(node.left,elements)#一直递归到最左边再append,左,node,右这样
    elements.append(node.value)
    inOrder(node.right,elements)

def checkBST(B):
    elements = []
    inOrder(B.root,elements)
    for i in range(len(B)):
        if elements[i-1] >= elements[i]:
            return False
    return True

