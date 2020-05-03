#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def firstIndex(arr, x):
    l=len(arr)
    if l==0:
        return-1
    if arr[0]==x:
        return 0
    smalloutput=arr[1:]
    sortedoutput=firstIndex(smalloutput, x)
    if sortedoutput== -1:
        return -1
    else:
        return sortedoutput +1
    
    # Please add your code here
    pass

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
print(firstIndex(arr, x))

