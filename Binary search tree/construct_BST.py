#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructBST(lst,start,end):
    if start>end:
        return
    if not lst:
        return None
    mid=(start+end)//2
    root=BinaryTreeNode(lst[mid])
    root.left=constructBST(lst,start,mid-1)
    root.right=constructBST(lst,mid+1,end)

    return root
    pass

def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Main
n=int(input())
lst=[int(i) for i in input().strip().split()]
root=constructBST(lst,0,n-1)
preOrder(root)

