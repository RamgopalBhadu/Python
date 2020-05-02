#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def nextLargest(tree, n):
    #t=tree
    ans=None
    if tree==None:
        return ans
    if tree.data>n:
        ans=tree
    for child in tree.children:
        temp=nextLargest(child, n)
        if temp!=None:
            if (not ans) or temp.data<ans.data:
            	ans=temp
    return ans        
        
    pass

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
n = int(input())
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
print(nextLargest(tree, n).data)

