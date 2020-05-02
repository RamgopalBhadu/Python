#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLevelWise(root):
    if root is None:
        return None
    q=queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode=q.get()
        print(currentNode.data,end=':')
        if currentNode.left is None:
            
            print("L",end=':')
            print(-1,end=',')
        else:
            print("L",end=':')
            print(currentNode.left.data,end=',')
            q.put(currentNode.left)
        if currentNode.right is None:
            
            print("R",end=':')
            print(-1)
        else:
            print("R",end=':')
            print(currentNode.right.data)
            q.put(currentNode.right)    
    pass

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main 
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
printLevelWise(root)

