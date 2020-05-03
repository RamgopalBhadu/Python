#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Read input as specified in the question.
## Print output as specified in the question.
def countZeroes(n):
   
    if n==0:
        return 0
        
 

    if n%10==0:
        small=countZeroes(int(n/10))
        return small+1
    else:
        small=countZeroes(int(n/10))
        return small
    
    
n=int(input())
z=countZeroes(n)
print(z)
    
    

