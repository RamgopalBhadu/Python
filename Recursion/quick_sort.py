#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def partition(a,si,ei):
    pivot=a[si]
    c=0
    for i in range(si,ei+1):
        if a[i] < pivot:
            c=c+1
    a[si+c],a[si]=a[si],a[si+c]
    pivot_index=si+c
    
    i=si
    j=ei
    while i<j:
        if a[i]<pivot:
            i=i+1
        elif a[j]>=pivot:
            j=j-1
        else:
            a[i],a[j]=a[j],a[i]
            i=i+1
            j=j-1
    return pivot_index

def quickSort(a, si, ei):
    if si >= ei:
        return
    pivot_index=partition(a,si,ei)
    quickSort(a, si,pivot_index-1 )
    quickSort(a, pivot_index+1, ei)
   
    

n=int(input())
a=list(int(i) for i in input().strip().split(' '))
quickSort(a, 0, n-1)
print(*a)

