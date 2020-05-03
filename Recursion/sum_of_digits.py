#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
def sumofDigits(n):
   
    if n==0:
        return 0
       
    
    return n%10+sumofDigits(int(n/10))

    
    
n=int(input())
z=sumofDigits(n)
print(z)

