#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def checkNumber(arr,x,si):
    l=len(arr)
    if si==l:
        return False
    if arr[si]==x:
        return True
    isFound=checkNumber(arr,x,si+1)
    return isFound

    # Please add your code here
    pass

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
x=int(input())
a=checkNumber(arr,x,0)
if a==True:
    print('true')
else:
    print('false')
    

