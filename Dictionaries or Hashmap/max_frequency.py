#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def maxFreq(l):
    d={}
    count,itm=0,''
    for n in l:
        d[n]=d.get(n,0) + 1
        if d[n]>count:
            count, itm=d[n],n
    return itm
    pass

# Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(maxFreq(l))

