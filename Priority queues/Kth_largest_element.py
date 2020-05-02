#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import heapq
def kthLargest(arr, k):
    heap=arr[:k]
    heapq.heapify(heap)
    n=len(arr)
    for i in range(k,n):
        if heap[0]<arr[i]:
            heapq.heapreplace(heap,arr[i])
    return heap[0]
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    pass

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kthLargest(lst, k)
print(ans)

