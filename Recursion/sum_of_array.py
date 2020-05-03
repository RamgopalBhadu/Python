#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def sumArray(arr,n):
    if n==0:
        return 0
    
    return arr[n-1]+sumArray(arr,n-1)
    # Please add your code here
    pass

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
print(sumArray(arr,n))

