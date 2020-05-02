#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def frequency(l):
    map={}
    for num in l:
        map[num]=map.get(num,0)+1
    return map    
def printPairDiffK(l, k):
    m=frequency(l)
    for num in m:
        if num in m and num-k in m:
            if (num!=(num-k)):
                for _ in range(0,m[num]*m[num-k]):
                	print(num-k,num)
            else:
                for _ in range(0,m[num]*(m[num]-1)//2):
                	print(num-k,num)
#Implement Your Code Here


n=int(input())
l=list(int(i) for i in input().strip().split(' '))
k=int(input())
printPairDiffK(l, k)

