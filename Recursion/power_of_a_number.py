#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
def pow(x,n):
    if n==0:
        return 1
    smallOutput=pow(x,n-1)
    return x*smallOutput


# Main
x,n =(int(i) for i in input().strip().split(' '))
k = pow(x,n)
print(k)

