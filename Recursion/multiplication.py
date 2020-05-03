#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
def multiply(m,n):
    if n==0:
        return 0
    return m+multiply(m,n-1)

import sys
sys.setrecursionlimit(10000)
m=int(input())
n=int(input())
x=multiply(m,n)
print(x)

