#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def isIdentical(tree1, tree2):
    if tree1==None and tree2==None:
        return True
    t1=tree1
    t2=tree2
    if (t1.data) != (t2.data):
        return False
    ans=True
    if len(tree1.children) != len(tree2.children):
        return False
    
    else:
        for child in tree1.children and tree2.children:
            ans=isIdentical(child, child)
    if ans==False:
        return False
    else:
        return True
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
arr1 = list(int(x) for x in input().strip().split(' '))
tree1 = createLevelWiseTree(arr1)
arr2 = list(int(x) for x in input().strip().split(' '))
tree2 = createLevelWiseTree(arr2)
if isIdentical(tree1, tree2):
    print('true')
else:
    print('false')

