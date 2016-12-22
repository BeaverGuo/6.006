# -*- coding: utf-8 -*-
#define a binary search tree class
#The BinarySearchTree class has a reference to the TreeNode that is the root of the binary search tree.
#binary search tree class create the real tree

class BinarySearchTree:
    def __init__(self):
        self.root=None
        self.size=0
    
    def length(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self.root.__iter__()
    
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)#search start from the root
        else:
            self.root=TreeNode(key,val)#handle the case: do not have a root,create one
        self.size =self.size+1
        
    def _put(self,key,val,currentNode):
        if key<currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)#recursive call to search the tree
            else:
                currentNode.leftChild=TreeNode(key,val,parent=currentNode)#parent是形参 设置默认值
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild=TreeNode(key,val,parent=currentNode)
                
    def get(self,key):
        if(self.root):
            res=self._get(key,self.root)#return the payload not the key!
            if res:
                return res.payload
            else:
                return None
        else:
            return None
    
    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key<currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)
        
 
    def __setitem__(self,k,v):#overloads operator[]
        self.put(k,v)
    
    def __getitem__(self,k):
        return self.get(k)
        
    def __contains__(self,key):#overloads in
        if self._get(key,self.root):
            return True
        else:
            return False
    
    def __delitem__(self,key):
        self.delete(key)
    
    def delete(self,key):
        if self.size > 1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error,Key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error,Key not in tree')
    
    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None#hard to understand
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ
    
    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current
        
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            else:
                if self.hasRightChild():
                    if self.isRightChild():
                        self.parent.rightChild = self.rightChild
                    else:
                        self.parent.leftChild = self.rightChild
                    self.rightChild.parent = self.parent
            
    
    def remove(self,currentNode):
        if currentNode.isLeaf():#leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        
        else:#this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,currentNode.leftChild.rightChild
                                                )
            else:
                if currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                elif currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key,currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,currentNode.rightChild.rightChild
                                                )
    
    
            
    
#put method to put a tree node to the binary search tree
    
#use optional parameters
#TreeNode class is used to create a tree node to the search tree and some helper function
#for implementing binary search tree methods
class TreeNode:
    def __init__(self,key,val,left=None,right=None,parent=None):
        self.key = key
        self.payload=val
        self.leftChild=left
        self.rightChild=right
        self.parent=parent
    
    def hasLeftChild(self):
        return self.leftChild
    def hasRightChild(self):
        return self.rightChild
    
    def isLeftChild(self):
        return self.parent and self.parent.leftChild==self #logical error:forget parent
    def isRightChild(self):
        return self.parent and self.parent.rightChild==self
    
    def isRoot(self):
        return not self.parent#good logical
    def isLeaf(self):
        return not (self.leftChild or self.rightChild)
    
    def hasAnyChildren(self):
        return self.leftChild or self.rightChild
    def hasBothChildren(self):
        return self.leftChild and self.rightChild
    
    def replaceNodeData(self,key,val,lc,rc):
        self.key=key
        self.payload=val
        self.leftChild=lc
        self.rightChild=rc
        if self.hasLeftChild():
            self.leftChild.parent=self
        if self.hasRightChild():
            self.rightChild.parent=self
    

print('hello world')
mytree = BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"

print(mytree[6])
print(mytree[2])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

