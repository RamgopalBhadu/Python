#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTreePostOrder(postorder, inorder):
    if len(postorder)==0:
        return None
    rootdata=postorder[len(postorder)-1]
    root=BinaryTreeNode(rootdata)
    rootIndexInOrder=-1
    for i in range(0,len(inorder)):
        if inorder[i]==rootdata:
           rootIndexInOrder=i
           break
    if rootIndexInOrder==-1:
        return None
    leftinorder=inorder[0:rootIndexInOrder]
    rightinorder=inorder[rootIndexInOrder+1:]
    
    lenleftsubtree=len(leftinorder)
    
    leftpostorder=postorder[0:lenleftsubtree]
    rightpostorder=postorder[lenleftsubtree:len(postorder)-1]
    
    leftchild=buildTreePostOrder(leftpostorder, leftinorder)
    rightchild=buildTreePostOrder(rightpostorder, rightinorder)
    root.left=leftchild
    root.right=rightchild
    return root
    pass

def printLevelATNewLine(root):
    # Given a binary tree, print the level order traversal. Make sure each level
    # start in new line.
    if root==None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ

# Main
n=int(input())
postOrder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
root = buildTreePostOrder(postOrder, inorder)
printLevelATNewLine(root)

