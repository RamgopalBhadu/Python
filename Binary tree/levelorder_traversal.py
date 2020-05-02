#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLevelATNewLine(root):
    if root is None:
        return None
    q=queue.Queue()
    q.put(root)
    q.put(None)
    while not q.empty():
        currentNode=q.get()
        if currentNode is not None:
            print(currentNode.data,end=' ')
            if currentNode.left is not None:
            	q.put(currentNode.left)
            if currentNode.right is not None:
            	q.put(currentNode.right)
        if currentNode is None:
            print()
            if q.empty() is False:
                q.put(None)
            
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
#n=int(input())
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
printLevelATNewLine(root)

