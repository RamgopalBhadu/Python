#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import heapq
def checkMaxHeap(arr,n):
    if n<=1:
        return arr
    for i in range(int((n - 2) / 2) + 1): 

        if arr[2 * i + 1] > arr[i]:  
                return False

        if (2 * i + 2 < n and
            arr[2 * i + 2] > arr[i]):  
                return False
    return True
    pass

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst,n) else print('false')

