#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
def lastIndex(arr,x,si):
    l=len(arr)
    if si==l:
        return -1
    smallerListoutput=lastIndex(arr,x,si+1)
    if smallerListoutput != -1:
        return smallerListoutput
    else:
        if arr[si]==x:
            return si
        else:
            return -1
        
n=int(input())
arr=list(int (i) for i in input().strip().split(' '))
x=int(input())
Index=lastIndex(arr,x,0)
print(Index)

