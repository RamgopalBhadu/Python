#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import heapq
def kSmallest(arr, k):
    heap=arr[:k]
    heapq._heapify_max(heap)
    n=len(arr)
    for i in range(k,n):
        if heap[0]>arr[i]:
            heapq._heapreplace_max(heap,arr[i])
    return heap
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    pass

# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
for ele in ans:
    print(ele)

