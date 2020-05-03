#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
def sumofGP(k) :
    if k==0:
        return 1.00000
    
    return (1/2)**k+sumofGP(k-1)
      
      
k=int(input())
t=float(sumofGP(k))
print("%0.5f"%t)

