#!/usr/bin/env python
# coding: utf-8

# In[ ]:




def permutations(s):
    l=[]
    length=len(s)
    if length==1:
        return [s]
    for i in range(0,length):
        permu=permutations(s[0:i]+s[i+1:])
        for perm in permu:
            l.append(s[i]+perm)
    return l
    pass


string = input()
ans = permutations(string)
for s in ans:
    print(s)






